# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uselect.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides functions to efficiently wait for events on multiple streams.

.. note:: This module is not available on the BOOST Move hub.
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
Error condition happened on the associated stream.
"""

POLLHUP: int
"""
Hang up happened on the associated stream.
"""


def poll() -> "Poll":
    """
    Creates an instance of the Poll class.
    """


# skipping def select(...)


class Poll:
    @overload
    def register(self, obj: IO) -> None:
        ...

    @overload
    def register(self, obj: IO, eventmask: int) -> None:
        ...

    def register(self, obj: IO, eventmask: int) -> None:
        """
        Register `stream` ``obj`` for polling. ``eventmask`` is logical OR of:

        * :data:`POLLIN`
        * :data:`POLLOUT`

        Note that flags like :data:`POLLHUP` and :data:`POLLERR` are
        *not* valid as input eventmask (these are unsolicited events which
        will be returned from :meth:`poll` regardless of whether they are asked
        for). This semantics is per POSIX.

        ``eventmask`` defaults to ``POLLIN | POLLOUT``.

        It is OK to call this function multiple times for the same ``obj``.
        Successive calls will update ``obj``'s eventmask to the value of
        ``eventmask`` (i.e. will behave as :meth:`modify()`).
        """

    def unregister(self, obj: IO) -> None:
        """
        Unregister ``obj`` from polling.
        """

    def modify(self, obj: IO, eventmask: int) -> None:
        """
        Modify the ``eventmask`` for ``obj``. If ``obj`` is not registered, ``OSError``
        is raised with error of ``ENOENT``.
        """

    @overload
    def poll(self) -> List[Tuple[IO, int]]:
        ...

    @overload
    def poll(self, timeout: int) -> List[Tuple[IO, int]]:
        ...

    def poll(self, timeout: int = -1, /) -> List[Tuple[IO, int]]:
        """
        Wait for at least one of the registered objects to become ready or have an
        exceptional condition, with optional timeout in milliseconds (if ``timeout``
        arg is not specified or -1, there is no timeout).

        Returns list of (``obj``, ``event``, ...) tuples. There may be other elements in
        tuple, depending on a platform and version, so don't assume that its size is 2.
        The ``event`` element specifies which events happened with a stream and
        is a combination of ``POLL*`` constants described above. Note that
        flags :data:`POLLHUP` and :data:`POLLERR` can be returned at any time
        (even if were not asked for), and must be acted on accordingly (the
        corresponding stream unregistered from poll and likely closed), because
        otherwise all further invocations of :meth:`poll` may return immediately with
        these flags set for this stream again.

        In case of timeout, an empty list is returned.
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
        Like :meth:`poll`, but instead returns an iterator which yields a
        `callee-owned tuple`. This function provides an efficient, allocation-free
        way to poll on streams.

        If ``flags`` is 1, one-shot behavior for events is employed: streams for
        which events happened will have their event masks automatically reset
        (equivalent to ``poll.modify(obj, 0)``), so new events for such a stream
        won't be processed until new mask is set with :meth:`modify`. This
        behavior is useful for asynchronous I/O schedulers.
        """
