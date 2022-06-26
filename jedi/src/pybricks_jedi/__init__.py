import io
import json
import re
from enum import IntEnum

import docstring_parser
import jedi
from jedi.api.classes import BaseName, Completion, Name, ParamName, Signature
from typing_extensions import NotRequired, TypedDict

# Packages included in Pybricks firmware that ships with Pybricks Code.
PYBRICKS_CODE_PACKAGES = {
    "micropython",
    "pybricks",
    "pybricks.geometry",
    "pybricks.hubs",
    "pybricks.iodevices",
    "pybricks.parameters",
    "pybricks.pupdevices",
    "pybricks.robotics",
    "pybricks.tools",
    "uerrno",
    "uio",
    "umath",
    "urandom",
    "uselect",
    "usys",
}

# Subset of Python builtins included in Pybricks MicroPython.
PYBRICKS_BUILTINS = {
    "abs",
    "all",
    "any",
    "ArithmeticError",
    "AssertionError",
    "AttributeError",
    "BaseException",
    "bin",
    "bool",
    "bytearray",
    "bytes",
    "callable",
    "chr",
    "classmethod",
    "complex",
    "dict",
    "dir",
    "divmod",
    "enumerate",
    "EOFError",
    "eval",
    "Exception",
    "exec",
    "float",
    "GeneratorExit",
    "getattr",
    "globals",
    "hasattr",
    "hash",
    "help",
    "hex",
    "id",
    "ImportError",
    "IndentationError",
    "IndexError",
    "input",
    "int",
    "isinstance",
    "issubclass",
    "iter",
    "KeyboardInterrupt",
    "KeyError",
    "len",
    "list",
    "locals",
    "LookupError",
    "map",
    "max",
    "MemoryError",
    "min",
    "NameError",
    "next",
    "NotImplementedError",
    "object",
    "oct",
    "ord",
    "OSError",
    "OverflowError",
    "pow",
    "print",
    "range",
    "repr",
    "reversed",
    "round",
    "RuntimeError",
    "set",
    "setattr",
    "slice",
    "sorted",
    "staticmethod",
    "StopIteration",
    "str",
    "sum",
    "super",
    "SyntaxError",
    "SystemExit",
    "tuple",
    "type",
    "TypeError",
    "ValueError",
    "ZeroDivisionError",
    "zip",
}

# Types from monaco editor


class IRange(TypedDict):
    startLineNumber: int
    startColumn: int
    endLineNumber: int
    endColumn: int


class ISingleEditOperation(TypedDict):
    range: IRange
    text: str  # TODO: can also be JavaScript null
    forceMoveMarkers: NotRequired[bool]


class Command(TypedDict):
    id: str
    title: str
    tooltip: NotRequired[str]
    arguments: NotRequired[list]


class UriComponents(TypedDict):
    scheme: str
    authority: str
    path: str
    query: str
    fragment: str


class IMarkdownString(TypedDict):
    value: str
    isTrusted: NotRequired[bool]
    supportThemeIcons: NotRequired[bool]
    supportHtml: NotRequired[bool]
    baseUri: NotRequired[UriComponents]
    uris: NotRequired[dict[str, UriComponents]]


class CompletionItemKind(IntEnum):
    Method = 0
    Function = 1
    Constructor = 2
    Field = 3
    Variable = 4
    Class = 5
    Struct = 6
    Interface = 7
    Module = 8
    Property = 9
    Event = 10
    Operator = 11
    Unit = 12
    Value = 13
    Constant = 14
    Enum = 15
    EnumMember = 16
    Keyword = 17
    Text = 18
    Color = 19
    File = 20
    Reference = 21
    Customcolor = 22
    Folder = 23
    TypeParameter = 24
    User = 25
    Issue = 26
    Snippet = 27


class CompletionItemTag(IntEnum):
    Deprecated = 1


