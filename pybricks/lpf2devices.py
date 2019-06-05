"""LEGO® Power Functions 2.0 motor, sensors, and lights."""

from ._common import Motor as CommonMotor, ColorLight


class Motor(CommonMotor):
    """LEGO® Power Functions 2.0 motors:

        * ?/6181852: LEGO® BOOST Interactive Motor
        * TODO: Expand list with compatible devices
    """


class ColorDistanceSensor():
    """LEGO® Power Functions 2.0 Color and Distance Sensor (?/6182145)
    """

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
        :rtype: :class:`Color <parameters.Color>`, or ``None`` if no color is
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
