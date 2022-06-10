# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Use LEGO® MINDSTORMS® NXT motors and sensors with the EV3 brick."""


from .parameters import Port

from ._common import ColorLight, CommonColorSensor
from .iodevices import AnalogSensor


from typing import Callable, Optional, Tuple


class TouchSensor:
    """LEGO® MINDSTORMS® NXT Touch Sensor."""

    def __init__(self, port: Port):
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


class LightSensor:
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    def __init__(self, port: Port):
        """LightSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0% (dark) to 100% (bright).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Measures the reflection of a surface using a red light.

        Returns:
            Reflection, ranging from 0% (no reflection) to 100% (high
            reflection).
        """


class ColorSensor(CommonColorSensor):
    """LEGO® MINDSTORMS® NXT Color Sensor."""

    light = ColorLight()

    def rgb(self) -> Tuple[int, int, int]:
        """Measures the reflection of a surface using a red, green, and then a
        blue light.

        Returns:
            Tuple of reflections for red, green, and blue light, each
            ranging from 0.0% (no reflection) to 100.0% (high reflection).
        """


class UltrasonicSensor:
    """LEGO® MINDSTORMS® NXT Ultrasonic Sensor."""

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Measures the distance between the sensor and an object using
        ultrasonic sound waves.

        Returns:
            Measured distance.
        """


class SoundSensor:
    """LEGO® MINDSTORMS® NXT Sound Sensor."""

    def __init__(self, port: Port):
        """SoundSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def intensity(self, audible_only: bool = True) -> int:
        """intensity(audible_only=True) -> int: %

        Measures the ambient sound intensity (loudness).

        Arguments:
            audible_only (bool): Detect only audible sounds. This tries to
                filter out frequencies that cannot be heard by the
                human ear.

        Returns:
            Sound intensity.
        """


class TemperatureSensor:
    """LEGO® MINDSTORMS® NXT Temperature Sensor."""

    def __init__(self, port: Port):
        """TemperatureSensor(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def temperature(self) -> int:
        """temperature() -> float: °C

        Measures the temperature.

        Returns:
            Measured temperature.
        """


class EnergyMeter:
    """LEGO® MINDSTORMS® Education NXT Energy Meter."""

    def __init__(self, port: Port):
        """EnergyMeter(port)

        Arguments:
            port (Port): Port to which the sensor is connected.
        """

    def storage(self) -> int:
        """storage() -> int: J

        Gets the total available energy stored in the battery.

        Returns:
            Remaining stored energy.
        """

    def input(self) -> Tuple[int, int, int]:
        """input() -> Tuple[int, int, int]

        Measures the electrical signals at the input (bottom) side
        of the energy meter. It measures the voltage applied to it and the
        current passing through it. The product of these two values is power.
        This power value is the rate at which the stored energy increases. This
        power is supplied by an energy source such as the provided solar panel
        or an externally driven motor.

        Returns:
            Voltage (mV), current (mA), and power (mW) measured at the input
            port.
        """

    def output(self) -> Tuple[int, int, int]:
        """output() -> Tuple[int, int, int]

        Measures the electrical signals at the output (top) side
        of the energy meter. It measures the voltage applied to the external
        load and the current passing to it. The product of these two values
        is power. This power value is the rate at which the stored energy
        decreases. This power is consumed by the load, such as a light or a
        motor.

        Returns:
            Voltage (mV), current (mA), and power (mW) measured at the output
            port.
        """


class VernierAdapter(AnalogSensor):
    """LEGO® MINDSTORMS® Education NXT/EV3 Adapter for Vernier Sensors."""

    def __init__(self, port: Port, conversion: Optional[Callable[[int], float]] = None):
        """VernierAdapter(port, conversion=None)

        Arguments:
            port (Port): Port to which the sensor is connected.
            conversion (callable): Function of the format :meth:`.conversion`.
                This function is used to convert the raw analog voltage to the
                sensor-specific output value. Each Vernier Sensor has its
                own conversion function. The example given below demonstrates
                the conversion for the Surface Temperature Sensor.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Measures the raw analog sensor voltage.

        Returns:
            Analog voltage.
        """

    def conversion(self, voltage: int) -> float:
        """conversion(voltage) -> float

        Converts the raw voltage (mV) to a sensor value.

        If you did not provide a :meth:`.conversion` function earlier, no
        conversion will be applied.

        Arguments:
            voltage (Number, mV): Analog sensor voltage

        Returns:
            Converted sensor value.
        """

    def value(self) -> float:
        """value() -> float

        Measures the sensor :meth:`.voltage` and then
        applies your :meth:`.conversion` to give you the sensor value.

        Returns:
            Converted sensor value.
        """
