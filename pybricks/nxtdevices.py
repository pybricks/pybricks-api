# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Use LEGO® MINDSTORMS® NXT motors and sensors with the EV3 brick."""


from .iodevices import AnalogSensor as _AnalogSensor
from ._common import ColorLight as _ColorLight


class TouchSensor:
    """LEGO® MINDSTORMS® NXT Touch Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def pressed(self):
        """Checks if the sensor is pressed.

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
        """Measures the ambient light intensity.

        Returns:
            :ref:`percentage`: Ambient light intensity, ranging from 0 (dark)
            to 100 (bright).
        """
        pass

    def reflection(self):
        """Measures the reflection of a surface using a red light.

        Returns:
            :ref:`percentage`: Reflection, ranging from 0 (no reflection) to
            100 (high reflection).

        """
        pass


class ColorSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    light = _ColorLight()

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def color(self):
        """Measures the color of a surface.

        :returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``, ``Color.YELLOW``,
            ``Color.RED``, ``Color.WHITE`` or ``Color.NONE``.
        :rtype: :class:`Color <.parameters.Color>`

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
            :ref:`percentage`: Reflection, ranging from 0 (no reflection) to
            100 (high reflection).

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


class UltrasonicSensor:
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

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
        """Measures the ambient sound intensity (loudness).

        Arguments:
            audible_only (bool): Detect only audible sounds. This tries to
                filter out frequencies that cannot be heard by the
                human ear.

        Returns:
            :ref:`percentage`: Sound intensity.

        """
        pass


class TemperatureSensor:
    """LEGO® MINDSTORMS® NXT Temperature Sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.

        """
        pass

    def temperature(self):
        """Measures the temperature.

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
        """Gets the total available energy stored in the battery.

        Returns:
            :ref:`energy`: Remaining stored energy.

        """
        pass

    def input(self):
        """Measures the electrical signals at the input (bottom) side
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
        """Measures the electrical signals at the output (top) side
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


class VernierAdapter(_AnalogSensor):
    """LEGO® MINDSTORMS® Education NXT/EV3 Adapter for Vernier Sensors."""

    def __init__(self, port, conversion=None):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
            conversion (callable): Function of the format ``conversion``.
                This function is used to convert the raw analog voltage to the
                sensor-specific output value. Each Vernier Sensor has its
                own conversion function. The example given below demonstrates
                the conversion for the Surface Temperature Sensor.
        """
        pass

    def voltage(self):
        """Measures the raw analog sensor voltage.

        Returns:
            :ref:`voltage`: Analog voltage.
        """
        pass

    def conversion(self, voltage):
        """Converts the raw voltage (mV) to a sensor value.

        If you did not provide a ``conversion`` function earlier, no conversion
        will be applied.

        Arguments:
            voltage (:ref:`voltage`): Analog sensor voltage

        :returns: Converted sensor value.
        :rtype: float
        """
        pass

    def value(self):
        """Measures the sensor :meth:`.voltage` and then
        applies your :meth:`.conversion` to give you the sensor value.

        :returns: Converted sensor value.
        :rtype: float
        """
        pass