class CompletionItemInsertTextRule(IntEnum):
    KeepWhitespace = 1
    InsertAsSnippet = 4


class CompletionItemLabel(TypedDict):
    label: str
    detail: NotRequired[str]
    description: NotRequired[str]


class CompletionItemRanges(TypedDict):
    insert: IRange
    replace: IRange


class CompletionItem(TypedDict):
    label: str | CompletionItemLabel
    kind: CompletionItemKind
    tags: NotRequired[list[CompletionItemTag]]
    detail: NotRequired[str]
    documentation: NotRequired[str]
    sortText: NotRequired[str]
    filterText: NotRequired[str]
    preselect: NotRequired[bool]
    insertText: str
    insertTextRules: NotRequired[CompletionItemInsertTextRule]
    range: IRange | CompletionItemRanges
    commitCharacters: NotRequired[list[str]]
    additionalTextEdits: NotRequired[list[ISingleEditOperation]]
    command: NotRequired[Command]


class ParameterInformation(TypedDict):
    label: str | tuple[int, int]
    documentation: NotRequired[str]


class SignatureInformation(TypedDict):
    label: str
    documentation: NotRequired[str]
    parameters: list[ParameterInformation]
    activeParameter: NotRequired[int]


class SignatureHelp(TypedDict):
    signatures: list[SignatureInformation]
    activeSignature: int
    activeParameter: int


def _is_pybricks(c: Completion) -> bool:
    # filter all "private" names (leading underscore)
    if (isinstance(c.name, str)) and c.name.startswith("_"):
        return False

    if isinstance(c.full_name, str):
        # this catches things like `from __future__ import annotations`
        if c.full_name.startswith("_") and c.module_name != "__main__":
            return False

        # filter out enum types
        if c.full_name.startswith("enum."):
            return False

        # filter out typing types
        if c.full_name.startswith("typing."):
            return False

    # filter out packages/modules that are not included in Pybricks firmware
    if c.type == "module" or c.type == "namespace":
        return c.full_name in PYBRICKS_CODE_PACKAGES

    # filter subset of builtins
    if c.module_name == "builtins" and c.type != "keyword":
        return c.name in PYBRICKS_BUILTINS

    # this is a type alias, not a real type
    if c.full_name == "pybricks.parameters.Number":
        return False

    return True


def _get_docstring(name: BaseName) -> str:
    """
    Gets the docstring for a name.
    """

    docstring = name.docstring(raw=True)

    # jedi does not appear to be smart enough to use __init__ docstring for class
    if name.type == "class" and isinstance(name, Name):
        n: Name
        for n in name.defined_names():
            if n.name == "__init__":
                docstring = "\n".join([docstring, _get_docstring(n)])

    return docstring


def _parse_docstring(text: str) -> tuple[IMarkdownString, list[IMarkdownString]]:
    """
    Parses a doc string, removes the overload declarations, performs some
    fixups and extracts the individual parameter strings.

    Args:
        The raw docstring.

    Returns:
        A tuple with the fixed up doc string and a list of parameter doc strings.
    """
    # docstring_parser does not support signatures at the beginning of the
    # docstring, so we have to remove them
    # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_docstring_signature

    lines, end_of_signatures = [], False

    for line in io.StringIO(text).readlines():
        # signatures look like: "name(params...)"
        if not end_of_signatures and re.match(r"^\w+\(.*\)", line):
            continue

        end_of_signatures = True

        # TODO: we may want to do some restructured text to markdown fixes,
        # e.g. strip off ":class:" from ":class:`SomeClass`" and replace
        # ".. some-directive::" with an appropriate header

        lines.append(line)

    text = "".join(lines)

    doc = docstring_parser.parse(text, docstring_parser.DocstringStyle.GOOGLE)

    # convert to numpy doc for better markdown rendering (section names are underlined)
    numpy_doc = docstring_parser.compose(doc, docstring_parser.Style.NUMPYDOC)

    docstring = IMarkdownString(value=numpy_doc)
    param_docstrings = [IMarkdownString(value=p.description) for p in doc.params]

    return docstring, param_docstrings


