# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/micropython.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Access and control MicroPython internals.
"""

from typing import Any, overload


def const(value: int) -> int:
    """
    Declares the value as a constant. This value will be
    substituted wherever it is used, which makes your code more efficient.

    To reduce memory usage further, prefix its name with an
    underscore (``_ORANGES``). This constant can only be used within the
    same file.

    If you want to import the value from another module, use a name without an
    underscore (``APPLES``). This uses a bit more memory.
    """
    ...


@overload
def opt_level() -> int:
    ...


@overload
def opt_level(level: int) -> None:
    ...


def opt_level(*args):
    """
    Sets the optimization level for code compiled on the hub:

    0. Assertion statements are enabled. The built-in ``__debug__`` variable
       is ``True``. Script line numbers are saved, so they can be reported when
       an Exception occurs.
    1. Assertions are ignored and ``__debug__`` is ``False``.
       Script line numbers are saved.
    2. Assertions are ignored and ``__debug__`` is ``False``.
       Script line numbers are saved.
    3. Assertions are ignored and ``__debug__`` is ``False``.
       Script line numbers are *not* saved.

    This applies only to code that you run in the REPL, because regular scripts
    are already compiled before they are sent to the hub.

    If no argument is given, this function returns the current optimization
    level.

    """


@overload
def mem_info() -> None:
    ...


@overload
def mem_info(verbose: Any) -> None:
    ...


def mem_info(*args):
    """
    Prints information about stack and heap memory usage.

    If the ``verbose`` argument is given, it also prints out
    the entire heap, indicating which blocks are used and which are free.
    """


@overload
def qstr_info() -> None:
    ...


@overload
def qstr_info(verbose: Any) -> None:
    ...


def qstr_info(*args):
    """
    Prints how many strings are interned and how much RAM they use.

    MicroPython uses string interning to save both RAM and ROM.
    This avoids having to store duplicate copies of the same string.

    If the ``verbose`` argument is given it also prints out the names of all
    RAM-interned strings.
    """


def stack_use() -> int:
    """
    Returns the amount of stack that is being used. This can be used to
    compute differences in stack usage at different points in a script.
    """


# REVISIT: Skipping heap lock funcs for now


def kbd_intr(chr: int) -> None:
    """
    Set the character that will raise a ``KeyboardInterrupt`` exception.  By
    default this is set to ``3`` during script execution, corresponding to
    :kbd:`Ctrl-C`. Passing ``-1`` to this function will disable capture of
    :kbd:`Ctrl-C`, and passing ``3`` will restore it.

    This function can be used to prevent the capturing of :kbd:`Ctrl-C` on the
    incoming stream of characters that is usually used for the REPL, in case
    that stream is used for other purposes.
    """
