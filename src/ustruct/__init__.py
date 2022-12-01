# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/ustruct.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides functions to convert between Python values and C-like
data structs.
"""

from typing import Union, Tuple


def calcsize(format: str) -> int:
    """
    Gets the data size corresponding to a format string

    Arguments:
        format (str): Data format string.

    Returns:
        The number of bytes needed to represent this format.
    """


def pack(format: str, *values) -> bytes:
    """
    pack(format, value1, value2, ...)

    Packs the values using the given format.

    Arguments:
        format (str): Data format string.

    Returns:
        The data encoded as bytes.
    """


def pack_into(format: str, buffer: bytearray, offset: int, *values) -> bytes:
    """
    pack_into(format, buffer, offset, value1, value2, ...)

    Encode the values using the given format and write them to a given buffer.

    Arguments:
        format (str): Data format string.
        buffer (bytearray): Buffer to store the encoded data.
        offset (int): Offset from the start of the buffer. Use a negative value
            to count from the end of the buffer.
    """


def unpack(format: str, data: Union[bytes, bytearray]) -> Tuple:
    """
    unpack(format, data) -> Tuple

    Decodes the binary data using the given format.

    Arguments:
        format (str): Data format string.
        data (bytes or bytearray): Data to unpack.

    Returns:
        The decoded data as a tuple of values.
    """


def unpack_from(format: str, data: Union[bytes, bytearray], offset: int) -> Tuple:
    """
    unpack_from(format, data, offset) -> Tuple

    Decodes binary data from a buffer using the given format.

    Arguments:
        format (str): Data format string.
        data (bytes or bytearray): Data buffer to unpack.
        offset (int): Offset from the start of the data. Use a negative value
            to count from the end of the data.

    Returns:
        The decoded data as a tuple of values.
    """
