# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uio.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module contains ``stream`` objects that behave like files.
"""

# TODO: open() is not implemented on Powered Up hubs

from typing import overload, Union

# TODO: MicroPython streams implement '__enter__', '__exit__', 'close', 'read',
# 'readinto', 'readline', 'write', 'flush', 'seek', 'tell'
# and are iterable


class BytesIO:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, data: Union[bytes, bytearray]) -> None:
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        BytesIO(​)
        BytesIO(data)
        BytesIO(alloc_size)

        A binary stream using an in-memory bytes buffer.

        Arguments:
            data (bytes or bytearray): Optional bytes-like object
                that contains initial data.
            alloc_size (int): Optional number of preallocated bytes. This
                parameter is unique to MicroPython. It is not recommended to
                use it in end-user code.
        """

    def getvalue(self) -> bytes:
        """
        getvalue() -> bytes

        Gets the contents of the underlying buffer.
        """


class StringIO:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, string: str) -> None:
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        StringIO(​)
        StringIO(string)
        StringIO(alloc_size)

        A stream using an in-memory string buffer.

        Arguments:
            string (str): Optional string with initial data.
            alloc_size (int): Optional number of preallocated bytes. This
                parameter is unique to MicroPython. It is not recommended to
                use it in end-user code.
        """

    def getvalue(self) -> str:
        """
        getvalue() -> str

        Gets the contents of the underlying buffer.
        """


class FileIO:
    """
    This type represents a file opened in binary mode with ``open(name, 'rb')``.
    You should not instantiate this class directly.
    """
