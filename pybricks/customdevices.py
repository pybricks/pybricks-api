"""Custom motors and sensors."""


class AnalogSensor():
    """Generic or custom analog sensor."""

    def __init__(self, port, check_type=True):
        """

        Arguments:
            port (Port): Port to which the sensor is connected.
            verify_type(bool): Verify that the sensor is detected as an analog
                sensor (*Default*: ``True``).

                If you choose ``verify_type=False``, the EV3 will treat it as
                an analog sensor even if no such sensor is detected. This is
                useful if you have a (custom) analog sensor that is not
                detected automatically.
        """
        pass

    def voltage(self):
        """Measured analog voltage.

        Returns:
            :ref:`voltage`: Analog voltage.
        """
        pass

    def resistance(self):
        """Measured resistance.

        This value is only meaningful if the analog device is a passive load
        such as a resistor or thermistor.

        Returns:
            :ref:`resistance: Ω <voltage>`: Resistance of the analog device.
        """
        pass

    def active(self):
        """Set sensor to active mode. This sets pin 5 of the sensor
        port to `high`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light on.
        From then on, ``voltage()`` returns the raw reflected light value.
        """
        pass

    def passive(self):
        """Set sensor to passive mode. This sets pin 5 of the sensor
        port to `low`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light off.
        From then on, ``voltage()`` returns the raw ambient light value.
        """
        pass


class I2CDevice():
    """Generic or custom I2C device."""

    def __init__(self, port, address):
        """

        Arguments:
            port (Port): Port to which the device is connected.
            address(int): I2C address of the client device. See
                :ref:`I2C Addresses <i2caddress>`.
        """
        pass

    def read(self, reg, length):
        """Read bytes, starting at a given register.

        Arguments:
            reg (``int``): Register at which to begin
                reading: 0--255 or 0x00--0xFF.
            length (``int``): How many bytes to read.

        Returns:
            ``bytes``: Bytes returned from the device.
        """
        pass

    def write(self, reg, data):
        """Write bytes, starting at a given register.

        Arguments:
            reg (``int``): Register at which to begin
                writing: 0--255 or 0x00--0xFF.
            data (``bytes``): Bytes to be written.
        """
        pass


class UARTDevice():
    """Generic UART device."""

    def __init__(self, port, baudrate, timeout=None):
        """

        Arguments:
            port (Port): Port to which the device is connected.
            baudrate (int): Baudrate of the UART device.
            timeout (:ref:`time`): How long to wait
                during :meth:`.read` before giving up. If you choose ``None``,
                it will wait forever. (*Default*: ``None``)
        """
        pass

    def read(self, length):
        """Read a given number of bytes from the buffer.

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
        """Read all bytes from the buffer.

        Returns:
            ``bytes``: Bytes returned from the device.
        """
        pass

    def write(self, data):
        """Write bytes.

        Arguments:
            data (``bytes``): Bytes to be written.
        """
        pass

    def waiting(self):
        """How many bytes are still waiting to be read.

        Returns:
            ``int``: Number of bytes in the buffer.
        """
        pass

    def clear(self):
        """Empty the buffer."""
        pass
