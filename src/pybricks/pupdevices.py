# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® Powered Up motor, sensors, and lights."""

from typing import Optional, Union, overload, Tuple

from ._common import (
    Keypad as _Keypad,
    DCMotor as _DCMotor,
    ColorLight as _ColorLight,
    Motor as _Motor,
    LightArray as _LightArray,
    CommonColorSensor,
    AmbientColorSensor,
)

from .parameters import Button as _Button, Color, Direction, Port


class DCMotor(_DCMotor):
    pass


class Motor(_Motor):
    """Generic class to control motors with built-in rotation sensors."""

    def reset_angle(self, angle: Optional[int]) -> None:
        """reset_angle(angle=None)

        Sets the accumulated rotation angle of the motor to a desired value.

        If you don't specify an angle, the absolute angle
        will be used if your motor supports it.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
        """
        pass


class Remote:
    """LEGO® Powered Up Bluetooth Remote Control."""

    light = _ColorLight()
    buttons = _Keypad(
        (
            _Button.LEFT_MINUS,
            _Button.RIGHT_MINUS,
            _Button.LEFT,
            _Button.CENTER,
            _Button.RIGHT,
            _Button.LEFT_PLUS,
            _Button.RIGHT_PLUS,
        )
    )
    addresss: Union[str, None]

    def __init__(self, name: str = None, timeout: int = 10000):
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
        pass

    @overload
    def name(self, name: str) -> None:
        ...

    @overload
    def name(self) -> str:
        ...

    def name(self, *args):
        """name(name)
        name() -> str

        Sets or gets the Bluetooth name of the remote.

        Arguments:
            name (str): New Bluetooth name of the remote. If no name is given,
                this method returns the current name.
        """


class TiltSensor:
    """LEGO® Powered Up Tilt Sensor."""

    def __init__(self, port):
        """TiltSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def tilt(self) -> Tuple[int, int]:
        """tilt() -> Tuple[int, int]: deg

        Measures the tilt relative to the horizontal plane.

        Returns:
            Tuple of pitch and roll angles.
        """
        pass


class ColorDistanceSensor(CommonColorSensor):
    """LEGO® Powered Up Color and Distance Sensor."""

    light = _ColorLight()

    def distance(self) -> int:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object
        using infrared light.

        Returns:
            Distance ranging from 0% (closest) to 100% (farthest).
        """
        pass


class PFMotor(DCMotor):
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
        pass


class ColorSensor(AmbientColorSensor):
    """LEGO® SPIKE Color Sensor."""

    lights = _LightArray(3)


class UltrasonicSensor:
    """LEGO® SPIKE Color Sensor."""

    lights = _LightArray(3)

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def distance(self):
        """Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Returns:
            :ref:`distance`: Measured distance. If no valid distance was
            measured, it returns 2000 mm.

        """
        pass

    def presence(self):
        """Checks for the presence of other ultrasonic sensors by detecting
        ultrasonic sounds.

        Returns:
            bool: ``True`` if ultrasonic sounds are detected,
            ``False`` if not.
        """
        pass


class ForceSensor:
    """LEGO® SPIKE Force Sensor."""

    def __init__(self, port):
        """ForceSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def force(self):
        """Measures the force exerted on the sensor.

        Returns:
            :ref:`force`: Measured force (up to approximately 10.00 N).
        """

    def distance(self):
        """Measures by how much the sensor button has moved.

        Returns:
            :ref:`distance`: How much the sensor button has
            moved (up to approximately 8.00 mm).
        """

    def pressed(self, force=3):
        """Checks if the sensor button is pressed.

        Arguments:
            force (:ref:`force`): Minimum force to be considered pressed.

        Returns:
            bool: ``True`` if the sensor is pressed, ``False`` if it is not.
        """

    def touched(self):
        """Checks if the sensor is touched.

        This is similar to :meth:`pressed`, but it detects slight movements of
        the button even when the measured force is still considered zero.

        Returns:
            bool: ``True`` if the sensor is touched or pressed, ``False``
            if it is not.
        """

        pass


class ColorLightMatrix:
    """
    LEGO® SPIKE 3x3 Color Light Matrix.
    """

    def __init__(self, port):
        """ColorLightMatrix(port)

        Arguments:
            port (Port): Port to which the device is connected.

        """
        ...

    def on(self, colors):
        """
        Turns the lights on.

        Arguments:
            colors (Color or list):
                If a single :class:`.Color` is given, then all 9 lights are set
                to that color. If a list of colors is given, then each light is
                set to that color.
        """
        ...

    def off(self):
        """
        Turns all of the lights off.
        """
        ...


class InfraredSensor:
    """LEGO® Powered Up Infrared Sensor."""

    def __init__(self, port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def reflection(self):
        """Measures the reflection of a surface using an infrared light.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0.0 (no reflection) to
            100.0 (high reflection).
        """
        pass

    def distance(self):
        """Measures the relative distance between the sensor and an object
        using infrared light.

        Returns:
            :ref:`relativedistance`: Relative distance ranging from 0 (closest)
            to 100 (farthest).
        """
        pass

    def count(self):
        """Counts the number of objects that have passed by the sensor.

        Returns:
            int: Number of objects counted.
        """
        pass


class Light:
    """LEGO® Powered Up Light."""

    def __init__(self, port):
        """Light(port)

        Arguments:
            port (Port): Port to which the device is connected.

        """
        pass

    def on(self, brightness: int = 100) -> None:
        """on(brightness=100)

        Turns on the light at the specified brightness.

        Arguments:
            brightness (Number, %):
                Brightness of the light.
        """

    def off(self) -> None:
        """off()

        Turns off the light."""
        pass
