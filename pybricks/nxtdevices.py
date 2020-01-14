"""Use LEGO® MINDSTORMS® NXT motors and sensors with the EV3 brick."""


class TouchSensor():
    """LEGO® MINDSTORMS® NXT Touch Sensor."""

    def __init__(self, port):
        """

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


class LightSensor():
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

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


class ColorSensor():
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    def __init__(self, port):
        """

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
        """Measure the reflection of a surface.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0 (no reflection) to
            100 (high reflection).

        """
        pass


class UltrasonicSensor():
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def distance(self):
        """Measure the distance between the sensor and an object using
        ultrasonic sound waves.

        Returns:
            :ref:`distance`: Distance.

        """
        pass
