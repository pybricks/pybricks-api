.. pybricks-requirements:: stm32-extra

:mod:`usys` -- System specific functions
============================================================

This MicroPython module is a subset of the `sys module`_ in Python.

.. rubric:: Input and output streams

.. module:: usys

.. autodata:: usys.stdin
    :annotation:

.. autodata:: usys.stdout
    :annotation:

.. autodata:: usys.stderr
    :annotation:

.. rubric:: Version info

.. autodata:: implementation
    :annotation:

.. autodata:: version
    :annotation:

.. autodata:: version_info
    :annotation:

Examples
---------------

Version information
*******************************

.. literalinclude::
    ../../../examples/micropython/usys/pybricks_version.py

.. literalinclude::
    ../../../examples/micropython/usys/micropython_version.py

Standard input and output
*******************************

The ``stdin`` stream can be used to capture input via the Pybricks Code
input/output window. See the `keyboard input`_ project to learn how this works.
This approach can be extended to exchange data with any `other device`_ as well.

.. _keyboard input: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/
.. _other device: https://pybricks.com/projects/tutorials/wireless/hub-to-device/

.. _sys module: https://docs.python.org/3.5/library/sys.html
