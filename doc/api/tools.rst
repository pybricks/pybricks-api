:mod:`tools <pybricks.tools>` -- Timing and Data logging
========================================================

.. automodule:: pybricks.tools
    :no-members:

.. autofunction:: wait

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. automethod:: pybricks.tools.StopWatch.time

    .. automethod:: pybricks.tools.StopWatch.pause

    .. automethod:: pybricks.tools.StopWatch.resume

    .. automethod:: pybricks.tools.StopWatch.reset

.. autoclass:: pybricks.tools.DataLog

.. toggle-header::
    :header: **Show/hide example: Logging and visualizing measurements**

    **Example**

    This example shows how to log the angle of a rotating wheel as time passes.

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/datalog/main.py

    It creates a ``csv`` file on the EV3 brick with the name ``log`` and
    the current date and time. For example, if you
    run this example on 13 February 2020 on 10:07 and 44.431260
    seconds, the file is called ``log_2020_02_13_10_07_44_431260.csv``. In this
    case, it has the following contents::

        time, angle
        3, 0
        108, 6
        212, 30
        316, 71
        419, 124
        523, 176
        628, 228
        734, 281
        838, 333
        942, 385

    The file is created on the EV3 Brick. You can find the file in the ev3dev
    device browser in the bottom left of your Visual Studio Code window. To
    upload it to your computer, right click it and click ``upload``.

    You can open this ``csv`` file with spreadsheet tools such as
    Microsoft Excel, Apple Numbers, or Libreoffice Calc (free). You can then
    further analyse or plot the data. The file can also be opened with most
    text editors.

.. toggle-header::
    :header: **Show/hide example: Using the optional arguments**

    **Example**

    This example shows how to log data beyond just numbers. It also shows how
    you can use the optional arguments of the ``DataLog`` class to choose the
    file name and extension.

    In this example, ``timestamp=False``, which means that the date and time
    are not added to the file name. This can be convenient because the file
    name will always be the same. However, this means that the contents of
    ``my_file.txt`` will be overwritten every time you run this script.

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/datalog/extra.py