def _map_completion_kind(type: str) -> CompletionItemKind:
    match type:
        case "module":
            return CompletionItemKind.Module
        case "class":
            return CompletionItemKind.Class
        case "instance":
            return CompletionItemKind.Variable
        case "function":
            return CompletionItemKind.Function
        case "param":
            return CompletionItemKind.Variable
        case "path":
            return CompletionItemKind.File
        case "keyword":
            return CompletionItemKind.Keyword
        case "property":
            return CompletionItemKind.Property
        case "statement":
            return CompletionItemKind.Variable
        case _:
            return CompletionItemKind.User


def _map_completion_item(
    completion: Completion, line: int, column: int
) -> CompletionItem:
    """
    Maps a Jedi completion to a Monaco editor CompletionItem.

    Note: All members of the CompletionItem must be directly mappable without
    PyProxy in Pyodide.
    """
    return CompletionItem(
        insertText=completion.name_with_symbols,
        kind=_map_completion_kind(completion.type),
        label=completion.name_with_symbols,
        range=IRange(
            startLineNumber=line,
            startColumn=column - completion.get_completion_prefix_length(),
            endLineNumber=line,
            endColumn=column,
        ),
        documentation=_parse_docstring(_get_docstring(completion))[0],
    )


def _map_parameter(param: ParamName, docstr: str) -> ParameterInformation:
    return ParameterInformation(label=param.to_string(), documentation=docstr)


def _map_signature(signature: Signature) -> SignatureInformation:
    optional = {} if signature.index is None else dict(activeParameter=signature.index)

    docstr, param_docstr = _parse_docstring(_get_docstring(signature))

    return SignatureInformation(
        label=signature.to_string(),
        documentation=docstr,
        parameters=[_map_parameter(*p) for p in zip(signature.params, param_docstr)],
        **optional,
    )


def _map_signatures(signatures: list[Signature]) -> SignatureHelp:
    return SignatureHelp(
        signatures=[_map_signature(s) for s in signatures],
        activeSignature=0,
        activeParameter=0,
    )


def initialize():
    """
    Initialize jedi with Pybricks-specific config.
    """

    jedi.preload_module(
        "typing",
        "enum",
        "micropython",
        "pybricks._common",
        "pybricks.ev3dev",
        "pybricks.ev3dev.speaker",
        "pybricks.geometry",
        "pybricks.hubs",
        "pybricks.iodevices",
        "pybricks.parameters",
        "pybricks.pupdevices",
        "pybricks.robotics",
        "pybricks.tools",
        "pybricks",
        "ubuiltins",
        "uerrno",
        "uio",
        "ujson",
        "umath",
        "urandom",
        "uselect",
        "ustruct",
        "usys",
    )

    # also preload "everything" in builtins
    jedi.Script("").complete()


def complete(code: str, line: int, column: int) -> str:
    """
    Calls jedi.Script().complete() and filters the results for Pybricks.

    Args:
        code: The Python code to parse.
        line: The 1-based line number of the cursor position.
        column: The 1-based column number of the cursor position.

    Returns:
        A json string containing a filtered list of completion items.
    """
    completions = jedi.Script(code).complete(line, column - 1, fuzzy=True)
    return json.dumps(
        [_map_completion_item(c, line, column) for c in completions if _is_pybricks(c)]
    )


def get_signatures(code: str, line: int, column: int) -> str:
    """
    Calls jedi.Script().get_signatures().

    Args:
        code: The Python code to parse.
        line: The 1-based line number of the cursor position.
        column: The 1-based column number of the cursor position.

    Returns:
        A json string containing the signature help.
    """
    signatures = jedi.Script(code).get_signatures(line, column - 1)
    return json.dumps(_map_signatures(signatures))
