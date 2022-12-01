# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uselect.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides functions to efficiently wait for events on multiple streams.
"""

from typing import IO, Iterator, List, Tuple, overload

POLLIN: int
"""
Data is available for reading.
"""

POLLOUT: int
"""
More data can be written.
"""

POLLERR: int
"""
Error condition happened on the associated stream. Should be handled explicitly
or else further invocations of :meth:`poll` may return right away.
"""

POLLHUP: int
"""
Hang up happened on the associated stream. Should be handled explicitly
or else further invocations of :meth:`poll` may return right away.
"""


class Poll:
    def register(self, object: IO, eventmask: int) -> None:
        """
        register(object, eventmask=POLLOUT | POLLOUT)

        Register a stream object for polling. The stream object will now be
        monitored for events. If an event happens, it becomes part of the
        return value of :meth:`poll`.

        If this method is called again for the same stream object, the object
        will not be registered again, but the ``eventmask`` flags will be
        updated, as if calling :meth:`modify()`.

        Arguments:
            object (FileIO): Stream to be registered for polling.
            eventmask (int): Which events to use. Should be ``POLLIN``,
                ``POLLOUT``, or their logical disjunction: ``POLLIN | POLLOUT``.
        """

    def unregister(self, object: IO) -> None:
        """
        unregister(poll)

        Unregister an object from polling.

        Arguments:
            object (FileIO): Stream to be unregistered from polling.
        """

    def modify(self, obj: IO, eventmask: int) -> None:
        """
        modify(object, eventmask)

        Modifies the event mask for the stream object.

        Arguments:
            object (FileIO): Stream to be registered for polling.
            eventmask (int): Which events to use.

        Raises:
            ``OSError``: If the object is not registered. The error is ``ENOENT``.
        """

    @overload
    def poll(self) -> List[Tuple[IO, int]]:
        ...

    @overload
    def poll(self, timeout: int) -> List[Tuple[IO, int]]:
        ...

    def poll(self, timeout: int = -1, /) -> List[Tuple[IO, int]]:
        """
        poll(timeout=-1) -> List[Tuple[FileIO, int]]

        Wait until at least one of the registered objects has a new event or
        exceptional condition ready to be handled.

        Arguments:
            timeout (int): Timeout in milliseconds. Choose ``0`` to return
                immediately or choose ``-1`` to wait indefinitely.

        Returns:
            A list of tuples. There is one (``object``, ``eventmask``, ...)
            tuple for each object with an event, or no tuples if there are no
            events to be handled. The ``eventmask`` value
            is a combination of poll flags to indicate what happened. This may
            include ``POLLERR`` and ``POLLHUP`` even if they were not registered.
        """

    @overload
    def ipoll(self) -> Iterator[Tuple[IO, int]]:
        ...

    @overload
    def ipoll(self, timeout: int) -> Iterator[Tuple[IO, int]]:
        ...

    @overload
    def ipoll(self, timeout: int, flags: int) -> Iterator[Tuple[IO, int]]:
        ...

    def ipoll(self, timeout: int = -1, flags: int = 0, /) -> Iterator[Tuple[IO, int]]:
        """
        ipoll(timeout=-1, flags=1) -> Iterator[Tuple[FileIO, int]]

        First, just like :meth:`poll`, wait until at least one of the registered
        objects has a new event or exceptional condition ready to be handled.

        But instead of a list, this method returns an iterator for improved
        efficiency. The iterator yields one (``object``, ``eventmask``, ...)
        tuple at a time, and overwrites it when yielding the next value. If you
        need the values later, make sure to copy them explicitly.

        Arguments:
            timeout (int): Timeout in milliseconds. Choose ``0`` to return
                immediately or choose ``-1`` to wait indefinitely.
            flags (int): If set to ``1``, one-shot behavior for events is
                employed. This means that streams for which events happened
                will have their event masks automatically reset using
                ``poll.modify(obj, 0)``. This way, new events for such a stream
                won't be processed until a new mask is set with :meth:`modify`,
                which is useful for asynchronous I/O schedulers.
        """


def poll() -> Poll:
    """
    Creates an instance of the :class:`Poll` class.

    Returns:
        The :class:`Poll` instance.
    """
