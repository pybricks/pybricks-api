import json
from pybricks_jedi import CompletionItem, complete


def test_get_completion_for_private_globals():
    code = """
_X = 0

_
"""
    completions: list[CompletionItem] = json.loads(complete(code, 4, 2))
    assert [c["insertText"] for c in completions] == ["_X", "__name__"]


def test_get_completion_for_private_attributes():
    code = """
class X:
    def __init__(self):
        self.public = 0
        self._protected = 0
        self.__private = 0

x = X()

x.
"""
    completions: list[CompletionItem] = json.loads(complete(code, 10, 3))
    assert [c["insertText"] for c in completions] == [
        "public",
        "_protected",
        "__init__",
    ]
