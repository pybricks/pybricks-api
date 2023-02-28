# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® MINDSTORMS® EV3 motors and sensors."""

from typing import Optional, Tuple, List

from . import _common
from .parameters import (
    Button as _Button,
    Color as _Color,
    Direction as _Direction,
    Port as _Port,
)


class Motor(_common.Motor):
    """LEGO® MINDSTORMS® EV3 Motor."""


class TouchSensor:
    """LEGO® MINDSTORMS® EV3 Touch Sensor."""

    def __init__(self, port: _Port):
        """TouchSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def pressed(self) -> bool:
        """pressed() -> bool

        Checks if the sensor is pressed.

        Returns:
            ``True`` if the sensor is pressed, ``False`` if it is
            not pressed.
        """


class ColorSensor:
    """LEGO® MINDSTORMS® EV3 Color Sensor."""

    def __init__(self, port: _Port):
        """ColorSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def color(self) -> Optional[_Color]:
        """color() -> Color

        Measures the color of a surface.

        Returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``,
            ``Color.YELLOW``, ``Color.RED``, ``Color.WHITE``, ``Color.BROWN``,
            or ``None`` if no color is detected.

        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark)
            to 100% (bright).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Measures the reflection of a surface using a red light.

        Returns:
            Reflection, ranging from 0% (no reflection) to
            100% (high reflection).

        """

    def rgb(self) -> Tuple[int, int, int]:
        """rgb() -> Tuple[int, int, int]

        Measures the reflection of a surface using a red, green, and then a
        blue light.

        Returns:
            Tuple of reflections for red, green, and blue light, each
            ranging from 0.0% (no reflection) to 100.0% (high reflection).
        """


class InfraredSensor:
    """LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon."""

    def __init__(self, port: _Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """

    def distance(self) -> int:
        """distance() -> int: %

        Measures the relative distance between the sensor and an object using
        infrared light.

        Returns:
            Relative distance ranging from 0% (closest)
            to 100% (farthest).

        """

    def beacon(self, channel: int) -> Tuple[Optional[int], Optional[int]]:
        """
        beacon(channel) -> Tuple[int, int]
        beacon(channel) -> Tuple[None, None]

        Measures the relative distance and angle between the remote and the
        infrared sensor.

        Arguments:
            channel (int): Channel number of the remote.

        Returns:
            Tuple of relative distance (0% to 100%) and approximate angle
            (-75 to 75 degrees) between remote and infrared sensor or
            a tuple of (``None``, ``None``) if no remote is detected.
        """

    def buttons(self, channel: int) -> List[_Button]:
        """buttons(channel) -> List[Button]

        Checks which buttons on the infrared remote are pressed.

        This method can detect up to two buttons at once. If you press
        more buttons, you'll still get just two buttons.

        Arguments:
            channel (int): Channel number of the remote.

        Returns:
            List of pressed buttons on the remote on the selected channel.

        """

    def keypad(self) -> List[_Button]:
        """keypad() -> List[Button]

        Checks which buttons on the infrared remote are pressed.

        This method can independently detect all 4 up/down buttons, but
        it cannot detect the beacon button.

        This method only works with the remote in channel 1.

        Returns:
            List of pressed buttons.
        """


class GyroSensor:
    """LEGO® MINDSTORMS® EV3 Gyro Sensor."""

    def __init__(self, port: _Port, direction: _Direction = _Direction.CLOCKWISE):
        """GyroSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
            direction (Direction):
                Positive rotation direction when looking at the red dot on top
                of the sensor.

        """

    def speed(self) -> int:
        """speed() -> int: deg/s

        Gets the speed (angular velocity) of the sensor.

        Returns:
            Angular velocity.

        """

    def angle(self) -> int:
        """angle() -> int: deg

        Gets the accumulated angle of the sensor.

        Returns:
            Rotation angle.

        """

    def reset_angle(self, angle: int) -> None:
        """reset_angle(angle)

        Sets the rotation angle of the sensor to a desired value.

        Arguments:
            angle (Number, deg): Value to which the angle should be reset.
        """


class UltrasonicSensor:
    """LEGO® MINDSTORMS® EV3 Ultrasonic Sensor."""

    def __init__(self, port: _Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """

    def distance(self, silent: bool = False) -> int:
        """distance(silent=False) -> int: mm

        Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Arguments:
            silent (bool): Choose ``True`` to turn the sensor off after
                           measuring the distance. This reduces interference
                           with other ultrasonic sensors. If you do
                           this too frequently, the sensor can freeze.
                           If this happens, unplug it and plug it back in.

        Returns:
            Measured distance.

        """

    def presence(self) -> bool:
        """presence() -> bool

        Checks for the presence of other ultrasonic sensors by detecting
        ultrasonic sounds.

        If the other ultrasonic sensor is operating in silent mode, you can
        only detect the presence of that sensor while it is taking a
        measurement.

        Returns:
            ``True`` if ultrasonic sounds are detected,
            ``False`` if not.
        """
