# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Use LEGO® MINDSTORMS® NXT motors and sensors with the EV3 brick."""


from pybricks.iodevices import AnalogSensor
from pybricks.builtins import ColorLight


class TouchSensor:
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


class LightSensor:
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


class ColorSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    light = ColorLight()

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
            ``Color.RED``, ``Color.WHITE`` or ``None``.
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

    def rgb(self):
        """Measure the reflection of a surface using a red, green, and then a
        blue light.

        Returns:
            tuple of three :ref:`percentages <percentage>`: Reflection for red,
            green, and blue light, each ranging from 0.0 (no reflection) to
            100.0 (high reflection).
        """
        pass


class UltrasonicSensor:
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


class SoundSensor:
    """LEGO® MINDSTORMS® NXT Sound Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def intensity(self, audible_only=True):
        """Measure the ambient sound intensity (loudness).

        Arguments:
            audible_only (bool): Detect only audible sounds. This tries to
                filter out frequencies that cannot be heard by the
                human ear.

        Returns:
            :ref:`percentage`: Sound intensity.

        """
        pass


class TemperatureSensor:
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def temperature(self):
        """Measure the temperature.

        Returns:
            :ref:`temperature`: Measured temperature.

        """
        pass


class EnergyMeter:
    """LEGO® MINDSTORMS® Education NXT Energy Meter."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def storage(self):
        """Get the total available energy stored in the battery.

        Returns:
            :ref:`energy`: Remaining stored energy.

        """
        pass

    def input(self):
        """This measures the electrical signals at the input (bottom) side
        of the energy meter. It measures the voltage applied to it and the
        current passing through it. The product of these two values is power.
        This power value is the rate at which the stored energy increases. This
        power is supplied by an energy source such as the provided solar panel
        or an externally driven motor.

        Returns:
            (:ref:`voltage`, :ref:`current`, :ref:`power`): Voltage, current,
            and power measured at the input port.

        """
        pass

    def output(self):
        """This measures the electrical signals at the output (top) side
        of the energy meter. It measures the voltage applied to the external
        load and the current passing to it. The product of these two values
        is power. This power value is the rate at which the stored energy
        decreases. This power is consumed by the load, such as a light or a
        motor.

        Returns:
            (:ref:`voltage`, :ref:`current`, :ref:`power`): Voltage, current,
            and power measured at the output port.

        """
        pass


class VernierAdapter(AnalogSensor):
    """LEGO® MINDSTORMS® Education NXT/EV3 Adapter for Vernier Sensors."""

    def __init__(self, port, conversion=None):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
            conversion (callable): Function of the format :meth:`.conversion`.
                This function is used to convert the raw analog voltage to the
                sensor-specific output value. Each Vernier Sensor has its
                own conversion function. The example given below demonstrates
                the conversion for the Surface Temperature Sensor.
        """
        pass

    def voltage(self):
        """Measure the raw analog sensor voltage.

        Returns:
            :ref:`voltage`: Analog voltage.
        """
        pass

    def conversion(self, voltage):
        """User-supplied function that converts the raw voltage (mV) to a
        sensor value.

        If you did not provide a ``conversion`` function earlier, no conversion
        will be applied.

        Arguments:
            voltage (:ref:`voltage`): Analog sensor voltage

        :returns: Converted sensor value.
        :rtype: float
        """
        pass

    def value(self):
        """This method measures the sensor :meth:`.voltage` and then
        applies your :meth:`.conversion` to give you the sensor value.

        :returns: Converted sensor value.
        :rtype: float
        """
        pass
