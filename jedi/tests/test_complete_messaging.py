# SPDX-License-Identifier: MIT
# Copyright (c) 2026 The Pybricks Authors

"""
Tests for correct code completion of the messaging module.
"""

import json

import pytest
from pybricks_jedi import CompletionItem, complete


def test_from_pybricks_messaging_import():
    code = "from pybricks.messaging import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "AppData",
        "BLERadio",
        "BluetoothMailboxClient",
        "BluetoothMailboxServer",
        "Connection",
        "HubNetwork",
        "LogicMailbox",
        "Mailbox",
        "NumericMailbox",
        "TextMailbox",
    ]


def test_ble_radio_dot():
    code = "\n".join(
        [
            "from pybricks.messaging import BLERadio",
            "ble = BLERadio()",
            "ble.",
        ]
    )
    completions: list[CompletionItem] = json.loads(complete(code, 3, 5))
    assert [c["insertText"] for c in completions] == [
        "broadcast",
        "observe",
        "signal_strength",
        "version",
    ]


def test_hub_network_dot():
    code = "\n".join(
        [
            "from pybricks.messaging import HubNetwork",
            "network = HubNetwork()",
            "network.",
        ]
    )
    completions: list[CompletionItem] = json.loads(complete(code, 3, 9))
    assert [c["insertText"] for c in completions] == [
        "address",
        "connect",
        "inbox",
        "is_connected",
        "send",
    ]


def test_app_data_dot():
    code = "\n".join(
        [
            "from pybricks.messaging import AppData",
            "app = AppData([(0, 4)])",
            "app.",
        ]
    )
    completions: list[CompletionItem] = json.loads(complete(code, 3, 5))
    assert [c["insertText"] for c in completions] == [
        "close",
        "configure",
        "get_bytes",
        "write_bytes",
    ]
