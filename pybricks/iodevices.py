# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Generic input/output devices."""


class PUPDevice:
    """Powered Up motor or sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the device is connected.
        """
        pass

    def info(self):
        """Returns information about the device.

        Returns:
            ``dict``: Dictionary with information, such as the device ``id``.
        """
        pass

    def read(self, mode):
        """Reads values from a given mode.

        Arguments:
            mode (``int``): Device mode.

        Returns:
            ``tuple``: Values read from the sensor.
        """
        pass

    def write(self, mode, data):
        """Writes values to the sensor. Only selected sensors and modes support
        this.

        Arguments:
            mode (``int``): Device mode.
            data (``tuple``): Values to be written.
        """
        pass


class LUMPDevice:
    """Devices using the LEGO UART Messaging Protocol."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the device is connected.
        """
        pass

    def read(self, mode):
        """Reads values from a given mode.

        Arguments:
            mode (``int``): Device mode.

        Returns:
            ``tuple``: Values read from the sensor.
        """
        pass


class Ev3devSensor:
    """Read values of an ev3dev-compatible sensor."""

    sensor_index = 0
    """Index of the ev3dev sysfs `lego-sensor`_ class."""

    port_index = 0
    """Index of the ev3dev sysfs `lego-port`_ class."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the device is connected.
        """
        pass

    def read(self, mode):
        """Reads values at a given mode.

        Arguments:
            mode (``str``): `Mode name`_.

        Returns:
            ``tuple``: Values read from the sensor.
        """
        pass


class AnalogSensor:
    """Generic or custom analog sensor."""

    def __init__(self, port):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
        """
        pass

    def voltage(self):
        """Measures analog voltage.

        Returns:
            :ref:`voltage`: Analog voltage.
        """
        pass

    def resistance(self):
        """Measures resistance.

        This value is only meaningful if the analog device is a passive load
        such as a resistor or thermistor.

        Returns:
            :ref:`resistance: Ω <voltage>`: Resistance of the analog device.
        """
        pass

    def active(self):
        """Sets sensor to active mode. This sets pin 5 of the sensor
        port to `high`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light on.
        From then on, ``voltage()`` returns the raw reflected light value.
        """
        pass

    def passive(self):
        """Sets sensor to passive mode. This sets pin 5 of the sensor
        port to `low`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light off.
        From then on, ``voltage()`` returns the raw ambient light value.
        """
        pass


class I2CDevice:
    """Generic or custom I2C device."""

    def __init__(self, port, address):
        """

        Arguments:
            port (Port): Port to which the device is connected.
            address(int): I2C address of the client device. See
                :ref:`I2C Addresses <i2caddress>`.
        """
        pass

    def read(self, reg, length=1):
        """Reads bytes, starting at a given register.

        Arguments:
            reg (``int``): Register at which to begin
                reading: 0--255 or 0x00--0xFF.
            length (``int``): How many bytes to read.

        Returns:
            ``bytes``: Bytes returned from the device.
        """
        pass

    def write(self, reg, data=None):
        """Writes bytes, starting at a given register.

        Arguments:
            reg (``int``): Register at which to begin
                writing: 0--255 or 0x00--0xFF.
            data (``bytes``): Bytes to be written.
        """
        pass


class UARTDevice:
    """Generic UART device."""

    def __init__(self, port, baudrate, timeout=None):
        """

        Arguments:
            port (Port): Port to which the device is connected.
            baudrate (int): Baudrate of the UART device.
            timeout (:ref:`time`): How long to wait
                during ``read`` before giving up. If you choose ``None``,
                it will wait forever.
        """
        pass

    def read(self, length=1):
        """Reads a given number of bytes from the buffer.

        Your program will wait until the requested number of bytes are
        received. If this takes longer than ``timeout``, the ``ETIMEDOUT``
        exception is raised.

        Arguments:
            length (``int``): How many bytes to read.

        Returns:
            ``bytes``: Bytes returned from the device.
        """
        pass

    def read_all(self):
        """Reads all bytes from the buffer.

        Returns:
            ``bytes``: Bytes returned from the device.
        """
        pass

    def write(self, data):
        """Writes bytes.

        Arguments:
            data (``bytes``): Bytes to be written.
        """
        pass

    def waiting(self):
        """Gets how many bytes are still waiting to be read.

        Returns:
            ``int``: Number of bytes in the buffer.
        """
        pass

    def clear(self):
        """Empties the buffer."""
        pass
