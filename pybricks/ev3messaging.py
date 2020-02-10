# SPDX-License-Identifier: MIT
# Copyright (C) 2020 David Lechner

"""
This module contains everything to do with EV3 bytecode messages.

.. availability::
    :ev3dev-stretch:

.. versionadded:: 2.0.0
"""


class Mailbox:
    def __init__(self, name, connection, encode=repr, decode=eval):
        """Object that represents a mailbox that contains encoded data.

        See :class:`LogicMailbox`, :class:`NumericMailbox` and
        :class:`TextMailbox` for mailboxes that are compatible with the
        standard EV3 firmware and desktop programming software.

        ``encode`` is used in :meth:`send` and ``decode`` is used in
        :meth:`read`. The defaults of ``repr`` and ``eval`` work with most
        builtin types (like dict and list) but don't work for other objects
        (like motors and sensors).

        .. warning:: In general, ``eval`` is considered a security risk because
            it can execute arbitrary code! Never use ``eval`` with untrusted
            data, like like data received from the Internet.

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

    def read(self):
        """Gets the current value of the mailbox.

        Returns:
            The current value or ``None`` if the mailbox is empty.
        """
        return ''

    def send(self, value, brick=None):
        """Sends a value to this mailbox on connected devices.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            value:
                The value that will be delivered to the mailbox.
            brick (str):
                The name or Bluetooth address of the brick or ``None`` to
                to broadcast to all connected devices.

        Raises:
            OSError:
                There is a problem with the connection.
        """

    def wait(self):
        """Waits for the mailbox to be updated by remote device."""

    def wait_new(self):
        """Waits for a new value to be delivered to the mailbox that is not
        equal to the current value in the mailbox.


        Returns:
            The new value.
        """
        return object()


class LogicMailbox(Mailbox):
    def __init__(self, name, connection):
        """
        Object that represents a mailbox that contains a logic (true/false)
        value.

        This is compatible with the "logic" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """

    def read(self):
        """Gets the current value of the mailbox as a boolean value.

        Returns:
            bool:
                The current value or ``None`` if the mailbox is empty.
        """
        return ''

    def send(self, value, brick=None):
        """Sends a boolean value to this mailbox on connected devices.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            value (bool):
                The value that will be delivered to the mailbox.
            brick (str):
                The name or Bluetooth address of the brick or ``None`` to
                to broadcast to all connected devices.

        Raises:
            OSError:
                There is a problem with the connection.
        """


class NumericMailbox(Mailbox):
    def __init__(self, name, connection):
        """
        Object that represents a mailbox that contains a number.

        This is compatible with the "numeric" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """

    def read(self):
        """Gets the current value of the mailbox as a numeric value.

        Returns:
            float:
                The current value or ``None`` if the mailbox is empty.
        """
        return ''

    def send(self, value, brick=None):
        """Sends a numeric value to this mailbox on connected devices.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            value (float):
                The value that will be delivered to the mailbox.
            brick (str):
                The name or Bluetooth address of the brick or ``None`` to
                to broadcast to all connected devices.

        Raises:
            TypeError:
                ``value`` connot be converted to a floating point.
            OSError:
                There is a problem with the connection.
        """


class TextMailbox(Mailbox):
    def __init__(self, name, connection):
        """
        Object that represents a mailbox that contains text.

        This is compatible with the "text" mailbox type in EV3-G.

        Arguments:
            name (str):
                The name of this mailbox.
            connection:
                A connection object such as :class:`BluetoothMailboxClient`.
        """

    def read(self):
        """Gets the current value of the mailbox as a string value.

        Returns:
            str:
                The current value or ``None`` if the mailbox is empty.
        """
        return ""

    def send(self, value, brick=None):
        """Sends a string value to this mailbox on connected devices.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            value (str):
                The value that will be delivered to the mailbox.
            brick (str):
                The name or Bluetooth address of the brick or ``None`` to
                to broadcast to all connected devices.

        Raises:
            OSError:
                There is a problem with the connection.
        """


class BluetoothMailboxServer:
    """Object that represents an incoming Bluetooth connection from another
    EV3.

    The remote EV3 can either be running MicroPython or the standard EV3
    firmare.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def wait_for_connection(self, count=1):
        """Waits for a :class:`BluetoothMailboxClient` on a remote device to
        connect.

        Arguments:
            count (int):
                The number of remote connections to wait for.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def close(self):
        """Closes all connections."""


class BluetoothMailboxClient:
    """Object that represents an outgoing Bluetooth connection to another
    EV3.

    The remote EV3 can either be running MicroPython or the standard EV3
    firmare.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def connect(self, brick):
        """Connects to an :class:`BluetoothMailboxServer` on another device.

        The remote device must be paired and waiting for a connection. See
        :meth:`BluetoothMailboxServer.wait_for_connection`.

        .. todo:: Currently the Bluetooth address must be used instead of the
                  the brick name.

        Arguments:
            brick (str):
                The name or Bluetooth address of the remote EV3 to connect to.

        Raises:
            OSError:
                There was a problem establishing the connection.
        """

    def close(self):
        """Closes all connections."""
