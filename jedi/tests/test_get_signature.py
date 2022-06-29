# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors

"""
Tests for correct signatures of the pupdevices.Motor class.
"""


from itertools import zip_longest
import json

import pytest
from pybricks_jedi import SignatureHelp, get_signatures


def _get_function_signature(module: str, function: str) -> SignatureHelp:
    """
    Gets the signature help object for code like::

        from {module} import {function}
        {function}(

    Args:
        module: the module name
        func: the function name (a function in the module)
    """
    code = f"from {module} import {function}; {function}("
    return json.loads(get_signatures(code, 1, len(code) + 1))


FUNCTION_PARAMS = [
    pytest.param("pybricks.tools", "wait", [(["time: Number"], "None")]),
    pytest.param(
        "pybricks.geometry",
        "vector",
        [
            (["x: float", "y: float"], "Matrix"),
            (["x: float", "y: float", "z: float"], "Matrix"),
        ],
    ),
]


@pytest.mark.parametrize("module,function,signatures", FUNCTION_PARAMS)
def test_get_signature_for_functions(
    module: str, function: str, signatures: list[tuple[list[str], str]]
):
    help = _get_function_signature(module, function)

    assert help["activeSignature"] == 0
    assert help["activeParameter"] == 0
    assert help["signatures"]

    for sig, (params, returns) in zip_longest(help["signatures"], signatures):
        assert sig["label"] == f"{function}({', '.join(params)}) -> {returns}"
        assert sig["documentation"]["value"]
        # ensure signatures are stripped from doc comment
        assert not sig["documentation"]["value"].startswith(f"{function}(")

        for pi, p in zip_longest(sig["parameters"], params):
            assert pi["label"] == p
            assert pi["documentation"]["value"]


def _get_constructor_signature(module: str, type: str) -> SignatureHelp:
    """
    Gets the signature help object for code like::

        from {module} import {type}
        instance = {type}(

    Args:
        module: the module name
        type: the type name (a type in the module)
    """
    code = f"from {module} import {type}; {type}("
    return json.loads(get_signatures(code, 1, len(code) + 1))


CONSTRUCTOR_PARAMS = [
    pytest.param("pybricks.hubs", "MoveHub", [[]]),
    pytest.param("pybricks.hubs", "CityHub", [[]]),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        [["top_side: Axis=Axis.Z", "front_side: Axis=Axis.X"]],
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        [["top_side: Axis=Axis.Z", "front_side: Axis=Axis.X"]],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "DCMotor",
        [["port: Port", "positive_direction: Direction=Direction.CLOCKWISE"]],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        [
            [
                "port: Port",
                "positive_direction: Direction=Direction.CLOCKWISE",
                "gears: Optional[Union[Collection[int], Collection[Collection[int]]]]=None",
                "reset_angle: bool=True",
            ]
        ],
    ),
    pytest.param("pybricks.pupdevices", "TiltSensor", [["port: Port"]]),
    pytest.param("pybricks.pupdevices", "InfraredSensor", [["port: Port"]]),
    pytest.param("pybricks.pupdevices", "ColorDistanceSensor", [["port: Port"]]),
    pytest.param(
        "pybricks.pupdevices",
        "PFMotor",
        [
            [
                "sensor: ColorDistanceSensor",
                "channel: int",
                "color: Color",
                "positive_direction: Direction=Direction.CLOCKWISE",
            ]
        ],
    ),
    pytest.param("pybricks.pupdevices", "ColorSensor", [["port: Port"]]),
    pytest.param("pybricks.pupdevices", "UltrasonicSensor", [["port: Port"]]),
    pytest.param("pybricks.pupdevices", "ForceSensor", [["port: Port"]]),
    pytest.param("pybricks.pupdevices", "ColorLightMatrix", [["port: Port"]]),
    pytest.param("pybricks.pupdevices", "Light", [["port: Port"]]),
    pytest.param(
        "pybricks.pupdevices",
        "Remote",
        [["name: Optional[str]=None", "timeout: int=10000"]],
    ),
    # TODO: iodevices go here
    pytest.param(
        "pybricks.parameters",
        "Color",
        [["h: Number", "s: Number=100", "v: Number=100"]],
    ),
    pytest.param(
        "pybricks.robotics",
        "DriveBase",
        [
            [
                "left_motor: Motor",
                "right_motor: Motor",
                "wheel_diameter: Number",
                "axle_track: Number",
            ]
        ],
    ),
    pytest.param(
        "pybricks.geometry",
        "Matrix",
        [["rows: Sequence[Sequence[float]]"]],
    ),
]


