# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/sys.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides a subset of the standard Python ``sys`` module.
"""

from typing import Tuple

from uio import FileIO as _FileIO

stdin: _FileIO = _FileIO()
"""
This is a stream object (:class:`uio.FileIO`) that receives input from a
connected terminal, if any.

Also see :func:`kbd_intr <micropython.kbd_intr>` to disable
``KeyboardInterrupt`` when passing binary data via ``stdin``.
"""

stdout: _FileIO = _FileIO()
"""
This is a stream object (:class:`uio.FileIO`) that sends output to a connected
terminal, if any.
"""

stderr: _FileIO = _FileIO()
"""
Alias for :data:`stdout`.
"""

implementation: Tuple[str, Tuple[int, int, int], str, int] = (
    "micropython",
    (1, 19, 1),
    "NAME Hub with PROCESSOR",
    6,
)
"""
MicroPython version tuple. See format and example below.
"""

version: str = "3.4.0; Pybricks MicroPython v3.2.0b5 on 2022-11-11"
"""
Python compatibility version, Pybricks version, and build date.
See format and example below.
"""

version_info: Tuple[int, int, int] = (3, 4, 0)
"""Python compatibility version. See format and example below."""
