# SPDX-License-Identifier: MIT
# Copyright (C) 2020 David Lechner

"""This module provides classes for working with Bluetooth Classic.

.. availability::
    :ev3dev-stretch:

.. versionadded:: 2.0.0
"""

from socketserver import BaseServer, ThreadingMixIn, StreamRequestHandler

try:
    from socket import BDADDR_ANY
except ImportError:
    BDADDR_ANY = '00:00:00:00:00:00'


__all__ = ['BDADDR_ANY', 'RFCOMMServer', 'ThreadingRFCOMMServer',
           'StreamRequestHandler', 'ALL_BRICKS', 'EV3MailboxServer',
           'EV3MailboxClient']


class RFCOMMServer(BaseServer):
    """Object that simplifies setting up an RFCOMM socket server.

    This is based on the ``socketserver.SocketServer`` class in the Python
    standard library.

    .. availability::
        :ev3dev-stretch:

    .. versionadded:: 2.0.0
    """


class ThreadingRFCOMMServer(ThreadingMixIn, RFCOMMServer):
    """Version of :class:`RFCOMMServer` that handles connections in a new
    thread.

    .. availability::
        :ev3dev-stretch:

    .. versionadded:: version

    .. versionadded:: 2.0.0
    """


ALL_BRICKS = None
"""Can be used in ``send`` methods to broadcast to call connected bricks.

.. availability::
    :ev3dev-stretch:

.. versionadded:: 2.0.0
"""

EV3_RFCOMM_CHANNEL = 1


class EV3MailboxMixIn:
    """Methods shared by both :class:`EV3MailboxServer` and
    :class:`EV3MailboxClient`

    .. availability::
        :ev3dev-stretch:

    .. versionadded:: 2.0.0
    """
    def get_raw_data(self, mbox):
        """Gets the current raw data from a mailbox.

        Arguments:
            mbox (str):
                The name of the mailbox.

        Returns:
            bytes:
                The current mailbox raw data or ``None`` if nothing has ever
                been delivered to the mailbox.
        """
        return b''

    def get_packed_data(self, mbox, fmt):
        """Gets the current packed data from a mailbox.

        Arguments:
            mbox (str):
                The name of the mailbox.
            fmt (str):
                ``ustruct.unpack()`` format string used to decode the binary
                data.

        Returns:
            tuple:
                The result of ``ustruct.unpack()`` on the mailbox data.

        Raises:
            TypeError:
                ``fmt`` is not a string.
            RuntimeError:
                ``mbox`` is empty.
        """
        return ()

    def get_logic(self, mbox):
        """Gets the current value of the mailbox as a boolean value.

        This is compatible with the "logic" mailbox type in EV3-G.

        Arguments:
            mbox (str):
                The name of the mailbox.

        Returns:
            bool:
                The current value or ``None`` if the mailbox is empty.
        """
        return False

    def get_numeric(self, mbox):
        """Gets the current value of the mailbox as a floating point value.

        This is compatible with the "numeric" mailbox type in EV3-G.

        Arguments:
            mbox (str):
                The name of the mailbox.

        Returns:
            float:
                The current value or ``None`` if the mailbox is empty.
        """
        return 0.0

    def get_text(self, mbox):
        """Gets the current value of the mailbox as a string value.

        This is compatible with the "text" mailbox type in EV3-G.

        Arguments:
            mbox (str):
                The name of the mailbox.

        Returns:
            str:
                The current value or ``None`` if the mailbox is empty.
        """
        return ""

    def send_raw_data(self, brick, mbox, payload):
        """Sends a mailbox value using raw bytes data.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the brick or
                :data:`ALL_BRICKS` to broadcast to all connected devices.
            mbox (str):
                The name of the mailbox.
            payload (bytes):
                A bytes-like object that will be sent to the mailbox.
        """

    def send_packed_data(self, brick, mbox, fmt, *args):
        """Sends a mailbox value using packed values.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the brick or
                :data:`ALL_BRICKS` to broadcast to all connected devices.
            mbox (str):
                The name of the mailbox.
            fmt (str):
                Format string compatible with ``ustruct.pack()``
            *:
                Arguments for ``ustruct.pack()``
        """

    def send_logic(self, brick, mbox, value):
        """Sends a boolean mailbox value.

        This is compatible with the "logic" mailbox type in EV3-G.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the brick or
                :data:`ALL_BRICKS` to broadcast to all connected devices.
            mbox (str):
                The name of the mailbox.
            value (bool):
                The value that will be delivered to the mailbox.
        """

    def send_numeric(self, brick, mbox, value):
        """Sends a float mailbox value.

        This is compatible with the "numeric" mailbox type in EV3-G.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the brick or
                :data:`ALL_BRICKS` to broadcast to all connected devices.
            mbox (str):
                The name of the mailbox.
            value (bool):
                The value that will be delivered to the mailbox.
        """

    def send_text(self, brick, mbox, value):
        """Sends a string mailbox value.

        This is compatible with the "text" mailbox type in EV3-G.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the brick or
                :data:`ALL_BRICKS` to broadcast to all connected devices.
            mbox (str):
                The name of the mailbox.
            value (bool):
                The value that will be delivered to the mailbox.
        """

    def wait_for_update(self, mbox):
        """Waits until ``mbox`` receives a value.

        Arguments:
            mbox (str):
                The name of the mailbox.
        """


class EV3MailboxServer(EV3MailboxMixIn, ThreadingRFCOMMServer):
    """Object that represents an incoming Bluetooth connection from another
    EV3.

    The remote EV3 can either be running MicroPython or the standard EV3
    firmare.

    See :class:`EV3MailboxMixIn` for additional methods.

    .. availability::
        :ev3dev-stretch:

    .. versionadded:: 2.0.0
    """
    def __init__(self):
        pass

    def wait_for_connection(self, count=1):
        """Waits for a :class:`EV3MailboxClient` on a remote device to connect.

        Arguments:
            count (int):
                The number of remote connections to wait for.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """


class EV3MailboxClient(EV3MailboxMixIn, ThreadingMixIn):
    """Object that represents an outgoing Bluetooth connection to another
    EV3.

    The remote EV3 can either be running MicroPython or the standard EV3
    firmare.

    See :class:`EV3MailboxMixIn` for additional methods.

    .. availability::
        :ev3dev-stretch:

    .. versionadded:: 2.0.0
    """
    def __init__(self, brick):
        """
        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the remote EV3 to connect to.
        """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def connect(self):
        """Connects to an :class:`EV3MailboxServer` on another device.

        The remote device must be paired and waiting for a connection. See
        :meth:`EV3MailboxServer.wait_for_connection`.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def close(self):
        """Closes the connection."""
