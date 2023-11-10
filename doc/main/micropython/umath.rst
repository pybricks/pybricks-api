.. pybricks-requirements:: stm32-extra stm32-float

:mod:`umath <umath>` -- Math functions
============================================================

.. module:: umath

This MicroPython module is similar to the `math module`_ in Python.

See also the :ref:`built-in math functions<builtinmath>` that can be used
without importing anything.

Rounding and sign
-------------------------------------

.. blockimg:: pybricks_blockMathOp_roundup

.. autofunction:: umath.ceil

.. blockimg:: pybricks_blockMathOp_rounddown

.. autofunction:: umath.floor

.. autofunction:: umath.trunc

.. autofunction:: umath.fmod

.. autofunction:: umath.fabs

.. autofunction:: umath.copysign

Powers and logarithms
-------------------------------

.. autodata:: umath.e

.. blockimg:: pybricks_blockMathOp_exp

.. autofunction:: umath.exp

.. blockimg:: pybricks_blockMathArithmetic_power

.. blockimg:: pybricks_blockMathOp_pow10

.. autofunction:: umath.pow

.. blockimg:: pybricks_blockMathOp_ln

.. autofunction:: umath.log

.. blockimg:: pybricks_blockMathOp_root

.. autofunction:: umath.sqrt

Trigonometry
-------------------------------

.. autodata:: umath.pi

.. autofunction:: umath.degrees

.. autofunction:: umath.radians

.. blockimg:: pybricks_blockMathOp_sin

.. autofunction:: umath.sin

.. blockimg:: pybricks_blockMathOp_asin

.. autofunction:: umath.asin

.. blockimg:: pybricks_blockMathOp_cos

.. autofunction:: umath.cos

.. blockimg:: pybricks_blockMathOp_acos

.. autofunction:: umath.acos

.. blockimg:: pybricks_blockMathOp_tan

.. autofunction:: umath.tan

.. blockimg:: pybricks_blockMathOp_atan

.. autofunction:: umath.atan

.. blockimg:: pybricks_blockMathOp_atan2

.. autofunction:: umath.atan2

Other math functions
-------------------------------

.. autofunction:: umath.isfinite

.. autofunction:: umath.isinfinite

.. autofunction:: umath.isnan

.. autofunction:: umath.modf

.. autofunction:: umath.frexp

.. autofunction:: umath.ldexp

.. _math module: https://docs.python.org/3.5/library/math.html#module-math
