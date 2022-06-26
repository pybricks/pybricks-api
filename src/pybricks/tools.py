# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Common tools for timing and data logging."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .parameters import Number


def wait(time: Number) -> None:
    """wait(time)

    Pauses the user program for a specified amount of time.

    Arguments:
        time (Number, ms): How long to wait.
    """


class StopWatch:
    """A stopwatch to measure time intervals. Similar to the stopwatch
    feature on your phone."""

    def __init__(self):
        ...

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


# HACK: hide from jedi
if TYPE_CHECKING:
    del Number
