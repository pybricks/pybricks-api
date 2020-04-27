# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Common tools for timing and data logging."""


def wait(time):
    """Pauses the user program for a specified amount of time.

    Arguments:
        time (:ref:`time`): How long to wait.

    """
    pass


class StopWatch:
    """A stopwatch to measure time intervals. Similar to the stopwatch
    feature on your phone."""

    def __init__(self):
        pass

    def time(self):
        """Gets the current time of the stopwatch.

        Returns:
            :ref:`time`: Elapsed time.
        """
        pass

    def pause(self):
        """Pauses the stopwatch."""
        pass

    def resume(self):
        """Resumes the stopwatch."""
        pass

    def reset(self):
        """Resets the stopwatch time to 0.

        The run state is unaffected:

        * If it was paused, it stays paused (but now at 0).
        * If it was running, it stays running (but starting again from 0).
        """
        pass


class DataLog:
    """Create a file and log data."""

    def __init__(self, *headers, name='log', timestamp=True, extension='csv',
                 append=False):
        """

        Arguments:
            headers (`col1`, `col2`, `...`): Column headers. These are the
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
        pass

    def log(self, *values):
        """Saves one or more values on a new line in the file.

        Arguments:
            values (object, object, `...`): One or more objects or values.
        """
        pass
