# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2026 The Pybricks Authors

"""
Classes to send and receive messages from another device.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, Self, TypeVar, overload

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Sequence

    from ._common import MaybeAwaitable

T = TypeVar("T")


class BLERadio:
    """
    Send and receive messages without a connection using Bluetooth Low Energy.

    .. versionadded:: 4.0

        This used to be part of each hub class.
    """

    def __init__(
        self,
        broadcast_channel: int | None = None,
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
        self, data: Iterable[bool | int | float | str | bytes]
    ) -> MaybeAwaitable: ...

    @overload
    def broadcast(self, data: bool | float | str | bytes) -> MaybeAwaitable: ...

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

    def observe(
        self, channel: int
    ) -> (
        tuple[bool | int | float | str | bytes, ...]
        | bool
        | int
        | float
        | str
        | bytes
        | None
    ):
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


class HubNetwork:
    """
    Send and receive messages between supported hubs using Bluetooth.

    Create this object in every program that takes part in the network. One
    hub, called the *manager*, then connects to others identified by their
    address. For example: :meth:`connect('00:16:53:12:34:56') <connect>`.
    After that, all hubs are equal: each one can send messages to any other
    brick.

    You can find the address of each hub in the EV3 settings menu, or print it
    with the :meth:`address` method. Connections are preserved when you
    restart a program.

    The protocol ensures that messages get delivered. But they will only be
    seen in your program if there is enough room. The manager takes care of
    relaying messages in the background, which only works while the manager
    program is still running.

    .. versionadded:: 4.1
    """

    def __init__(self, inbox_size: int = 1024):
        """HubNetwork(inbox_size=1024)

        Arguments:
            inbox_size (int): How many bytes of messages to store for each
                brick that sends them.

        Raises:
            RuntimeError: If a ``HubNetwork`` object already exists, or if
                this is used after multitasking has started.
            OSError: If this brick has no working Bluetooth.
            ValueError: If ``inbox_size`` is too small to hold one message.
        """

    def address(self) -> str:
        """address() -> str

        Gets the Bluetooth address of this brick.

        This is the same address that is shown on the brick's screen. You can
        print it to find out which address to type in the programs of the
        other bricks.

        Returns:
            The address of this brick, such as ``'00:16:53:AB:CD:EF'``. The
            letters are always uppercase.
        """
        return ""

    def connect(self, address: str) -> MaybeAwaitable:
        """connect(address)

        Connects to one other hub (EV3 Brick) to set up the network.

        Only one hub in the network does this. That hub is called the manager.
        The other hubs don't have to run a program yet. They just won't
        receive messages until their programs run.

        Connecting is slow. It takes up to about fifteen seconds per brick,
        and it does not always work on the first try, so it tries again a few
        times before it gives up. This is why you normally do this at the
        start of your program.

        A brick that is already connected is ready right away, so it is safe
        to use this again later. This makes the second run very quick to start.

        Arguments:
            address (str): The Bluetooth address of the brick to connect to,
                such as ``'00:16:53:12:34:56'``. You can connect to up to
                seven other bricks.

        Raises:
            OSError: If the brick could not be reached. ValueError: If
                ``address`` is not a valid Bluetooth address, or if it is the
                address of this brick.
        """

    def is_connected(self, address: str | None = None) -> bool:
        """
        is_connected() -> bool
        is_connected(address) -> bool

        Checks whether a brick has joined the network.

        This is useful on the bricks that wait. They can keep checking
        ``is_connected()`` until the manager brick has reached them, instead
        of guessing how long the network takes to set up.

        Only the manager brick can use the ``address`` argument to check
        individual bricks.

        Arguments:
            address (str): The Bluetooth address of the hub to check.

        Returns:
            ``True`` if the hub has joined the network, ``False`` if not. If
            no address is given, it is ``True`` if any hub is connected.

        Raises:
            ValueError: If ``address`` is not a valid Bluetooth address.
        """
        return False

    def send(
        self,
        data: bool
        | float
        | str
        | bytes
        | None
        | tuple[bool | int | float | str | bytes | None, ...],
        address: str | None = None,
    ) -> MaybeAwaitable:
        """
        send(data) send(data, address)

        Sends a message to all hubs on the network, or to one specific hub.

        A message is one object, or a tuple of objects. An object may be of
        type ``int``, ``float``, ``str``, ``bytes``, ``True``, ``False``, or
        ``None``. The brick that receives it gets the same objects back, so
        sending ``(60, "left")`` arrives as ``(60, "left")``.

        A message that is only ``bytes`` is sent just as it is, which is what
        you want if you build your own messages. Such a message can hold 255
        bytes. Every other message also carries a short description of the
        objects in it, so a little less fits: ``True``, ``False`` and ``None``
        take 2 bytes each, ``int`` and ``float`` take 5 bytes each, and
        ``str`` and ``bytes`` take the number of bytes in them plus 2 to 4.
        One message holds up to 32 objects.

        Messages from this brick to one other brick arrive in the order that
        you sent them.

        Arguments:
            data: The message to send.
            address (str): The Bluetooth address of
                the brick to send to. Leave out to send to every other brick
                on the network. A brick never receives its own messages.

        Raises:
            ValueError: If ``address`` is not a valid Bluetooth address, or if
                the message is too big to send.
            TypeError: If the message holds an object that cannot be sent.
        """

    def inbox(
        self, latest: bool = False
    ) -> tuple[
        tuple[
            str,
            bool
            | int
            | float
            | str
            | bytes
            | None
            | tuple[bool | int | float | str | bytes | None, ...],
        ],
        ...,
    ]:
        """inbox(latest=False) -> tuple

        Gets the messages that have arrived since you last read them.

        This never waits. If nothing has arrived, you get an empty result, so
        a ``for`` loop over it simply does nothing. Reading removes the messages from this brick's memory, so each message
        is given to you only once.

        Every brick that sends to you gets an inbox of its own internally.
        When one brick sends more than fits in its inbox, its oldest message
        is dropped. A brick that sends all the time cannot push another
        brick's messages out.

        A program never receives messages that were sent before it started.
        Messages are given to you in the order that they arrived, no matter
        which brick sent them.

        Arguments:
            latest (bool): Choose ``True`` to keep only the newest message
                from each brick and throw the older ones away. This is what
                you want when a brick keeps sending you its latest value, such
                as a sensor reading, and only the newest one is of any use.

        Returns:
            A tuple of ``(address, data)`` pairs, where ``address`` is the
            Bluetooth address of the brick that sent the message, and ``data``
            is the message in the same form as it was sent. With ``latest``,
            there is at most one pair per brick.

        Raises:
            ValueError: If a message does not match the description it carries
                with it, which means that it was damaged on the way.
        """
        return ()


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
        encode: Callable[[T], bytes] | None = None,
        decode: Callable[[bytes], T] | None = None,
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

    def send(self, value: T, brick: str | None = None) -> None:
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

    def __enter__(self) -> Self:
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

    def __enter__(self) -> Self:
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

    def __init__(self, modes: list[tuple[int, int]]):
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

    def get_bytes(self, mode: int, index: int | None = None) -> bytes | int:
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


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del abstractmethod
    del Callable
    del Iterable
    del MaybeAwaitable
    del Sequence
    del T
