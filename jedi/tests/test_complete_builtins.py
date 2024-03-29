# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of builtins.
"""


import json

import pytest

from pybricks_jedi import CompletionItem, complete


def test_empty_code():
    code = ""
    completions: list[CompletionItem] = json.loads(complete(code, 1, 1))
    # since nothing has been imported, this is just all builtins and keywords
    assert [c["insertText"] for c in completions] == [
        "abs",
        "all",
        "any",
        "ArithmeticError",
        "assert",
        "AssertionError",
        "async",
        "AttributeError",
        "await",
        "BaseException",
        "bin",
        "bool",
        "break",
        "bytearray",
        "bytes",
        "callable",
        "chr",
        "class",
        "classmethod",
        "complex",
        "continue",
        "def",
        "del",
        "dict",
        "dir",
        "divmod",
        "enumerate",
        "EOFError",
        "eval",
        "Exception",
        "exec",
        "False",
        "float",
        "for",
        "from",
        "GeneratorExit",
        "getattr",
        "global",
        "globals",
        "hasattr",
        "hash",
        "help",
        "hex",
        "id",
        "if",
        "import",
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
        "lambda",
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
        "None",
        "nonlocal",
        "not",
        "NotImplementedError",
        "object",
        "oct",
        "ord",
        "OSError",
        "OverflowError",
        "pass",
        "pow",
        "print",
        "raise",
        "range",
        "repr",
        "return",
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
        "True",
        "try",
        "tuple",
        "type",
        "TypeError",
        "ValueError",
        "while",
        "with",
        "yield",
        "ZeroDivisionError",
        "zip",
        "__name__",
    ]


FUNCTION_PARAMS = [
    pytest.param(
        "''.",
        [
            "count",
            "endswith",
            "find",
            "format",
            "index",
            "isalpha",
            "isdigit",
            "islower",
            "isspace",
            "isupper",
            "join",
            "lower",
            "lstrip",
            "replace",
            "rfind",
            "rindex",
            "rsplit",
            "rstrip",
            "split",
            "startswith",
            "strip",
            "upper",
        ],
    ),
    pytest.param(
        "str().",
        [
            "count",
            "endswith",
            "find",
            "format",
            "index",
            "isalpha",
            "isdigit",
            "islower",
            "isspace",
            "isupper",
            "join",
            "lower",
            "lstrip",
            "replace",
            "rfind",
            "rindex",
            "rsplit",
            "rstrip",
            "split",
            "startswith",
            "strip",
            "upper",
        ],
    ),
    pytest.param("(0).", ["from_bytes", "to_bytes"]),
    pytest.param("int().", ["from_bytes", "to_bytes"]),
    pytest.param(
        "{}.",
        [
            "clear",
            "copy",
            "fromkeys",
            "get",
            "items",
            "keys",
            "pop",
            "popitem",
            "setdefault",
            "update",
            "values",
        ],
    ),
    pytest.param(
        "dict().",
        [
            "clear",
            "copy",
            "fromkeys",
            "get",
            "items",
            "keys",
            "pop",
            "popitem",
            "setdefault",
            "update",
            "values",
        ],
    ),
    pytest.param(
        "[].",
        [
            "append",
            "clear",
            "copy",
            "count",
            "extend",
            "index",
            "insert",
            "pop",
            "remove",
            "reverse",
            "sort",
        ],
    ),
    pytest.param(
        "list().",
        [
            "append",
            "clear",
            "copy",
            "count",
            "extend",
            "index",
            "insert",
            "pop",
            "remove",
            "reverse",
            "sort",
        ],
    ),
    pytest.param("().", ["count", "index"]),
    pytest.param("tuple().", ["count", "index"]),
    pytest.param("bytearray().", ["append", "extend"]),
    pytest.param("bytes().", []),
    pytest.param("b''.", []),
    pytest.param("float().", []),
    pytest.param("(0.0).", []),
    pytest.param("complex().", []),
    pytest.param("type().", []),
]


@pytest.mark.parametrize("code,attributes", FUNCTION_PARAMS)
def test_get_completion_for_builtins(code: str, attributes: list[str]):
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == attributes
