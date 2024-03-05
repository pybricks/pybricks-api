# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of the CityHub class.
"""


import json
from pybricks_jedi import CompletionItem, complete

IMPORT = "from pybricks.hubs import CityHub"
CREATE_INSTANCE = "hub = CityHub()"


def _create_snippet(line: str) -> str:
    """
    Creates a code snippet::

        from pybricks.hubs import CityHub
        hub = CityHub()
        {line}

    Args:
        line: The value substituted for ``{line}``
    """
    return "\n".join((IMPORT, CREATE_INSTANCE, line))


def test_hub_dot():
    line = "hub."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "battery",
        "ble",
        "buttons",
        "light",
        "system",
    ]


def test_hub_dot_battery_dot():
    line = "hub.battery."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "current",
        "voltage",
    ]


def test_hub_dot_button_dot():
    line = "hub.buttons."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "pressed",
    ]


def test_hub_dot_light_dot():
    line = "hub.light."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "animate",
        "blink",
        "off",
        "on",
    ]


def test_hub_dot_system_dot():
    line = "hub.system."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "name",
        "reset_reason",
        "set_stop_button",
        "shutdown",
        "storage",
    ]
