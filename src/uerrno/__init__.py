# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uerrno.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
This module provides access to symbolic error codes for `OSError` exception.
"""

from typing import Dict

EAGAIN: int
"""
The operation is not complete and should be tried again soon.
"""

EBUSY: int
"""
The device or resource is busy and cannot be used right now.
"""

ECANCELED: int
"""
The operation was canceled.
"""

EINVAL: int
"""
An invalid argument was given. Usually ``ValueError`` is used instead.
"""

EIO: int
"""
An unspecified error occurred.
"""

ENODEV: int
"""
Device was not found. For example, a sensor or motor is not plugged in the correct port.
"""

EOPNOTSUPP: int
"""
The operation is not supported on this hub or on the connected device.
"""

EPERM: int
"""
The operation cannot be performed in the current state.
"""

ETIMEDOUT: int
"""
The operation timed out.
"""

# TODO: ev3dev has additional constants
# https://github.com/pybricks/pybricks-micropython/blob/11f19bc9c24fde66aa8ad42233a345e6683f5beb/bricks/ev3dev/mpconfigport.h#L156-L203

errorcode: Dict[int, str]
"""
Dictionary that maps numeric error codes to strings with symbolic error code.
"""
