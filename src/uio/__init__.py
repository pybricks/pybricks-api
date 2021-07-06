# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uio.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module contains additional types of ``stream`` (file-like) objects
and helper functions.
"""

# TODO: open() is not implemented on Powered Up hubs

from typing import overload

# TODO: MicroPython streams implement '__enter__', '__exit__', 'close', 'read',
# 'readinto', 'readline', 'write', 'flush', 'getvalue', 'seek', 'tell'
# and are iterable


class BytesIO:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, initial_bytes: bytes) -> None:
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        A binary stream using an in-memory bytes buffer.

        Args:
            initial_bytes: Optional bytes-like object that contains initial data.
            alloc_size: Optional number of preallocated bytes.
        """


class StringIO:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, initial_value: str) -> None:
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        A binary stream using an in-memory string buffer.

        Args:
            initial_value: Optional string object that contains initial data.
            alloc_size: Optional number of preallocated bytes.
        """


class FileIO:
    """
    This is type of a file open in binary mode, e.g. using ``open(name, 'rb')``.
    You should not instantiate this class directly.
    """
