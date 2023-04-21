.. pybricks-requirements::

:mod:`tools <pybricks.tools>` -- General purpose tools
========================================================

.. automodule:: pybricks.tools
    :no-members:

Timing tools
---------------

.. autofunction:: wait

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. automethod:: pybricks.tools.StopWatch.time

    .. automethod:: pybricks.tools.StopWatch.pause

    .. automethod:: pybricks.tools.StopWatch.resume

    .. automethod:: pybricks.tools.StopWatch.reset

Linear algebra tools
--------------------

.. pybricks-requirements:: stm32-float

.. autoclass:: pybricks.tools.Matrix
    :no-members:

    .. autoattribute:: pybricks.tools::Matrix.T

    .. autoattribute:: pybricks.tools::Matrix.shape

.. pybricks-requirements:: stm32-float

.. autofunction:: pybricks.tools.vector

.. autofunction:: pybricks.tools.cross
