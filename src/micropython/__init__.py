# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/micropython.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Access and control MicroPython internals.
"""

from typing import Any, Literal, overload


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
def opt_level() -> None:
    ...


@overload
def opt_level(level: Literal[0, 1, 2, 3]) -> None:
    ...


def opt_level(*args):
    """
    If ``level`` is given then this function sets the optimization level for subsequent
    compilation of scripts, and returns ``None``.  Otherwise it returns the current
    optimization level.

    The optimization level controls the following compilation features:

    - Assertions: at level 0 assertion statements are enabled and compiled into the
      bytecode; at levels 1 and higher assertions are not compiled.
    - Built-in ``__debug__`` variable: at level 0 this variable expands to ``True``;
      at levels 1 and higher it expands to ``False``.
    - Source-code line numbers: at levels 0, 1 and 2 source-code line number are
      stored along with the bytecode so that exceptions can report the line number
      they occurred at; at levels 3 and higher line numbers are not stored.

    The default optimization level is usually level 0.
    """


@overload
def mem_info() -> None:
    ...


@overload
def mem_info(verbose: Any) -> None:
    ...


def mem_info(*args):
    """
    Print information about currently used memory.  If the ``verbose`` argument
    is given then extra information is printed.

    The information that is printed is implementation dependent, but currently
    includes the amount of stack and heap used.  In verbose mode it prints out
    the entire heap indicating which blocks are used and which are free.
    """


@overload
def qstr_info() -> None:
    ...


@overload
def qstr_info(verbose: Any) -> None:
    ...


def qstr_info(*args):
    """
    Print information about currently interned strings.  If the ``verbose``
    argument is given then extra information is printed.

    The information that is printed is implementation dependent, but currently
    includes the number of interned strings and the amount of RAM they use.  In
    verbose mode it prints out the names of all RAM-interned strings.
    """


def stack_use() -> None:
    """
    Return an integer representing the current amount of stack that is being
    used.  The absolute value of this is not particularly useful, rather it
    should be used to compute differences in stack usage at different points.
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
