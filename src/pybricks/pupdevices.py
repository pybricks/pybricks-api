# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Powered Up motor, sensors, and lights."""

from __future__ import annotations

from typing import TYPE_CHECKING, Collection, Optional, Union, overload

from . import _common
from .parameters import Button, Color, Direction

if TYPE_CHECKING:
    from ._common import (
        MaybeAwaitable,
        MaybeAwaitableBool,
        MaybeAwaitableFloat,
        MaybeAwaitableInt,
        MaybeAwaitableTuple,
    )
    from .parameters import Number, Port


class DCMotor(_common.DCMotor):
    """LEGO® Powered Up motor without rotation sensors."""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """


class Motor(_common.Motor):
    """LEGO® Powered Up motor with rotation sensors."""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle.
            gears (list):
                List of gears linked to the motor. The gear connected
                to the motor comes first and the gear connected to the output
                comes last.

                For example: ``[12, 36]`` represents a gear train with a
                12-tooth gear connected to the motor and a 36-tooth gear
                connected to the output. Use a list of lists for multiple
                gear trains, such as ``[[12, 36], [20, 16, 40]]``.

                When you specify a gear train, all motor commands and settings
                are automatically adjusted to account for the resulting gear
                ratio. The motor direction remains unchanged by this.
            reset_angle (bool):
                Choose ``True`` to reset the rotation sensor value to the
                absolute marker angle (between -180 and 179).
                Choose ``False`` to keep the
                current value, so your program knows where it left off last
                time.
            profile (Number, deg): Precision profile. This is the approximate
                position tolerance in degrees that is acceptable in your
                application. A lower value gives more precise but more erratic
                movement; a higher value gives less precise but smoother
                movement. If no value is given, a suitable profile for this
                motor type will be selected automatically (about 11 degrees).
        """

    def reset_angle(self, angle: Optional[Number] = None) -> None:
        """reset_angle(angle=None)

        Sets the accumulated rotation angle of the motor to a desired value.

        If this motor is also being used by a drive base, its distance and
        angle values will also be affected. You might want to
        use its :meth:`reset <pybricks.robotics.DriveBase.reset>`
        method instead.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
                                 Choose ``None`` to reset it to the absolute
                                 value of the motor.
        """


class Remote:
    """LEGO® Powered Up Bluetooth Remote Control."""

    light = _common.ExternalColorLight()
    buttons = _common.Keypad(
        (
            Button.LEFT_MINUS,
            Button.RIGHT_MINUS,
            Button.LEFT,
            Button.CENTER,
            Button.RIGHT,
            Button.LEFT_PLUS,
            Button.RIGHT_PLUS,
        )
    )
    address: Union[str, None]

    def __init__(self, name: Optional[str] = None, timeout: int = 10000):
        """Remote(name=None, timeout=10000)

        When you instantiate this class, the hub will search for a remote
        and connect automatically.

        The remote must be on and ready for a connection, as indicated by a
        white blinking light.

        Arguments:
            name (str): Bluetooth name of the remote. If no name is given,
                the hub connects to the first remote that it finds.
            timeout (Number, ms): How long to search for the remote.
        """

    @overload
    def name(self, name: str) -> None: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Sets or gets the Bluetooth name of the remote.

        Arguments:
            name (str): New Bluetooth name of the remote. If no name is given,
                this method returns the current name.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Disconnects the remote from the hub.
        """


class TiltSensor:
    """LEGO® Powered Up Tilt Sensor."""

    def __init__(self, port: Port):
        """TiltSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def tilt(self) -> MaybeAwaitableTuple[int, int]:
        """tilt() -> Tuple[int, int]: deg

        Measures the tilt relative to the horizontal plane.

        Returns:
            Tuple of pitch and roll angles.
        """


