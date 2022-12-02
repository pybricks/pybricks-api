# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors
#
# Documentation adapted from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/json.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Convert between Python objects and the JSON data format.
"""

from typing import IO, Any, Tuple


def dump(object: Any, stream: IO, separators: Tuple[str, str] = (", ", ": ")):
    """
    dump(object, stream, separators=(", ", ": "))

    Serializes an object to a JSON string and write it to a stream.

    Arguments:
        obj: Object to serialize.
        stream: Stream to write the output to.
        separators (tuple): An ``(item_separator, key_separator)`` tuple to
            specify how elements should be separated.
    """


def dumps(object: Any, separators: Tuple[str, str] = (", ", ": ")) -> str:
    """
    dumps(object, separators=(", ", ": "))

    Serializes an object to JSON and return it as a string

    Arguments:
        obj: Object to serialize.
        separators (tuple): An ``(item_separator, key_separator)`` tuple to
            specify how elements should be separated.

    Return:
        The JSON string.
    """


def load(stream: IO) -> Any:
    """
    load(stream)

    Parses the stream to interpret and deserialize the JSON data to a
    MicroPython object.

    Parsing continues until end-of-file is encountered. A ``ValueError`` is
    raised if the data in stream is not correctly formed.

    Arguments:
        stream: Stream from which to read the JSON string.

    Returns:
        The deserialized MicroPython object.
    """


def loads(string) -> Any:
    """
    loads(string)

    Parses the string to interpret and deserialize the JSON data to a
    MicroPython object.

    A ``ValueError`` is raised if the string is not correctly formed.

    Arguments:
        string (str): JSON string to decode.

    Returns:
        The deserialized MicroPython object.
    """
