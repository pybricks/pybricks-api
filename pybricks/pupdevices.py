# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""LEGO® Powered Up motor, sensors, and lights."""

from ._common import (KeyPad as _KeyPad, Accelerometer as _Accelerometer,
                      ColorLight as _ColorLight, Motor as _Motor)


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


class TiltSensor(_Accelerometer):
    """LEGO® Powered Up Tilt Sensor."""

    def __init__(self, port):
        """TiltSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
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
        """Measures the color of a surface.

        :returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``,
            ``Color.RED``, ``Color.WHITE``, or ``None``.
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
        """Measures the reflection of a surface using a red light.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0.0 (no reflection) to
            100.0 (high reflection).
        """
        pass

    def rgb(self):
        """Measures the reflection of a surface using a red, green, and then a
        blue light.

        :returns: Tuple of reflections for red, green, and blue light, each
                  ranging from 0.0 (no reflection) to 100.0 (high reflection).
        :rtype: (:ref:`percentage`, :ref:`percentage`, :ref:`percentage`)
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

    def remote(self, channel, button_1=None, button_2=None):
        """Makes the sensor act like a Power Functions 1.0 IR remote.

        Choose a channel and up to two buttons to "press". The infrared
        receiver behaves just as if responding to the real remote.

        The sensor keeps sending the signal (as if you keep pressing the
        buttons). It keeps going until you call this method again with
        different buttons or no buttons at all.

        Arguments:
            channel (int): Channel number of the remote.
            button_1 (Button): Button of the Power Functions 1.0 IR remote.
                               Choose ``None`` if you don't want to press
                               any button.
            button_2 (Button): Button of the Power Functions 1.0 IR remote.
                               Choose ``None`` if you don't want to press
                               any button.
        """
