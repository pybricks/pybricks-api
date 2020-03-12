# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® MINDSTORMS® EV3 motors and sensors."""

from .parameters import Direction
from .builtins import Motor  # noqa E402


class TouchSensor:
    """LEGO® MINDSTORMS® EV3 Touch Sensor."""

    def __init__(self, port):
        """TouchSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def pressed(self):
        """Check if the sensor is pressed.

        Returns:
            bool: ``True`` if the sensor is pressed, ``False`` if it is
            not pressed.

        """
        pass


class ColorSensor:
    """LEGO® MINDSTORMS® EV3 Color Sensor."""

    def __init__(self, port):
        """ColorSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def color(self):
        """Measure the color of a surface.

        :returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``,
            ``Color.RED``, ``Color.WHITE``, ``Color.BROWN`` or ``None``.
        :rtype: :class:`Color <.parameters.Color>`, or ``None`` if no color is
                detected.

        """
        pass

    def ambient(self):
        """Measure the ambient light intensity.

        Returns:
            :ref:`percentage`: Ambient light intensity, ranging from 0 (dark)
            to 100 (bright).
        """
        pass

    def reflection(self):
        """Measure the reflection of a surface using a red light.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0 (no reflection) to
            100 (high reflection).

        """
        pass

    def rgb(self):
        """Measure the reflection of a surface using a red, green, and then a
        blue light.

        Returns:
            tuple of three :ref:`percentages <percentage>`: Reflection for red,
            green, and blue light, each ranging from 0.0 (no reflection) to
            100.0 (high reflection).
        """
        pass


class InfraredSensor:
    """LEGO® MINDSTORMS® EV3 Infrared Sensor and Beacon."""

    def __init__(self, port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def distance(self):
        """Measure the relative distance between the sensor and an object using
        infrared light.

        Returns:
            :ref:`relativedistance`: Relative distance ranging from 0 (closest)
            to 100 (farthest).

        """
        pass

    def beacon(self, channel):
        """Measure the relative distance and angle between the remote and the
        infrared sensor.

        Arguments:
            channel (int): Channel number of the remote.

        :returns: Tuple of relative distance (0 to 100) and approximate angle
                  (-75 to 75 degrees) between remote and infrared sensor.
        :rtype: (:ref:`relativedistance`, :ref:`angle`) or
                (``None``, ``None``) if no remote is detected.
        """
        pass

    def buttons(self, channel):
        """Check which buttons on the infrared remote are pressed.

        This method can detect up to two buttons at once. If you press
        more buttons, you may not get useful data.

        Arguments:
            channel (int): Channel number of the remote.

        :returns: List of pressed buttons on the remote on selected channel.
        :rtype: List of :class:`Button <.parameters.Button>`

        """
        pass

    def keypad(self):
        """Check which buttons on the infrared remote are pressed.

        This method can independently detect all 4 up/down buttons, but
        it cannot detect the beacon button.

        This method only works with the remote in channel 1.

        :returns: List of pressed buttons on the remote on selected channel.
        :rtype: List of :class:`Button <.parameters.Button>`

        """
        pass


class GyroSensor:
    """LEGO® MINDSTORMS® EV3 Gyro Sensor."""

    def __init__(self, port, positive_direction=Direction.CLOCKWISE):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
            positive_direction (Direction):
                Positive rotation direction when looking at the red dot on top
                of the sensor (*Default*: Direction.CLOCKWISE).

        """
        pass

    def speed(self):
        """Get the speed (angular velocity) of the sensor.

        Returns:
            :ref:`speed`: Sensor angular velocity.

        """
        pass

    def angle(self):
        """Get the accumulated angle of the sensor.

        Returns:
            :ref:`angle`: Rotation angle.

        """
        pass

    def reset_angle(self, angle):
        """Set the rotation angle of the sensor to a desired value.

        If you don't specify an angle, the absolute value will be used if
        available.

        Arguments:
            angle (:ref:`angle`): Value to which the angle should be reset.
        """
        pass

    def _calibrate(self):
        """Calibrate the sensor.

        This process sets the speed and angle to zero and ensures that the
        angle value does not drift.

        Make sure that the sensor does not move while calibrating.

        This process can take up to 15 seconds.
        """
        pass


class UltrasonicSensor:
    """LEGO® MINDSTORMS® EV3 Ultrasonic Sensor."""

    def __init__(self, port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def distance(self, silent=False):
        """Measure the distance between the sensor and an object using
        ultrasonic sound waves.

        Arguments:
            silent (bool): Choose ``True`` to turn the sensor off after
                           measuring the distance. Choose ``False`` to leave
                           the sensor on (*Default*). When you choose
                           ``silent=True``, the sensor does not
                           emit sounds waves except when taking the
                           measurement. This reduces interference with other
                           ultrasonic sensors, but turning the sensor off takes
                           approximately 300 ms each time.

        Returns:
            :ref:`distance`: Distance.

        """
        pass

    def presence(self):
        """Check for the presence of other ultrasonic sensors by detecting
        ultrasonic sounds.

        If the other ultrasonic sensor is operating in silent mode, you can
        only detect the presence of that sensor while it is taking a
        measurement.

        Returns:
            bool: ``True`` if ultrasonic sounds are detected,
            ``False`` if not.
        """
        pass
