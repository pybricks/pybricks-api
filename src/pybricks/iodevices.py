# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Generic input/output devices."""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

from . import _common

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableBytes, MaybeAwaitableTuple
    from .parameters import Number, Port


class PUPDevice:
    """Powered Up motor or sensor."""

    def __init__(self, port: Port):
        """PUPDevice(port)

        Arguments:
            port (Port): Port to which the device is connected.
        """

    def info(self) -> dict:
        """info() -> dict

        Gets information about the device.

        For passive devices (such as DC motors or lights), returns a
        dictionary with only the ``id`` key.

        For UART devices, returns a dictionary with an ``id`` key and a
        ``modes`` key. The ``modes`` value is a tuple of tuples, one per
        mode, each containing the mode name, number of values, and data
        type.

        Returns:
            Dictionary with device information.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> tuple

        Reads values from a given mode.

        For passive touch sensors, this returns a single boolean value
        indicating whether the sensor is pressed, regardless of the
        ``mode`` argument.

        Raises an error for other passive devices such as DC motors and
        lights, which do not support reading.

        Arguments:
            mode (int): Device mode.

        Returns:
            Values read from the device.

        Raises:
            OSError: If the device is a passive device that does not
                support reading (e.g. a DC motor or light).
        """

    def write(self, mode: int, data: tuple) -> MaybeAwaitable:
        """write(mode, data)

        Writes values to the device. Only selected UART devices and modes
        support this.

        Arguments:
            mode (int): Device mode.
            data (tuple): Values to be written. The number of values and
                their types must match what the device expects for the
                given mode.

        Raises:
            OSError: If the device is a passive device that does not
                support writing.
            ValueError: If the mode is invalid, the mode is not writable,
                the number of values does not match, or a value is out of
                range for its data type.
        """

    def reset(self) -> None:
        """reset()

        Resets the UART device. After this, it should automatically synchronize
        and be ready for use after a few seconds. This is useful to forcefully
        re-trigger what such a sensor does when plugged in.

        Raises:
            OSError: If the device is a passive device that does not
                support reset.
        """


class LUMPDevice(PUPDevice):
    """Devices using the LEGO UART Messaging Protocol.

    See the equivalent :class:`PUPDevice() <pybricks.iodevices.PUPDevice>` for
    a description of available methods.

    On EV3, this class provides access to UART devices only. You can use other
    classes to interact with passive devices.
    """


class DCMotor(_common.DCMotor):
    """DC Motor for LEGO® MINDSTORMS EV3."""


class AnalogSensor:
    """Generic or custom analog sensor."""

    def __init__(self, port: Port, custom: bool = False):
        """AnalogSensor(port, custom=False)

        Arguments:
            port (Port): Port to which the sensor is connected.
            custom (bool): Set to ``True`` if you are using a custom analog
                sensor.

        Raises:
            OSError: If no standard LEGO analog sensor is
                detected on the port. Only applies if ``custom=False``.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Measures analog voltage.

        Returns:
            Analog voltage.
        """

    def resistance(self) -> int:
        """resistance() -> int: Ω

        Measures resistance.

        This value is only meaningful if the analog device is a passive load
        such as a resistor or thermistor. It is calculated assuming a 10 kΩ
        internal pull-up resistor forming a voltage divider.

        If the circuit is open (no load connected), the maximum integer value
        is returned.

        Returns:
            Resistance of the analog device, or the maximum integer value
            if the circuit is open.
        """

    def active(self) -> None:
        """active()

        Sets sensor to active mode. This sets pin 5 of the sensor
        port to `high`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light on.
        From then on, ``voltage()`` returns the raw reflected light value.
        """

    def passive(self) -> None:
        """passive()

        Sets sensor to passive mode. This sets pin 5 of the sensor
        port to `low`.

        This is used in some analog
        sensors to control a switch. For example, if you use the NXT Light
        Sensor as a custom analog sensor, this method will turn the light off.
        From then on, ``voltage()`` returns the raw ambient light value.
        """