class ColorDistanceSensor(_common.CommonColorSensor):
    """LEGO® Powered Up Color and Distance Sensor."""

    light = _common.ExternalColorLight()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object
        using infrared light.

        Returns:
            Distance ranging from 0% (closest) to 100% (farthest).
        """


class PFMotor:
    """Control Power Functions motors with the infrared functionality of the
    :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`."""

    def __init__(
        self,
        sensor: ColorDistanceSensor,
        channel: int,
        color: Color,
        positive_direction: Direction = Direction.CLOCKWISE,
    ):
        """PFMotor(sensor, channel, color, positive_direction=Direction.CLOCKWISE)

        Arguments:
            sensor (ColorDistanceSensor):
                Sensor object.
            channel (int):
                Channel number of the receiver: ``1``, ``2``, ``3``, or ``4``.
            color (Color):
                Color marker on the receiver:
                :class:`Color.BLUE <.parameters.Color>` or
                :class:`Color.RED <.parameters.Color>`
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive duty cycle value.
        """

    def dc(self, duty: Number) -> MaybeAwaitable:
        """dc(duty)

        Rotates the motor at a given duty cycle (also known as "power").

        Arguments:
            duty (Number, %): The duty cycle (-100.0 to 100).
        """

    def stop(self) -> MaybeAwaitable:
        """stop()

        Stops the motor and lets it spin freely.

        The motor gradually stops due to friction.
        """

    def brake(self) -> MaybeAwaitable:
        """brake()

        Passively brakes the motor.

        The motor stops due to friction, plus the voltage that
        is generated while the motor is still moving.
        """


class ColorSensor(_common.AmbientColorSensor):
    """LEGO® SPIKE Color Sensor."""

    lights = _common.LightArray3()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """


class UltrasonicSensor:
    """LEGO® SPIKE Color Sensor."""

    lights = _common.LightArray4()

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: mm

        Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Returns:
            Measured distance. If no valid distance was measured,
            it returns 2000 mm.

        """

    def presence(self) -> MaybeAwaitableBool:
        """presence() -> bool

        Checks for the presence of other ultrasonic sensors by detecting
        ultrasonic sounds.

        Returns:
            ``True`` if ultrasonic sounds are detected, ``False`` if not.
        """


class ForceSensor:
    """LEGO® SPIKE Force Sensor."""

    def __init__(self, port: Port):
        """ForceSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def force(self) -> MaybeAwaitableFloat:
        """force() -> float: N

        Measures the force exerted on the sensor.

        Returns:
            Measured force (up to approximately 10.00 N).
        """

    def distance(self) -> MaybeAwaitableFloat:
        """distance() -> float: mm

        Measures by how much the sensor button has moved.

        Returns:
            Movement up to approximately 8.00 mm.
        """

    def pressed(self, force: Number = 3) -> MaybeAwaitableBool:
        """pressed(force=3) -> bool

        Checks if the sensor button is pressed.

        Arguments:
            force (Number, N): Minimum force to be considered pressed.

        Returns:
            ``True`` if the sensor is pressed, ``False`` if it is not.
        """

    def touched(self) -> MaybeAwaitableBool:
        """touched() -> bool

        Checks if the sensor is touched.

        This is similar to :meth:`pressed`, but it detects slight movements of
        the button even when the measured force is still considered zero.

        Returns:
            ``True`` if the sensor is touched or pressed, ``False``
            if it is not.
        """


class ColorLightMatrix:
    """
    LEGO® SPIKE 3x3 Color Light Matrix.
    """

    def __init__(self, port: Port):
        """ColorLightMatrix(port)

        Arguments:
            port (Port): Port to which the device is connected.

        """
        ...

    def on(self, color: Union[Color, Collection[Color]]) -> MaybeAwaitable:
        """on(colors)

        Turns the lights on.

        Arguments:
            colors (Color or list):
                If a single :class:`.Color` is given, then all 9 lights are set
                to that color. If a list of colors is given, then each light is
                set to that color.
        """
        ...

    def off(self) -> MaybeAwaitable:
        """off()

        Turns all lights off.
        """
        ...


class InfraredSensor:
    """LEGO® Powered Up Infrared Sensor."""

    def __init__(self, port: Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Measures the reflection of a surface using an infrared light.

        Returns:
            Measured reflection, ranging from 0% (no reflection) to
            100% (high reflection).
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object
        using infrared light.

        Returns:
            Distance ranging from 0% (closest) to 100% (farthest).
        """

    def count(self) -> MaybeAwaitableInt:
        """count() -> int

        Counts the number of objects that have passed by the sensor.

        Returns:
            Number of objects counted.
        """


class Light:
    """LEGO® Powered Up Light."""

    def __init__(self, port: Port):
        """Light(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def on(self, brightness: Number = 100) -> None:
        """on(brightness=100)

        Turns on the light at the specified brightness.

        Arguments:
            brightness (Number, %):
                Brightness of the light.
        """

    def off(self) -> None:
        """off()

        Turns off the light."""


# HACK: exclude from jedi
if TYPE_CHECKING:
    del Button
    del Color
    del Direction
    del MaybeAwaitable
    del MaybeAwaitableBool
    del MaybeAwaitableFloat
    del MaybeAwaitableInt
    del MaybeAwaitableTuple
    del Number
    del Port
