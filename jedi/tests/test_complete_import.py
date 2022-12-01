# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct code completion of import statements.
"""

import json
from pybricks_jedi import CompletionItem, complete


def test_from():
    code = "from "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    # only modules included in Pybricks firmware should be listed
    assert [c["insertText"] for c in completions] == [
        "micropython",
        "pybricks",
        "uerrno",
        "uio",
        "umath",
        "urandom",
        "uselect",
        "usys",
    ]


def test_from_pybricks_import():
    code = "from pybricks import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "geometry",
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
        "geometry",
        "hubs",
        "iodevices",
        "parameters",
        "pupdevices",
        "robotics",
        "tools",
    ]


def test_from_pybricks_geometry_import():
    code = "from pybricks.geometry import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "Axis",
        "Matrix",
        "vector",
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
    ]


def test_from_pybricks_parameters_import():
    code = "from pybricks.parameters import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
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
    assert [c["insertText"] for c in completions] == [
        "DriveBase",
    ]


def test_from_pybricks_tools_import():
    code = "from pybricks.tools import "
    completions: list[CompletionItem] = json.loads(complete(code, 1, len(code) + 1))
    assert [c["insertText"] for c in completions] == [
        "DataLog",
        "StopWatch",
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
        "poll",
        "Poll",
        "POLLERR",
        "POLLHUP",
        "POLLIN",
        "POLLOUT",
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