class I2CDevice:
    """Generic or custom I2C device.

    Note: Use the ``power_pin`` option at your own risk. Applying power to the
    pins can damage your hub or device if you are not careful. When you use
    this option, you will be prompted to confirm that you understand the risks.
    """

    def __init__(
        self,
        port: Port,
        address: int,
        custom: bool = False,
        power_pin: int = 0,
        nxt_quirk: bool = False,
    ):
        """I2CDevice(port, address, custom=False, power_pin=0, nxt_quirk=False)

        Arguments:
            port (Port): Port to which the device is connected.
            address (int): I2C address of the client device. See
                :ref:`I2C Addresses <i2caddress>`.
            custom (bool): Set to ``True`` if you are using a custom I2C device.
            power_pin (int): Power requirements for the device. Use
                ``0`` (default) for no power on the pins. On NXT and EV3, use ``1``
                to apply battery power to pin 1. Other pins are not supported.
            nxt_quirk (bool): Set to ``True`` for older NXT I2C sensors that
                need slower compatibility timing to communicate reliably,
                such as the old NXT Ultrasonic Sensor.
        """

    @overload
    def read(self, reg: int | None = None, length: int = 1) -> MaybeAwaitableBytes: ...

    @overload
    def read(
        self, reg: int | None = None, length: int = 1, map: callable = ...
    ) -> MaybeAwaitable: ...

    def read(
        self, reg: int | None = None, length: int = 1, map=None
    ) -> MaybeAwaitableBytes:
        """read(reg=None, length=1) -> bytes
        read(reg=None, length=1, map=callable) -> Any

        Reads bytes starting at a given register.

        Arguments:
            reg (int): Register at which to begin reading: 0--255 or
                0x00--0xFF. Use ``None`` to read without writing a register
                address first.
            length (int): How many bytes to read.
            map (callable): Optional callable to convert the returned bytes.
                If given, it is called with the bytes as its argument and its
                return value is returned instead.

        Returns:
            Bytes returned from the device, or the return value of ``map``
            if a callable was provided.
        """

    def write(
        self, reg: int | None = None, data: bytes | None = None
    ) -> MaybeAwaitable:
        """write(reg=None, data=None)

        Writes bytes, optionally starting at a given register.

        Arguments:
            reg (int): Register at which to begin writing: 0--255 or
                0x00--0xFF. Use ``None`` to write without a register prefix.
            data (bytes): Bytes to be written. Use ``None`` to write nothing
                after the register.

        Raises:
            ValueError: If ``reg`` is given and ``data`` is more than 32 bytes.
                To write more data, omit the ``reg`` argument and include the
                register as the first byte of ``data``.
        """


class UARTDevice:
    """Generic UART device.

    Note: Use the ``power_pin`` option at your own risk. Applying power to the
    pins can damage your hub or device if you are not careful. When you use
    this option, you will be prompted to confirm that you understand the risks.
    """

    def __init__(
        self,
        port: Port,
        baudrate: int = 115200,
        timeout: int | None = None,
        power_pin: int = 0,
    ):
        """UARTDevice(port, baudrate=115200, timeout=None, power_pin=0)

        Arguments:
            port (Port): Port to which the device is connected. On Powered UP
                hubs, all ports are supported. On EV3, only the sensor ports
                are supported.
            baudrate (int): Baudrate of the UART device.
            timeout (Number, ms): How long to wait during ``read`` and
                ``write`` before giving up. If you choose ``None``, it will
                wait forever.
            power_pin (int): Power requirements for the device. Use ``0``
                (default) for no power on the pins. On Powered UP hubs, use
                ``1`` or ``2`` for pin 1 or 2, respectively. This will apply
                battery power to the pin, equivalent to powering a motor.
                On EV3, use ``1`` to apply battery power to pin 1, though only
                minimal current is available.

        Raises:
            ValueError: If ``timeout`` is 0 or negative.
        """

    def read(self, length: int = 1) -> MaybeAwaitableBytes:
        """read(length=1) -> bytes

        Reads a given number of bytes from the buffer.

        Your program will wait until the requested number of bytes are
        received. If this takes longer than ``timeout``, the ``ETIMEDOUT``
        exception is raised.

        Arguments:
            length (int): How many bytes to read. Must be at least 1.

        Returns:
            Bytes returned from the device.

        Raises:
            ValueError: If ``length`` is less than 1.
            OSError: If the read takes longer than ``timeout``.
        """

    def read_all(self) -> bytes:
        """read_all() -> bytes

        Reads all bytes currently in the buffer. Returns immediately without
        waiting, even if the buffer is empty.

        Returns:
            Bytes currently in the buffer, or an empty bytes object if there
            is nothing to read.
        """

    def write(self, data: bytes) -> MaybeAwaitable:
        """write(data)

        Writes bytes to the device.

        Arguments:
            data (bytes): Bytes to be written.

        Raises:
            TypeError: If ``data`` is not ``bytes``, ``bytearray``, or ``str``.
            OSError: If the write takes longer than ``timeout``.
        """

    def waiting(self) -> int:
        """waiting() -> int

        Gets how many bytes are still waiting to be read.

        Returns:
            Number of bytes in the buffer.
        """

    def set_baudrate(self, baudrate: int) -> None:
        """set_baudrate(baudrate)

        Changes the baud rate of the UART device.

        Arguments:
            baudrate (int): Not all values may be supported.

        Raises:
            ValueError: If ``baudrate`` is less than 1.
        """

    def wait_until(self, pattern: bytes) -> MaybeAwaitable:
        """wait_until(pattern)

        Waits until a specific byte sequence is received. Bytes that do not
        match the pattern are discarded.

        Arguments:
            pattern (bytes): Byte sequence to wait for. Must not be empty.

        Raises:
            ValueError: If ``pattern`` is empty.
            OSError: If this method is already in progress.
        """

    def clear(self) -> None:
        """clear()

        Empties the receive buffer."""


