# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/sys.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides a subset of the standard Python ``sys`` module.
"""

from uio import FileIO

# REVISIT: most functions are excluded since they aren't useful for Pybricks

stdin: FileIO = FileIO()
"""
Stream object (:class:`uio.FileIO`) that receives input from a connected
terminal, if any.

Writing may modify newline characters. Use ``usys.stdin.buffer`` instead if
this is undesirable.

Also see :func:`micropython.kbd_intr` to disable ``KeyboardInterrupt`` if you
are passing binary data via ``stdin``.
"""

stdout: FileIO = FileIO()
"""
Stream object (:class:`uio.FileIO`) that sends output to a connected terminal,
if any.

Reading may modify newline characters. Use ``usys.stdout.buffer`` instead if
this is undesirable.
"""

stderr: FileIO = FileIO()
"""
Alias for :data:`stdout`.
"""
