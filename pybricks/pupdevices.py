# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Powered Up motor, sensors, and lights."""

from ._common import (KeyPad as _KeyPad, DCMotor as _DCMotor,
                      ColorLight as _ColorLight, Motor as _Motor,
                      LightArray as _LightArray, Light as _Light)

from .parameters import Direction as _Direction


class Motor(_Motor):
    """Generic class to control motors with built-in rotation sensors."""

    def reset_angle(self, angle=None):
        """Sets the accumulated rotation angle of the motor to a desired value.

        If you don't specify an angle, the absolute angle
        will be used if your motor supports it.

        Arguments:
            angle (:ref:`angle`): Value to which the angle should be reset.
        """
        pass


class RemoteControl:
    """LEGO® Powered Up Bluetooth Remote Control/Handset."""

    light = _ColorLight()
    buttons = _KeyPad()

    def __init__(self, device=None, timeout=10000):
        """Connect the handset to the hub.

        Arguments:
            device (str): Bluetooth address of the handset (? TODO ?).
                 If you do not specify a device identifier, the hub will
                 attempt to pair with any handset that is currently in
                 advertising mode.
            timeout (:ref:`time`): The amount of time before giving up
                 searching.
        """
        pass


class TiltSensor:
    """LEGO® Powered Up Tilt Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def tilt(self):
        """Measures the tilt relative to the horizontal plane.

        Returns:
            (:ref:`angle`, :ref:`angle`): Tuple of pitch and roll angles.
        """
        pass


class ColorDistanceSensor:
    """LEGO® Powered Up Color and Distance Sensor."""

    light = _ColorLight()

    def __init__(self, port):
        """ColorDistanceSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def color(self):
        """Scans the color of a surface.

        :returns:
            Detected color.
        :rtype: :class:`Color <.parameters.Color>`, or ``None`` if no color is
                detected.
        """
        pass

    def ambient(self):
        """Measures the ambient light intensity.

        Returns:
            :ref:`percentage`: Ambient light intensity, ranging from 0 (dark)
            to 100 (bright).
        """
        pass

    def reflection(self):
        """Measures the reflection of a surface.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0.0 (no reflection) to
            100.0 (high reflection).
        """
        pass

    def color_map(self, hues, saturation, values):
        """Configures how :meth:`.color` selects a
        :class:`Color <.parameters.Color>` based on a :meth:`.hsv` measurement.

        Specify only colors that you wish to detect in your application.
        This way, measurements are
        rounded to the nearest expected color, and other colors are ignored.

        If you give no arguments, the current settings will be returned as a
        tuple.

        Arguments:
            hues (dict): A dictionary that
                maps :class:`Color <.parameters.Color>` to hues. When the
                saturation is high, :meth:`.color` will return one of these
                colors, whichever has the nearest hue.
            saturation (:ref:`percentage`): Minimum saturation of a proper
                color.
            values (:ref:`percentage`): A dictionary that
                maps ``Color.WHITE``, ``Color.GRAY``, ``Color.BLACK`` and
                ``None`` to brightness values. When the saturation is
                low, :meth:`.color` will return one of these colors, whichever
                has the nearest value.
        """
        pass

    def hsv(self):
        """Scans the hue, saturation and brightness value of a surface.

        :returns: Tuple with the hue, saturation, and value
            (brightness) of the color.
        :rtype: (:ref:`hue`, :ref:`percentage`, :ref:`percentage`)

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


class PFMotor(_DCMotor):
    """Control Power Functions motors with the infrared functionality of the
    :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`."""

    def __init__(self,
                 sensor,
                 channel,
                 color,
                 positive_direction=_Direction.CLOCKWISE):
        """

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


class ColorSensor:
    """LEGO® SPIKE Color Sensor."""

    lights = _LightArray(3)

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def color(self, surface=True):
        """Scans the color of a surface or an external light source.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        :returns:
            Detected color.
        :rtype: :class:`Color <.parameters.Color>`, or ``None`` if no color is
                detected.
        """
        pass

    def color_map(self, hues, saturation, values):
        """Configures how :meth:`.color` selects a
        :class:`Color <.parameters.Color>` based on a :meth:`.hsv` measurement.

        Specify only colors that you wish to detect in your application.
        This way, measurements are
        rounded to the nearest expected color, and other colors are ignored.

        If you give no arguments, the current settings will be returned as a
        tuple.

        Arguments:
            hues (dict): A dictionary that
                maps :class:`Color <.parameters.Color>` to hues. When the
                saturation is high, :meth:`.color` will return one of these
                colors, whichever has the nearest hue.
            saturation (:ref:`percentage`): Minimum saturation of a proper
                color.
            values (:ref:`percentage`): A dictionary that
                maps ``Color.WHITE``, ``Color.GRAY``, ``Color.BLACK`` and
                ``None`` to brightness values. When the saturation is
                low, :meth:`.color` will return one of these colors, whichever
                has the nearest value.
        """
        pass

    def hsv(self, surface=True):
        """Scans the hue, saturation and brightness value of a
        surface or an external light source.

        Arguments:
            surface (bool): Choose ``true`` to scan the color of objects
                and surfaces. Choose ``false`` to scan the color of
                screens and other external light sources.

        :returns: Tuple with the hue, saturation, and value
            (brightness) of the color.
        :rtype: (:ref:`hue`, :ref:`percentage`, :ref:`percentage`)

        """
        pass

    def ambient(self):
        """Measures the ambient light intensity.

        Returns:
            :ref:`percentage`: Ambient light intensity, ranging from 0 (dark)
            to 100 (bright).
        """
        pass

    def reflection(self):
        """Measures the reflection of a surface.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0.0 (no reflection) to
            100.0 (high reflection).
        """
        pass


class UltrasonicSensor:
    """LEGO® SPIKE Color Sensor."""

    lights = _LightArray(3)

    def __init__(self, port):
        """

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
        """

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


class InfraredSensor:
    """LEGO® Powered Up Infrared Sensor."""

    def __init__(self, port):
        """

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


class Light(_Light):
    """LEGO® Powered Up Light."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the device is connected.

        """
        pass