class LWP3Device:
    """
    Connects to a hub running official LEGO firmware using the
    `LEGO Wireless Protocol v3`_.

    .. _`LEGO Wireless Protocol v3`:
        https://lego.github.io/lego-ble-wireless-protocol-docs/
    """

    def __init__(
        self,
        hub_kind: int,
        name: str = None,
        timeout: int = 10000,
        pair: bool = False,
        num_notifications: int = 8,
        connect: bool = True,
    ):
        """LWP3Device(hub_kind, name=None, timeout=10000, pair=False, num_notifications=8, connect=True)

        Arguments:
            hub_kind (int):
                The `hub type identifier`_ of the hub to connect to.
            name (str):
                The name of the hub to connect to or ``None`` to connect to any
                hub.
            timeout (int):
                The time, in milliseconds, to wait for a connection before
                raising an exception.
            pair (bool): Whether to attempt pairing for a secure connection.
                This is required for some newer hubs.
            num_notifications (int): Number of incoming messages from the remote
                hub to store before discarding older messages.
            connect (bool): Choose ``False`` to skip connecting.
                ``connect()`` can be called later to connect.

        .. versionchanged:: 3.6

            Added ``pair`` parameter.

        .. versionchanged:: 3.7

            Added ``num_notifications`` parameter.

        .. _`hub type identifier`:
            https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#hub-type-ids
        """

    def connect(self) -> MaybeAwaitable:
        """connect()

        Connects to the device. Only needed if you disconnected or initialized
        with ``connect=False``.

        Raises:
            OSError: If the connection attempt fails or times out.
        """

    @overload
    def name(self, name: str) -> MaybeAwaitable: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Sets or gets the Bluetooth name of the device.

        Arguments:
            name (str): New Bluetooth name of the device. If no name is given,
                this method returns the current name.

        Raises:
            OSError: If the device is not connected.
        """

    def write(self, buf: bytes) -> MaybeAwaitable:
        """write(buf)

        Sends a message to the remote hub.

        Arguments:
            buf (bytes): The raw binary message to send. Maximum 20 bytes.

        Raises:
            ValueError: If the message exceeds 20 bytes.
            OSError: If the device is not connected or the write fails.
        """

    def read(self) -> bytes | None:
        """read() -> bytes | None

        Retrieves the oldest buffered message received from the remote hub.

        If all buffered messages have already been read, this returns ``None``.

        Returns:
            The oldest raw binary message or ``None`` if there are no more messages.

        .. versionchanged:: 3.7

            Now supports reading multiple buffered messages instead of blocking
            until one new message was received.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Disconnects the device.

        Raises:
            OSError: If disconnecting fails.
        """


class XboxController:
    """Use the Microsoft® Xbox® controller as a sensor in your projects to
    control them remotely.

    The hub will scan for the controller and connect to it. It will disconnect
    when the program ends.

    For tips on connectivity and pairing, see :ref:`below <xbox-controller-pairing>`.
    """

    buttons = _common.Keypad([])

    def __init__(
        self,
        joystick_deadzone: int = 10,
        name: str | None = None,
        timeout: int = 10000,
        connect: bool = True,
    ):
        """__init__(joystick_deadzone=10, name=None, timeout=10000, connect=True)

        Arguments:
            joystick_deadzone (Number, %): Joystick deadzone (0 to 100). Values
                below this threshold in both axes will be reported as 0 to
                prevent stick drift.
            name (str): The Bluetooth name of the Xbox controller to connect to,
                or ``None`` to connect to any available controller.
            timeout (Number, ms): How long to wait for a connection before
                giving up. Choose ``None`` to wait indefinitely.
            connect (bool): Choose ``False`` to skip connecting to the controller.
                ``connect()`` can be called later to connect.
        """

    def connect(self) -> MaybeAwaitable:
        """connect()

        Connects to the Xbox controller. Only needed if you disconnected or
        initialized the controller with ``connect=False``.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Disconnects the Xbox controller.
        """

    def name(self) -> str:
        """name() -> str

        Gets the Bluetooth name of the connected controller.

        Returns:
            Bluetooth name of the controller.

        Raises:
            OSError: If the controller is not connected.
        """

    def state(self) -> tuple:
        """state() -> tuple

        Gets all raw controller input values as a single tuple. This gives
        access to values not exposed by the other methods.

        The joystick axes (x, y, z, rz) are centered at 0. The trigger axes
        are raw 10-bit values (0-1023).

        Returns:
            Tuple of ``(x, y, z, rz, left_trigger, right_trigger, dpad,
            buttons, upload, profile, trigger_switches, paddles)``.

        Raises:
            OSError: If the controller is not connected.
        """

    def joystick_left(self) -> tuple[int, int]:
        """joystick_left() -> tuple

        Gets the left joystick position as percentages between -100%
        and 100%. The center position is (0, 0). A square deadzone is applied:
        if both axes are within the deadzone, both are reported as 0.

        Returns:
            Tuple of X (horizontal) and Y (vertical) position.

        Raises:
            OSError: If the controller is not connected.
        """

    def joystick_right(self) -> tuple[int, int]:
        """joystick_right() -> tuple

        Gets the right joystick position as percentages between -100%
        and 100%. The center position is (0, 0). A square deadzone is applied:
        if both axes are within the deadzone, both are reported as 0.

        Returns:
            Tuple of X (horizontal) and Y (vertical) position.

        Raises:
            OSError: If the controller is not connected.
        """

    def triggers(self) -> tuple[int, int]:
        """triggers() -> tuple

        Gets the left and right trigger positions as percentages between 0%
        and 100%.

        Returns:
            Tuple of left and right trigger positions.

        Raises:
            OSError: If the controller is not connected.
        """

    def dpad(self) -> int:
        """dpad() -> int

        Gets the direction-pad value. ``1`` is up, ``2`` is up-right, ``3``
        is right, ``4`` is down-right, ``5`` is down, ``6`` is down-left,
        ``7`` is left, ``8`` is up-left, and ``0`` is not pressed.

        This is essentially the same as reading the state of the
        ``Button.UP``, ``Button.RIGHT``, ``Button.DOWN``, and ``Button.LEFT``
        buttons, but this method conveniently returns a number that indicates
        a direction.

        Returns:
            Direction-pad position, indicating a direction.

        Raises:
            OSError: If the controller is not connected.
        """

    def profile(self) -> int:
        """profile() -> int

        Gets the current profile of the controller. Only available on the
        Xbox Elite Controller Series 2.

        Returns:
            Profile number.

        Raises:
            OSError: If the controller is not connected.
        """

    def rumble(
        self,
        power: Number | tuple[Number, Number, Number, Number] = 100,
        duration: int = 200,
        count: int = 1,
        delay: int = 100,
    ) -> MaybeAwaitable:
        """rumble(power=100, duration=200, count=1, delay=100)

        Makes the builtin actuators rumble, creating force feedback.

        If you give a single ``power`` value, the left and right main actuators
        will both rumble with that power while the trigger actuators stay off.
        For more fine-grained control, set ``power`` as a tuple of four values,
        which control the left main actuator, right main actuator, left trigger
        actuator, and the right trigger actuator, respectively. For example,
        ``power=(0, 0, 100, 0)`` makes the left trigger rumble at full power.

        The rumble runs in the background while your program continues. To
        make your program wait, just pause the program for a matching duration.
        For one rumble, this equals ``duration``. For multiple rumbles, this
        equals ``count * (duration + delay)``.

        This method does nothing if all actuator powers are zero, if
        ``duration`` is zero, or if ``count`` is less than 1.

        Arguments:
            power (Number, % or tuple): Rumble power. A single value applies
                to both main actuators (0-100%). A tuple applies individually
                to (left handle, right handle, left trigger, right trigger).
            duration (Number, ms): Duration of each rumble. Capped at 2500 ms.
            count (int): Number of rumbles (0-100).
            delay (Number, ms): Delay before each rumble. Only used if
                ``count > 1``. Capped at 2500 ms.
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del MaybeAwaitable
    del MaybeAwaitableBytes
    del MaybeAwaitableTuple
    del Number
    del Port
