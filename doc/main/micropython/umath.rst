.. pybricks-requirements:: stm32-extra stm32-float

:mod:`umath <umath>` -- Math functions
============================================================

.. module:: umath

This MicroPython module is similar to the `math module`_ in Python.

See also the :ref:`built-in math functions<builtinmath>` that can be used
without importing anything.

Rounding and sign
-------------------------------------

.. autofunction:: umath.ceil

.. autofunction:: umath.floor

.. autofunction:: umath.trunc

.. autofunction:: umath.fmod

.. autofunction:: umath.fabs

.. autofunction:: umath.copysign

Powers and logarithms
-------------------------------

.. autodata:: umath.e

.. autofunction:: umath.exp

.. autofunction:: umath.pow

.. autofunction:: umath.log

.. autofunction:: umath.sqrt

Trigonometry
-------------------------------

.. autodata:: umath.pi

.. autofunction:: umath.degrees

.. autofunction:: umath.radians

.. autofunction:: umath.sin

.. autofunction:: umath.asin

.. autofunction:: umath.cos

.. autofunction:: umath.acos

.. autofunction:: umath.tan

.. autofunction:: umath.atan

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
