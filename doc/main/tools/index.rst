.. pybricks-requirements::

:mod:`tools <pybricks.tools>` -- General purpose tools
========================================================

.. automodule:: pybricks.tools
    :no-members:

Timing tools
---------------

.. blockimg:: pybricks_blockWaitTime

.. autofunction:: wait

.. blockimg:: pybricks_variables_set_stopwatch

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. blockimg:: pybricks_blockStopWatchTime

    .. automethod:: pybricks.tools.StopWatch.time

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_pause

    .. automethod:: pybricks.tools.StopWatch.pause

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_resume

    .. automethod:: pybricks.tools.StopWatch.resume

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_reset

    .. automethod:: pybricks.tools.StopWatch.reset

Input tools
-----------

.. autofunction:: pybricks.tools.read_input_byte

.. pybricks-requirements:: light-matrix

.. autofunction:: pybricks.tools.hub_menu

.. literalinclude::
    ../../../examples/pup/tools/hub_menu.py

Linear algebra tools
--------------------

.. versionchanged:: 3.3

    These tools were previously located in the ``pybricks.geometry`` module.

.. pybricks-requirements:: stm32-float

.. autoclass:: pybricks.tools.Matrix
    :no-members:

    .. autoattribute:: pybricks.tools::Matrix.T

    .. autoattribute:: pybricks.tools::Matrix.shape

.. pybricks-requirements:: stm32-float

.. blockimg:: pybricks_blockVector

.. autofunction:: pybricks.tools.vector

.. autofunction:: pybricks.tools.cross

Multitasking
--------------------

.. versionadded:: 3.3

Pybricks supports cooperative multitasking using the ``async`` and ``await``
keywords. This allows operations that normally take some time to complete to
run in parallel with other operations.

.. blockimg:: pybricks_blockMultiTask

.. autofunction:: pybricks.tools.multitask

.. autofunction:: pybricks.tools.run_task

The following example shows how to use multitasking to make a robot drive
forward, then turn and move a gripper at the same time, and then drive
backward.

.. literalinclude::
    ../../../examples/pup/robotics/drivebase_async.py

.. class:: coroutine

.. class:: await

Whenever you see a function or method prefixed by ``await``, this means that
it supports multitasking. When running a coroutine with ``run_task``, all
methods and functions prefixed by ``await`` will act as coroutines.

If you don't use multitasking, you can ignore the ``await`` keyword and write
programs as usual. Specifically, when ``run_task`` is not used, functions
prefixed by ``await`` will act as normal functions.
