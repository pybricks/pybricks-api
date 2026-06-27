# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2026 The Pybricks Authors

"""
Classes to send and receive messages from another device.
"""

from __future__ import annotations


from typing import (
    abstractmethod,
    Callable,
    Generic,
    Iterable,
    List,
    Optional,
    overload,
    Sequence,
    Tuple,
    TYPE_CHECKING,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    from ._common import (
        MaybeAwaitable,
    )

T = TypeVar("T")


class BLERadio:
    """
    Send and receive messages without a connection using Bluetooth Low Energy.

    .. versionadded:: 4.0

        This used to be part of each hub class.
    """

    def __init__(
        self,
        broadcast_channel: Optional[int] = None,
        observe_channels: Sequence[int] = [],
    ):
        """BLERadio(broadcast_channel=None, observe_channels=[])

        Arguments:
            broadcast_channel:
                Channel number (0 to 255) used to broadcast data.
                Choose ``None`` when not using broadcasting.
            observe_channels:
                A list of channels to listen to when ``hub.ble.observe()`` is
                called. Listening to more channels requires more memory.
                Default is an empty list (no channels).
        """

    @overload
    def broadcast(self, data: None) -> MaybeAwaitable: ...

    @overload
    def broadcast(
        self, data: Iterable[Union[bool, int, float, str, bytes]]
    ) -> MaybeAwaitable: ...

    @overload
    def broadcast(
        self, data: Union[bool, int, float, str, bytes]
    ) -> MaybeAwaitable: ...

    def broadcast(self, data: object) -> MaybeAwaitable:
        """broadcast(data)

        Starts broadcasting the given data on the previously selected
        ``broadcast_channel``.

        Data may be of type ``int``, ``float``, ``str``, ``bytes``,
        ``True``, or ``False``. It can also be a list or tuple of these.

        Choose ``None`` to stop broadcasting. This helps improve performance
        when you don't need the broadcast feature, especially when observing
        at the same time.

        The total data size is quite limited (26 bytes). ``True`` and
        ``False`` take 1 byte each. ``float`` takes 5 bytes. ``int`` takes 2 to
        5 bytes depending on how big the number is. ``str`` and ``bytes`` take
        the number of bytes in the object plus one extra byte.

        When multitasking, only one task can broadcast at a time. To broadcast
        information from multiple tasks (or block stacks), you could use a
        dedicated separate task that broadcast new values when one or more
        variables change.

        Args:
            data: The value or values to be broadcast.

        Raises:
            RuntimeError: If no ``broadcast_channel`` was configured.
            ValueError: If the encoded data exceeds 26 bytes.
            TypeError: If ``data`` contains a value that is not ``bool``,
                ``int``, ``float``, ``str``, or ``bytes``.
        """

    def observe(self, channel: int) -> Optional[
        Union[
            Tuple[Union[bool, int, float, str, bytes], ...],
            Union[bool, int, float, str, bytes],
        ]
    ]:
        """observe(channel) -> bool | int | float | str | bytes | tuple | None

        Retrieves the last observed data for a given channel.

        Receiving data is more reliable when the hub is not connected
        to a computer or other devices at the same time.

        Args:
            channel (int): The channel to observe. Must be one of the channels
                given to ``observe_channels`` when creating this object.

        Returns:
            The received data in the same format as it was sent, or ``None``
            if no data has been received within the last second.

        Raises:
            ValueError: If ``channel`` was not in ``observe_channels``.
        """

    def signal_strength(self, channel: int) -> int:
        """signal_strength(channel) -> int: dBm

        Gets the average signal strength in dBm for the given channel.

        This indicates how near the broadcasting device is. Nearby devices
        may have a signal strength around -40 dBm, while far away devices
        might have a signal strength around -70 dBm.

        Args:
            channel (int): The channel number. Must be one of the channels
                given to ``observe_channels`` when creating this object.

        Returns:
            The signal strength, or ``-128`` if no data has been received
            within the last second.

        Raises:
            ValueError: If ``channel`` was not in ``observe_channels``.
        """

    def version(self) -> str:
        """version() -> str

        Gets the firmware version from the Bluetooth chip.
        """


class Connection:
    @abstractmethod
    def read_from_mailbox(self, name: str) -> bytes: ...

    @abstractmethod
    def send_to_mailbox(self, name: str, data: bytes) -> None: ...

    @abstractmethod
    def wait_for_mailbox_update(self, name: str) -> None: ...


class Mailbox(Generic[T]):
    def __init__(
        self,
        name: str,
        connection: Connection,
        encode: Optional[Callable[[T], bytes]] = None,
        decode: Optional[Callable[[bytes], T]] = None,
    ):
        """Mailbox(name, connection, encode=None, decode=None)

        Object that represents a mailbox containing data.

        You can read data that is delivered by other EV3 bricks, or send data
        to other bricks that have the same mailbox.

        By default, the mailbox reads and sends only bytes. To send other
        data, you can provide an ``encode`` function that encodes your Python
        object into bytes, and a ``decode`` function to convert bytes back to
        a Python object.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
            encode (callable):
                Function that encodes a Python object to bytes.
            decode (callable):
                Function that creates a new Python object from bytes.
        """

    def read(self) -> T:
        """read()

        Gets the current value of the mailbox.

        Returns:
            The current value or ``None`` if the mailbox is empty.
        """
        return ""

    def send(self, value: T, brick: Optional[str] = None) -> None:
        """send(value, brick=None)

        Sends a value to this mailbox on connected devices.

        Arguments:
            value:
                The value that will be delivered to the mailbox.
            brick (str):
                The name or Bluetooth address of the brick or ``None``
                to broadcast to all connected devices.

        Raises:
            OSError:
                There is a problem with the connection.
        """

    def wait(self) -> None:
        """wait()

        Waits for the mailbox to be updated by a remote device."""

    def wait_new(self) -> T:
        """wait_new()

        Waits for a new value to be delivered to the mailbox that is not
        equal to the current value in the mailbox.

        Returns:
            The new value.
        """
        return object()


class LogicMailbox(Mailbox[bool]):
    def __init__(self, name: str, connection: Connection):
        """LogicMailbox(name, connection)

        Object that represents a mailbox containing boolean data.

        This works just like a regular :class:`Mailbox`, but values
        must be ``True`` or ``False``.

        This is compatible with the "logic" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """


class NumericMailbox(Mailbox[float]):
    def __init__(self, name: str, connection: Connection):
        """NumericMailbox(name, connection)

        Object that represents a mailbox containing numeric data.

        This works just like a regular :class:`Mailbox`, but values must be a
        number, such as ``15`` or ``12.345``

        This is compatible with the "numeric" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """


class TextMailbox(Mailbox[str]):
    def __init__(self, name: str, connection: Connection):
        """TextMailbox(name, connection)

        Object that represents a mailbox containing text data.

        This works just like a regular :class:`Mailbox`, but data must be a
        string, such as ``'hello!'``.

        This is compatible with the "text" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """


class BluetoothMailboxServer:
    """Object that represents a Bluetooth connection from one or more remote
    EV3s.

    The remote EV3s can either be running MicroPython or the standard EV3
    firmware.

    A "server" waits for a "client" to connect to it.
    """

    def __enter__(self) -> BluetoothMailboxServer:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.server_close()

    def wait_for_connection(self, count: int = 1) -> None:
        """wait_for_connection(count=1)

        Waits for a :class:`BluetoothMailboxClient` on a remote device to
        connect.

        Arguments:
            count (int):
                The number of remote connections to wait for.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def server_close(self) -> None:
        """server_close()

        Closes all connections."""


class BluetoothMailboxClient:
    """Object that represents a Bluetooth connection to one or more remote EV3s.

    The remote EV3s can either be running MicroPython or the standard EV3
    firmware.

    A "client" initiates a connection to a waiting "server".
    """

    def __enter__(self) -> BluetoothMailboxClient:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.close()

    def connect(self, brick: str) -> None:
        """connect(brick)

        Connects to an :class:`BluetoothMailboxServer` on another device.

        The remote device must be paired and waiting for a connection. See
        :meth:`BluetoothMailboxServer.wait_for_connection`.

        Arguments:
            brick (str):
                The name or Bluetooth address of the remote EV3 to connect to.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def close(self) -> None:
        """close()

        Closes all connections."""


class AppData:
    """
    Exchange raw data with the Pybricks Code host application over USB or
    Bluetooth. This is used by the smart sensor features like the vision
    processors.

    Each processor has one mode and produces a fixed amount of data. These are
    continuously sent to the hub as they change. The user code can read these
    buffered values at any time without blocking. All values are initially zero.

    From the hub's perspective, writing back to the host is an awaitable operation.
    Can be used to configure modes and mode settings.

    Only one instance may exist at a time. Must be created during program
    initialization. After that, all methods may be used while multi-tasking.
    """

    def __init__(self, modes: List[Tuple[int, int]]):
        """AppData(modes)

        Arguments:
            modes:
                A list of ``(mode, size)`` tuples, where ``mode`` is a mode
                number (0 to 255) and ``size`` is the number of bytes to
                allocate for that mode's receive buffer. Mode numbers must be
                unique. The list is sorted by mode number automatically.

        Raises:
            RuntimeError: If an ``AppData`` instance already exists.
            TypeError: If ``modes`` is not a list, or if any element is not a
                ``(mode, size)`` tuple with a mode value of 0 to 255.
            ValueError: If any mode number appears more than once.
        """

    def get_bytes(self, mode: int, index: Optional[int] = None) -> Union[bytes, int]:
        """get_bytes(mode, index=None) -> bytes | int

        Gets data received from the host for the given mode.

        Args:
            mode (int): The mode number to read.
            index (int): If given, returns the single byte at this position
                within the mode's buffer as an integer. Otherwise returns
                the entire mode buffer as ``bytes``.

        Returns:
            All received bytes for the mode, or a single byte as an integer
            if ``index`` is given.

        Raises:
            ValueError: If ``mode`` was not configured, or if ``index`` is
                out of range.
        """

    def write_bytes(self, data: bytes) -> MaybeAwaitable:
        """write_bytes(data)

        Sends raw bytes to the host application.

        Args:
            data (bytes): The data to send.
        """

    def configure(self, mode: int, parameter: int, value: bytes) -> MaybeAwaitable:
        """configure(mode, parameter, value)

        Sends a configuration command to the host for the given mode.

        This is a wrapper around :meth:`write_bytes`. It prepends a
        ``[0x01, mode, parameter]`` header to configure mode settings.

        Args:
            mode (int): The mode number to configure.
            parameter (int): The parameter identifier within the mode.
            value (bytes): The configuration value to send.
        """

    def close(self) -> None:
        """close()

        Deactivates the data callback and releases the receive buffer.

        This is also called automatically when the object is garbage collected.
        """


if TYPE_CHECKING:
    del MaybeAwaitable
    del T