@pytest.mark.parametrize("module,type,signatures", CONSTRUCTOR_PARAMS)
def test_get_signature_for_constructors(
    module: str, type: str, signatures: list[list[str]]
):
    help = _get_constructor_signature(module, type)

    assert help["activeSignature"] == 0
    assert help["activeParameter"] == 0
    assert help["signatures"]

    for sig, params in zip_longest(help["signatures"], signatures):
        assert sig["label"] == f"{type}({', '.join(params)})"
        assert sig["documentation"]["value"]
        # ensure signatures are stripped from doc comment
        assert not sig["documentation"]["value"].startswith(f"{type}(")

        for pi, p in zip_longest(sig["parameters"], params):
            assert pi["label"] == p
            assert pi["documentation"]["value"]


def _get_method_signature(module: str, type: str, method: str) -> SignatureHelp:
    """
    Gets the signature help object for code like::

        from {module} import {type}
        instance = {type}()
        instance.{method}(

    Args:
        module: the module name
        type: the type name (a type in the module)
        method: the method name (a method of the type)
    """
    code = f"from {module} import {type}; x = {type}(); x.{method}("
    return json.loads(get_signatures(code, 1, len(code) + 1))


METHOD_PARAMS = [
    pytest.param("pybricks.hubs", "MoveHub", "light.on", [(["color: Color"], "None")]),
    pytest.param("pybricks.hubs", "MoveHub", "light.off", [([], "None")]),
    pytest.param(
        "pybricks.hubs",
        "MoveHub",
        "light.blink",
        [(["color: Color", "durations: Collection[Number]"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "MoveHub",
        "light.animate",
        [(["colors: Collection[Color]", "interval: Number"], "None")],
    ),
    pytest.param("pybricks.hubs", "MoveHub", "imu.up", [([], "Side")]),
    pytest.param(
        "pybricks.hubs", "MoveHub", "imu.acceleration", [([], "Tuple[int, int, int]")]
    ),
    pytest.param("pybricks.hubs", "MoveHub", "battery.voltage", [([], "int")]),
    pytest.param("pybricks.hubs", "MoveHub", "battery.current", [([], "int")]),
    pytest.param(
        "pybricks.hubs", "MoveHub", "button.pressed", [([], "Collection[Button]")]
    ),
    pytest.param(
        "pybricks.hubs",
        "MoveHub",
        "system.set_stop_button",
        [(["button: Optional[Union[Button, Iterable[Button]]]"], "None")],
    ),
    pytest.param("pybricks.hubs", "MoveHub", "system.name", [([], "str")]),
    pytest.param("pybricks.hubs", "MoveHub", "system.shutdown", [([], "None")]),
    pytest.param("pybricks.hubs", "MoveHub", "system.reset_reason", [([], "int")]),
    pytest.param("pybricks.hubs", "CityHub", "light.on", [(["color: Color"], "None")]),
    pytest.param("pybricks.hubs", "CityHub", "light.off", [([], "None")]),
    pytest.param(
        "pybricks.hubs",
        "CityHub",
        "light.blink",
        [(["color: Color", "durations: Collection[Number]"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "CityHub",
        "light.animate",
        [(["colors: Collection[Color]", "interval: Number"], "None")],
    ),
    pytest.param("pybricks.hubs", "CityHub", "battery.voltage", [([], "int")]),
    pytest.param("pybricks.hubs", "CityHub", "battery.current", [([], "int")]),
    pytest.param(
        "pybricks.hubs", "CityHub", "button.pressed", [([], "Collection[Button]")]
    ),
    pytest.param(
        "pybricks.hubs",
        "CityHub",
        "system.set_stop_button",
        [(["button: Optional[Union[Button, Iterable[Button]]]"], "None")],
    ),
    pytest.param("pybricks.hubs", "CityHub", "system.name", [([], "str")]),
    pytest.param("pybricks.hubs", "CityHub", "system.shutdown", [([], "None")]),
    pytest.param("pybricks.hubs", "CityHub", "system.reset_reason", [([], "int")]),
    pytest.param(
        "pybricks.hubs", "TechnicHub", "light.on", [(["color: Color"], "None")]
    ),
    pytest.param("pybricks.hubs", "TechnicHub", "light.off", [([], "None")]),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        "light.blink",
        [(["color: Color", "durations: Collection[Number]"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        "light.animate",
        [(["colors: Collection[Color]", "interval: Number"], "None")],
    ),
    pytest.param("pybricks.hubs", "TechnicHub", "imu.up", [([], "Side")]),
    pytest.param("pybricks.hubs", "TechnicHub", "imu.tilt", [([], "Tuple[int, int]")]),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        "imu.acceleration",
        [(["axis: Axis"], "float"), ([], "Matrix")],
    ),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        "imu.angular_velocity",
        [(["axis: Axis"], "float"), ([], "Matrix")],
    ),
    pytest.param("pybricks.hubs", "TechnicHub", "imu.heading", [([], "float")]),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        "imu.reset_heading",
        [(["angle: Number"], "None")],
    ),
    pytest.param("pybricks.hubs", "TechnicHub", "battery.voltage", [([], "int")]),
    pytest.param("pybricks.hubs", "TechnicHub", "battery.current", [([], "int")]),
    pytest.param(
        "pybricks.hubs", "TechnicHub", "button.pressed", [([], "Collection[Button]")]
    ),
    pytest.param(
        "pybricks.hubs",
        "TechnicHub",
        "system.set_stop_button",
        [(["button: Optional[Union[Button, Iterable[Button]]]"], "None")],
    ),
    pytest.param("pybricks.hubs", "TechnicHub", "system.name", [([], "str")]),
    pytest.param("pybricks.hubs", "TechnicHub", "system.shutdown", [([], "None")]),
    pytest.param("pybricks.hubs", "TechnicHub", "system.reset_reason", [([], "int")]),
    pytest.param("pybricks.hubs", "PrimeHub", "light.on", [(["color: Color"], "None")]),
    pytest.param("pybricks.hubs", "PrimeHub", "light.off", [([], "None")]),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "light.blink",
        [(["color: Color", "durations: Collection[Number]"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "light.animate",
        [(["colors: Collection[Color]", "interval: Number"], "None")],
    ),
    pytest.param(
        "pybricks.hubs", "PrimeHub", "display.orientation", [(["up: Side"], "None")]
    ),
    pytest.param("pybricks.hubs", "PrimeHub", "display.off", [([], "None")]),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "display.pixel",
        [(["row: Number", "column: Number", "brightness: Number=100"], "None")],
    ),
    pytest.param(
        "pybricks.hubs", "PrimeHub", "display.image", [(["matrix: Matrix"], "None")]
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "display.animate",
        [(["matrices: Collection[Matrix]", "interval: Number"], "None")],
    ),
    pytest.param(
        "pybricks.hubs", "PrimeHub", "display.number", [(["number: Number"], "None")]
    ),
    pytest.param(
        "pybricks.hubs", "PrimeHub", "display.char", [(["char: str"], "None")]
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "display.text",
        [(["text: str", "on: Number=500", "off: Number=50"], "None")],
    ),
    pytest.param(
        "pybricks.hubs", "PrimeHub", "buttons.pressed", [([], "Collection[Button]")]
    ),
    pytest.param("pybricks.hubs", "PrimeHub", "imu.up", [([], "Side")]),
    pytest.param("pybricks.hubs", "PrimeHub", "imu.tilt", [([], "Tuple[int, int]")]),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "imu.acceleration",
        [(["axis: Axis"], "float"), ([], "Matrix")],
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "imu.angular_velocity",
        [(["axis: Axis"], "float"), ([], "Matrix")],
    ),
    pytest.param("pybricks.hubs", "PrimeHub", "imu.heading", [([], "float")]),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "imu.reset_heading",
        [(["angle: Number"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "speaker.volume",
        [(["volume: Number"], "None"), ([], "int")],
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "speaker.beep",
        [(["frequency: Number=500", "duration: Number=100"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "speaker.play_notes",
        [(["notes: Iterable[str]", "tempo: Number=120"], "None")],
    ),
    pytest.param("pybricks.hubs", "PrimeHub", "battery.voltage", [([], "int")]),
    pytest.param("pybricks.hubs", "PrimeHub", "battery.current", [([], "int")]),
    pytest.param("pybricks.hubs", "PrimeHub", "charger.connected", [([], "bool")]),
    pytest.param("pybricks.hubs", "PrimeHub", "charger.current", [([], "int")]),
    pytest.param("pybricks.hubs", "PrimeHub", "charger.status", [([], "int")]),
    pytest.param(
        "pybricks.hubs",
        "PrimeHub",
        "system.set_stop_button",
        [(["button: Optional[Union[Button, Iterable[Button]]]"], "None")],
    ),
    pytest.param("pybricks.hubs", "PrimeHub", "system.name", [([], "str")]),
    pytest.param("pybricks.hubs", "PrimeHub", "system.shutdown", [([], "None")]),
    pytest.param("pybricks.hubs", "PrimeHub", "system.reset_reason", [([], "int")]),
    pytest.param(
        "pybricks.hubs", "EssentialHub", "light.on", [(["color: Color"], "None")]
    ),
    pytest.param("pybricks.hubs", "EssentialHub", "light.off", [([], "None")]),
    pytest.param(
        "pybricks.hubs",
        "EssentialHub",
        "light.blink",
        [(["color: Color", "durations: Collection[Number]"], "None")],
    ),
    pytest.param(
        "pybricks.hubs",
        "EssentialHub",
        "light.animate",
        [(["colors: Collection[Color]", "interval: Number"], "None")],
    ),
    pytest.param(
        "pybricks.hubs", "EssentialHub", "button.pressed", [([], "Collection[Button]")]
    ),
    pytest.param("pybricks.hubs", "EssentialHub", "imu.up", [([], "Side")]),
    pytest.param(
        "pybricks.hubs", "EssentialHub", "imu.tilt", [([], "Tuple[int, int]")]
    ),
    pytest.param(
        "pybricks.hubs",
        "EssentialHub",
        "imu.acceleration",
        [(["axis: Axis"], "float"), ([], "Matrix")],
    ),
    pytest.param(
        "pybricks.hubs",
        "EssentialHub",
        "imu.angular_velocity",
        [(["axis: Axis"], "float"), ([], "Matrix")],
    ),
    pytest.param("pybricks.hubs", "EssentialHub", "imu.heading", [([], "float")]),
    pytest.param(
        "pybricks.hubs",
        "EssentialHub",
        "imu.reset_heading",
        [(["angle: Number"], "None")],
    ),
    pytest.param("pybricks.hubs", "EssentialHub", "battery.voltage", [([], "int")]),
    pytest.param("pybricks.hubs", "EssentialHub", "battery.current", [([], "int")]),
    pytest.param("pybricks.hubs", "EssentialHub", "charger.connected", [([], "bool")]),
    pytest.param("pybricks.hubs", "EssentialHub", "charger.current", [([], "int")]),
    pytest.param("pybricks.hubs", "EssentialHub", "charger.status", [([], "int")]),
    pytest.param(
        "pybricks.hubs",
        "EssentialHub",
        "system.set_stop_button",
        [(["button: Optional[Union[Button, Iterable[Button]]]"], "None")],
    ),
    pytest.param("pybricks.hubs", "EssentialHub", "system.name", [([], "str")]),
    pytest.param("pybricks.hubs", "EssentialHub", "system.shutdown", [([], "None")]),
    pytest.param("pybricks.hubs", "EssentialHub", "system.reset_reason", [([], "int")]),
    # TODO: iodevices module here
    pytest.param("pybricks.pupdevices", "DCMotor", "dc", [(["duty: Number"], "None")]),
    pytest.param("pybricks.pupdevices", "DCMotor", "stop", [([], "None")]),
    pytest.param("pybricks.pupdevices", "DCMotor", "brake", [([], "None")]),
    pytest.param(
        "pybricks.pupdevices",
        "DCMotor",
        "settings",
        [(["max_voltage: Number"], "None"), ([], "Tuple[int]")],
    ),
    pytest.param("pybricks.pupdevices", "Motor", "speed", [([], "int")]),
    pytest.param("pybricks.pupdevices", "Motor", "angle", [([], "int")]),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "reset_angle",
        [(["angle: Optional[Number]=None"], "None")],
    ),
    pytest.param("pybricks.pupdevices", "Motor", "stop", [([], "None")]),
    pytest.param("pybricks.pupdevices", "Motor", "brake", [([], "None")]),
    pytest.param("pybricks.pupdevices", "Motor", "hold", [([], "None")]),
    pytest.param("pybricks.pupdevices", "Motor", "run", [(["speed: Number"], "None")]),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "run_time",
        [
            (
                [
                    "speed: Number",
                    "time: Number",
                    "then: Stop=Stop.HOLD",
                    "wait: bool=True",
                ],
                "None",
            )
        ],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "run_angle",
        [
            (
                [
                    "speed: Number",
                    "rotation_angle: Number",
                    "then: Stop=Stop.HOLD",
                    "wait: bool=True",
                ],
                "None",
            )
        ],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "run_target",
        [
            (
                [
                    "speed: Number",
                    "target_angle: Number",
                    "then: Stop=Stop.HOLD",
                    "wait: bool=True",
                ],
                "None",
            )
        ],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "track_target",
        [(["target_angle: Number"], "None")],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "run_until_stalled",
        [
            (
                [
                    "speed: Number",
                    "then: Stop=Stop.COAST",
                    "duty_limit: Optional[Number]=None",
                ],
                "int",
            )
        ],
    ),
    pytest.param("pybricks.pupdevices", "Motor", "dc", [(["duty: Number"], "None")]),
    pytest.param("pybricks.pupdevices", "Motor", "control.done", [([], "bool")]),
    pytest.param("pybricks.pupdevices", "Motor", "control.stalled", [([], "bool")]),
    pytest.param("pybricks.pupdevices", "Motor", "control.load", [([], "int")]),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "settings",
        [(["max_voltage: Number"], "None"), ([], "Tuple[int]")],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "control.limits",
        [
            (
                [
                    "speed: Optional[Number]=None",
                    "acceleration: Optional[Number]=None",
                    "torque: Optional[Number]=None",
                ],
                "None",
            ),
            ([], "Tuple[int, int, int]"),
        ],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "control.pid",
        [
            (
                [
                    "kp: Optional[Number]=None",
                    "ki: Optional[Number]=None",
                    "kd: Optional[Number]=None",
                    "reserved: Optional[Number]=None",
                    "integral_rate: Optional[Number]=None",
                ],
                "None",
            ),
            ([], "Tuple[int, int, int, None, int]"),
        ],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "control.target_tolerances",
        [
            (
                [
                    "speed: Optional[Number]=None",
                    "position: Optional[Number]=None",
                ],
                "None",
            ),
            ([], "Tuple[int, int]"),
        ],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "Motor",
        "control.stall_tolerances",
        [
            (
                [
                    "speed: Optional[Number]=None",
                    "time: Optional[Number]=None",
                ],
                "None",
            ),
            ([], "Tuple[int, int]"),
        ],
    ),
    pytest.param(
        "pybricks.pupdevices", "TiltSensor", "tilt", [([], "Tuple[int, int]")]
    ),
    pytest.param("pybricks.pupdevices", "InfraredSensor", "distance", [([], "int")]),
    pytest.param("pybricks.pupdevices", "InfraredSensor", "reflection", [([], "int")]),
    pytest.param("pybricks.pupdevices", "InfraredSensor", "count", [([], "int")]),
    pytest.param(
        "pybricks.pupdevices", "ColorDistanceSensor", "color", [([], "Color")]
    ),
    pytest.param(
        "pybricks.pupdevices", "ColorDistanceSensor", "reflection", [([], "int")]
    ),
    pytest.param(
        "pybricks.pupdevices", "ColorDistanceSensor", "ambient", [([], "int")]
    ),
    pytest.param(
        "pybricks.pupdevices", "ColorDistanceSensor", "distance", [([], "int")]
    ),
    pytest.param("pybricks.pupdevices", "ColorDistanceSensor", "hsv", [([], "Color")]),
    pytest.param(
        "pybricks.pupdevices",
        "ColorDistanceSensor",
        "detectable_colors",
        [(["colors: Collection[Color]"], "None"), ([], "Collection[Color]")],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "ColorDistanceSensor",
        "light.on",
        [(["color: Color"], "None")],
    ),
    pytest.param(
        "pybricks.pupdevices", "ColorDistanceSensor", "light.off", [([], "None")]
    ),
    pytest.param("pybricks.pupdevices", "PFMotor", "dc", [(["duty: Number"], "None")]),
    pytest.param("pybricks.pupdevices", "PFMotor", "stop", [([], "None")]),
    pytest.param("pybricks.pupdevices", "PFMotor", "brake", [([], "None")]),
    pytest.param(
        "pybricks.pupdevices",
        "ColorSensor",
        "color",
        [(["surface: bool=True"], "Optional[Color]")],
    ),
    pytest.param("pybricks.pupdevices", "ColorSensor", "reflection", [([], "int")]),
    pytest.param("pybricks.pupdevices", "ColorSensor", "ambient", [([], "int")]),
    pytest.param(
        "pybricks.pupdevices",
        "ColorSensor",
        "hsv",
        [(["surface: bool=True"], "Color")],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "ColorSensor",
        "detectable_colors",
        [(["colors: Collection[Color]"], "None"), ([], "Collection[Color]")],
    ),
    pytest.param(
        "pybricks.pupdevices",
        "ColorSensor",
        "lights.on",
        [(["brightness: Union[Number, Tuple[Number, Number, Number]]"], "None")],
    ),
    pytest.param("pybricks.pupdevices", "ColorSensor", "lights.off", [([], "None")]),
    pytest.param("pybricks.pupdevices", "UltrasonicSensor", "distance", [([], "int")]),
    pytest.param("pybricks.pupdevices", "UltrasonicSensor", "presence", [([], "bool")]),
    pytest.param(
        "pybricks.pupdevices",
        "UltrasonicSensor",
        "lights.on",
        [
            (
                ["brightness: Union[Number, Tuple[Number, Number, Number, Number]]"],
                "None",
            )
        ],
    ),
    pytest.param(
        "pybricks.pupdevices", "UltrasonicSensor", "lights.off", [([], "None")]
    ),
    pytest.param("pybricks.pupdevices", "ForceSensor", "force", [([], "float")]),
    pytest.param("pybricks.pupdevices", "ForceSensor", "distance", [([], "float")]),
    pytest.param(
        "pybricks.pupdevices",
        "ForceSensor",
        "pressed",
        [(["force: Number=3"], "bool")],
    ),
    pytest.param("pybricks.pupdevices", "ForceSensor", "touched", [([], "bool")]),
    pytest.param(
        "pybricks.pupdevices",
        "ColorLightMatrix",
        "on",
        [(["color: Union[Color, Collection[Color]]"], "None")],
    ),
    pytest.param("pybricks.pupdevices", "ColorLightMatrix", "off", [([], "None")]),
    pytest.param(
        "pybricks.pupdevices", "Light", "on", [(["brightness: Number=100"], "None")]
    ),
    pytest.param("pybricks.pupdevices", "Light", "off", [([], "None")]),
    pytest.param(
        "pybricks.pupdevices",
        "Remote",
        "name",
        [(["name: str"], "None"), ([], "str")],
    ),
    pytest.param(
        "pybricks.pupdevices", "Remote", "light.on", [(["color: Color"], "None")]
    ),
    pytest.param("pybricks.pupdevices", "Remote", "light.off", [([], "None")]),
    pytest.param(
        "pybricks.pupdevices",
        "Remote",
        "buttons.pressed",
        [([], "Collection[Button]")],
    ),
    pytest.param("pybricks.tools", "StopWatch", "time", [([], "int")]),
    pytest.param("pybricks.tools", "StopWatch", "pause", [([], "None")]),
    pytest.param("pybricks.tools", "StopWatch", "resume", [([], "None")]),
    pytest.param("pybricks.tools", "StopWatch", "reset", [([], "None")]),
    pytest.param(
        "pybricks.robotics",
        "DriveBase",
        "straight",
        [(["distance: Number", "then: Stop=Stop.HOLD", "wait: bool=True"], "None")],
    ),
    pytest.param(
        "pybricks.robotics",
        "DriveBase",
        "turn",
        [(["angle: Number", "then: Stop=Stop.HOLD", "wait: bool=True"], "None")],
    ),
    pytest.param(
        "pybricks.robotics",
        "DriveBase",
        "curve",
        [
            (
                [
                    "radius: Number",
                    "angle: Number",
                    "then: Stop=Stop.HOLD",
                    "wait: bool=True",
                ],
                "None",
            )
        ],
    ),
    pytest.param(
        "pybricks.robotics",
        "DriveBase",
        "settings",
        [
            (
                [
                    "straight_speed: Optional[Number]=None",
                    "straight_acceleration: Optional[Number]=None",
                    "turn_rate: Optional[Number]=None",
                    "turn_acceleration: Optional[Number]=None",
                ],
                "None",
            ),
            ([], "Tuple[int, int, int, int]"),
        ],
    ),
    pytest.param(
        "pybricks.robotics",
        "DriveBase",
        "drive",
        [(["speed: Number", "turn_rate: Number"], "None")],
    ),
    pytest.param("pybricks.robotics", "DriveBase", "stop", [([], "None")]),
    pytest.param("pybricks.robotics", "DriveBase", "distance", [([], "int")]),
    pytest.param("pybricks.robotics", "DriveBase", "angle", [([], "int")]),
    pytest.param(
        "pybricks.robotics", "DriveBase", "state", [([], "Tuple[int, int, int, int]")]
    ),
    pytest.param("pybricks.robotics", "DriveBase", "reset", [([], "None")]),
]


@pytest.mark.parametrize("module,type,method,signatures", METHOD_PARAMS)
def test_get_signature_for_methods(
    module: str, type: str, method: str, signatures: list[tuple[list[str], str]]
):
    help = _get_method_signature(module, type, method)

    # strip method now that code has been generated (may have leading subcomponent)
    method = method.split(".")[-1]

    assert help["activeSignature"] == 0
    assert help["activeParameter"] == 0
    assert help["signatures"]

    for sig, (params, returns) in zip_longest(help["signatures"], signatures):
        assert sig["label"] == f"{method}({', '.join(params)}) -> {returns}"
        assert sig["documentation"]["value"]
        # ensure signatures are stripped from doc comment
        assert not sig["documentation"]["value"].startswith(f"{method}(")

        for pi, p in zip_longest(sig["parameters"], params):
            assert pi["label"] == p
            assert pi["documentation"]["value"]
