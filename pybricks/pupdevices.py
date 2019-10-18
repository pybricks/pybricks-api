"""LEGO® Powered Up motor, sensors, and lights."""

from .builtins import Motor as CommonMotor, ColorLight

from .builtins import KeyPad, Accelerometer
# The above abviously needs fixing (but not until after fixing merge conflict)


class Motor(CommonMotor):
    """LEGO® Powered Up motors"""

    def reset_angle(self, angle):
        """Reset the accumulated rotation angle of the motor.

        Arguments:
            angle (:ref:`angle`): Value to which the angle should be reset. If
                                  you don't specify an angle, the angle of the
                                  marker on the shaft will be used, if present.
        """
        pass


class RemoteControl():
    """LEGO® Powered Up Bluetooth Remote Control/Handset (6214560)"""

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
        self.buttons = KeyPad()
        self.light = ColorLight()


class TiltSensor(Accelerometer):
    """LEGO® Powered Up Tilt Sensor (45305/?)"""

    def __init__(self, port):
        """TiltSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass


class ColorDistanceSensor():
    """LEGO® Powered Up Color and Distance Sensor (?/6182145)"""

    def __init__(self, port):
        """ColorDistanceSensor(port)
        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        self.light = ColorLight()
        pass

    def color(self):
        """Measure the color of a surface.

        :returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``,
            ``Color.RED``, ``Color.WHITE``, or ``None``.
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
            :ref:`percentage`: Reflection, ranging from 0.0 (no reflection) to
            100.0 (high reflection).
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

    def distance(self):
        """Measure the relative distance between the sensor and an object using
        infrared light.

        Returns:
            :ref:`relativedistance`: Relative distance ranging from 0 (closest)
            to 100 (farthest).
        """
        pass
