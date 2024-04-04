# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Common tools for timing, data logging, and linear algebra."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Sequence, Tuple, overload, Coroutine

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


def wait(time: Number) -> MaybeAwaitable:
    """wait(time)

    Pauses the user program for a specified amount of time.

    Arguments:
        time (Number, ms): How long to wait.
    """


class StopWatch:
    """A stopwatch to measure time intervals. Similar to the stopwatch
    feature on your phone."""

    def __init__(self): ...

    def time(self) -> int:
        """time() -> int: ms

        Gets the current time of the stopwatch.

        Returns:
            Elapsed time.
        """

    def pause(self) -> None:
        """pause()

        Pauses the stopwatch."""

    def resume(self) -> None:
        """resume()

        Resumes the stopwatch."""

    def reset(self) -> None:
        """reset()

        Resets the stopwatch time to 0.

        The run state is unaffected:

        * If it was paused, it stays paused (but now at 0).
        * If it was running, it stays running (but starting again from 0).
        """


class DataLog:
    """Create a file and log data."""

    def __init__(
        self,
        *headers: str,
        name: str = "log",
        timestamp: bool = True,
        extension: str = "csv",
        append: bool = False,
    ):
        """DataLog(*headers, name='log', timestamp=True, extension='csv', append=False)

        Arguments:
            headers (str, str, ...): Column headers. These are the
                names of the data columns. For example, choose ``'time'`` and
                ``'angle'``.
            name (str): Name of the file.
            timestamp (bool): Choose ``True`` to add the date and time to the
                file name. This way, your file has a unique name.
                Choose ``False`` to omit the timestamp.
            extension (str): File extension.
            append (bool): Choose ``True`` to reopen an existing data log file
                and append data to it. Choose ``False`` to clear existing
                data. If the file does not exist yet, an empty file will be
                created either way.
        """

    def log(self, *values: Any) -> None:
        """log(value1, value2, ...)

        Saves one or more values on a new line in the file.

        Arguments:
            values (object, object, ...): One or more objects or values.
        """


class Matrix:
    """Mathematical representation of a matrix. It supports
    addition (``A + B``), subtraction (``A - B``),
    and matrix multiplication (``A * B``) for matrices of compatible size.

    It also supports scalar multiplication (``c * A`` or ``A * c``)
    and scalar division (``A / c``).

    A :class:`.Matrix` object is immutable."""

    def __add__(self, other) -> Matrix: ...

    def __iadd__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __isub__(self, other) -> Matrix: ...

    def __mul__(self, other) -> Matrix: ...

    def __rmul__(self, other) -> Matrix: ...

    def __imul__(self, other) -> Matrix: ...

    def __truediv__(self, other) -> Matrix: ...

    def __itruediv__(self, other) -> Matrix: ...

    def __floordiv__(self, other) -> Matrix: ...

    def __ifloordiv__(self, other) -> Matrix: ...

    def __init__(self, rows: Sequence[Sequence[float]]):
        """Matrix(rows)

        Arguments:
            rows (list): List of rows. Each row is itself a list of numbers.

        """

    @property
    def T(self) -> Matrix:  # noqa: N802
        """Returns a new :class:`.Matrix` that is the transpose of the
        original."""

    @property
    def shape(self) -> Tuple[int, int]:
        """Returns a tuple (``m``, ``n``),
        where ``m`` is the number of rows and ``n`` is the number of columns.
        """


@overload
def vector(x: float, y: float) -> Matrix:
    """
    Convenience function to create a :class:`.Matrix` with the shape (``2``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.

    Returns:
        A matrix with the shape of a column vector.
    """


@overload
def vector(x: float, y: float, z: float) -> Matrix:
    """
    Convenience function to create a :class:`.Matrix` with the shape (``3``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.
        z (float): z-coordinate of the vector.

    Returns:
        A matrix with the shape of a column vector.
    """


def vector(*args):
    """
    vector(x, y) -> Matrix
    vector(x, y, z) -> Matrix

    Convenience function to create a :class:`.Matrix` with the
    shape (``2``, ``1``) or (``3``, ``1``).

    Arguments:
        x (float): x-coordinate of the vector.
        y (float): y-coordinate of the vector.
        z (float): z-coordinate of the vector (optional).

    Returns:
        A matrix with the shape of a column vector.
    """


def cross(a: Matrix, b: Matrix) -> Matrix:
    """
    cross(a, b) -> Matrix

    Gets the cross product ``a`` × ``b`` of two vectors.

    Arguments:
        a (Matrix): A three-dimensional vector.
        b (Matrix): A three-dimensional vector.

    Returns:
        The cross product, also a three-dimensional vector.
    """


def read_input_byte(last: bool = False, chr: bool = False) -> Optional[int | str]:
    """
    read_input_byte() -> int | str | None

    Reads one byte from standard input without blocking and removes it from the
    input buffer.

    Arguments:
        last (bool): Choose ``True`` to read the last (most recent) byte in the buffer and discard the rest.
                     Choose ``False`` to read only the first (oldest) byte.
        chr (bool): Choose ``True`` to convert the result to a one-character string.

    Returns:
        The byte that was read, as a numeric value (``0`` to ``255``) or
        string (e.g. ``"B"``). Returns ``None`` if no data is available. If
        ``chr=True``, it also return ``None`` if the byte that was read is not
        printable as a character.
    """


def hub_menu(*symbols: int | str) -> int | str:
    """
    hub_menu(symbol1, symbol2, ...) -> int | str

    Shows a menu on the hub display and waits for the user to select an item
    using the buttons. Can be used in your own menu-program that lets you
    choose which of your other programs to run.

    Note that this is just a convenience function that combines the display,
    buttons, and waits to make a simple menu. This means that it can be used
    anywhere in a program, not just at the start.

    Arguments:
        symbol1 (int or str): The first symbol to show in the menu.
        symbol2 (int or str): The second symbol, and so on...

    Returns:
        The selected symbol.
    """


def multitask(*coroutines: Coroutine, race=False) -> MaybeAwaitableTuple:
    """
    multitask(coroutine1, coroutine2, ...) -> Tuple

    Runs multiple coroutines concurrently. This creates a new coroutine that
    can be used like any other, including in another ``multitask`` statement.

    Arguments:
        coroutines (coroutine, coroutine, ...): One or more coroutines to run
            in parallel.
        race (bool): Choose ``False`` to wait for all coroutines to finish.
            Choose ``True`` to wait for one coroutine to finish and then
            cancel the others, as if it's a "race".

    Returns:
        Tuple of the return values of each coroutine. Unfinished coroutines
        will have ``None`` as their return value.
    """


def run_task(coroutine: Coroutine) -> Optional[bool]:
    """
    run_task(coroutine) -> bool | None

    Runs a coroutine from start to finish while blocking the rest of the
    program. This is used primarily to run the main coroutine of a program.

    Calls to this function are not allowed to be nested.

    Arguments:
        coroutine (coroutine): The main coroutine to run.

    Returns:
        If no ``coroutine`` is given, this function returns whether the
        run loop is currently active (``True``) or not (``False``).
    """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Number
    del MaybeAwaitable
    del MaybeAwaitableTuple
