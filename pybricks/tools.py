"""Common tools for timing and data logging."""


def wait(time):
    """Pause the user program for a specified amount of time.

    Arguments:
        time (:ref:`time`): How long to wait.

    """
    pass


class StopWatch():
    """A stopwatch to measure time intervals. Similar to the stopwatch
    feature on your phone."""

    def __init__(self):
        pass

    def time(self):
        """Get the current time of the stopwatch.

        Returns:
            :ref:`time`: Elapsed time.
        """
        pass

    def pause(self):
        """Pause the stopwatch."""
        pass

    def resume(self):
        """Resume the stopwatch."""
        pass

    def reset(self):
        """Reset the stopwatch time to 0.

        The run state is unaffected:

        * If it was paused, it stays paused (but now at 0).
        * If it was running, it stays running (but starting again from 0).
        """
        pass


class DataLog():
    """Create a file and log data."""

    def __init__(self, *headers, name='log', timestamp=True, extension='csv'):
        """

        Arguments:
            headers (`col1`, `col2`, `...`): Column headers. These are the
                names of the data columns. For example, choose ``'time'`` and
                ``'angle'``.
            name (str): Name of the file.
            timestamp (bool): Choose ``True`` to add the date and time to the
                file name. This way, your file has a unique name.
                Choose ``False`` to omit the timestamp.
            extension (str): File extension
        """
        pass

    def log(self, *values):
        """Save one or more values on a new line in the file.

        Arguments:
            values (object, object, `...`): One or more objects or values.
        """
        pass
