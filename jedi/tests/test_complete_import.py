# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of import statements.
"""

import json

import pytest
from pybricks_jedi import CompletionItem, complete, update_user_modules


def test_from():
    code = "from "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    # only modules included in Pybricks firmware should be listed
    assert [c["insertText"] for c in completions] == [
        "micropython",
        "pybricks",
        "uerrno",
        "uio",
        "ujson",
        "umath",
        "urandom",
        "uselect",
        "ustruct",
        "usys",
    ]


@pytest.fixture
def user_modules():
    update_user_modules(["jedi", "pytest"])
    yield
    update_user_modules([])


def test_from_with_user_modules(user_modules):
    code = "from "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "jedi",
        "micropython",
        "pybricks",
        "pytest",
        "uerrno",
        "uio",
        "ujson",
        "umath",
        "urandom",
        "uselect",
        "ustruct",
        "usys",
    ]


def test_from_pybricks_import():
    code = "from pybricks import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "hubs",
        "iodevices",
        "parameters",
        "pupdevices",
        "robotics",
        "tools",
        "version",
    ]


def test_from_pybricks_dot():
    code = "from pybricks."
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "hubs",
        "iodevices",
        "parameters",
        "pupdevices",
        "robotics",
        "tools",
    ]


def test_from_pybricks_hubs_import():
    code = "from pybricks.hubs import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "CityHub",
        "EssentialHub",
        "EV3Brick",
        "InventorHub",
        "MoveHub",
        "PrimeHub",
        "TechnicHub",
    ]


def test_from_pybricks_iodevices_import():
    code = "from pybricks.iodevices import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "AnalogSensor",
        "DCMotor",
        "Ev3devSensor",
        "I2CDevice",
        "LUMPDevice",
        "LWP3Device",
        "PUPDevice",
        "UARTDevice",
        "XboxController",
    ]


def test_from_pybricks_parameters_import():
    code = "from pybricks.parameters import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "Axis",
        "Button",
        "Color",
        "Direction",
        "Icon",
        "Port",
        "Side",
        "Stop",
    ]


def test_from_pybricks_pupdevices_import():
    code = "from pybricks.pupdevices import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "ColorDistanceSensor",
        "ColorLightMatrix",
        "ColorSensor",
        "DCMotor",
        "ForceSensor",
        "InfraredSensor",
        "Light",
        "Motor",
        "PFMotor",
        "Remote",
        "TiltSensor",
        "UltrasonicSensor",
    ]


def test_from_pybricks_robotics_import():
    code = "from pybricks.robotics import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == ["Car", "DriveBase"]


def test_from_pybricks_tools_import():
    code = "from pybricks.tools import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "cross",
        "DataLog",
        "hub_menu",
        "Matrix",
        "multitask",
        "read_input_byte",
        "run_task",
        "StopWatch",
        "vector",
        "wait",
    ]


def test_from_micropython_import():
    code = "from micropython import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "const",
        "heap_lock",
        "heap_unlock",
        "kbd_intr",
        "mem_info",
        "opt_level",
        "qstr_info",
        "stack_use",
    ]


def test_from_uerrno_import():
    code = "from uerrno import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "EAGAIN",
        "EBUSY",
        "ECANCELED",
        "EINVAL",
        "EIO",
        "ENODEV",
        "EOPNOTSUPP",
        "EPERM",
        "errorcode",
        "ETIMEDOUT",
    ]


def test_from_uio_import():
    code = "from uio import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "BytesIO",
        "FileIO",
        "StringIO",
    ]


def test_from_ujson_import():
    code = "from ujson import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "decode",  # FIXME: Shouldn't be here
        "dump",
        "dumps",
        "encode",  # FIXME: Shouldn't be here
        "load",
        "loads",
    ]


def test_from_umath_import():
    code = "from umath import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "acos",
        "asin",
        "atan",
        "atan2",
        "ceil",
        "copysign",
        "cos",
        "degrees",
        "e",
        "exp",
        "fabs",
        "floor",
        "fmod",
        "frexp",
        "isfinite",
        "isinfinite",
        "isnan",
        "ldexp",
        "log",
        "modf",
        "pi",
        "pow",
        "radians",
        "sin",
        "sqrt",
        "tan",
        "trunc",
    ]


def test_from_urandom_import():
    code = "from urandom import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "choice",
        "getrandbits",
        "randint",
        "random",
        "randrange",
        "seed",
        "uniform",
    ]


def test_from_uselect_import():
    code = "from uselect import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "Poll",
        "poll",
        "POLLERR",
        "POLLHUP",
        "POLLIN",
        "POLLOUT",
    ]


def test_from_ustruct_import():
    code = "from ustruct import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "calcsize",
        "pack",
        "pack_into",
        "unpack",
        "unpack_from",
    ]


def test_from_usys_import():
    code = "from usys import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "implementation",
        "stderr",
        "stdin",
        "stdout",
        "version",
        "version_info",
    ]
