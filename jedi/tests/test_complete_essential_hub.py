# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of the EssentialHub class.
"""


import json
from pybricks_jedi import CompletionItem, complete

IMPORT = "from pybricks.hubs import EssentialHub"
CREATE_INSTANCE = "hub = EssentialHub()"


def _create_snippet(line: str) -> str:
    """
    Creates a code snippet::

        from pybricks.hubs import EssentialHub
        hub = EssentialHub()
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
        "button",
        "charger",
        "imu",
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


def test_hub_dot_buttons_dot():
    line = "hub.button."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "pressed",
    ]


def test_hub_dot_charger_dot():
    line = "hub.charger."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "connected",
        "current",
        "status",
    ]


def test_hub_dot_imu_dot():
    line = "hub.imu."
    code = _create_snippet(line)
    completions: list[CompletionItem] = json.loads(complete(code, 3, len(line) + 1))
    assert [c["insertText"] for c in completions] == [
        "acceleration",
        "angular_velocity",
        "heading",
        "reset_heading",
        "tilt",
        "up",
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
    ]
