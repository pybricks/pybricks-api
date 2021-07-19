Exceptions and error codes
=====================================================

.. autoclass:: ubuiltins.BaseException

.. autoclass:: ubuiltins.Exception

.. autoclass:: ubuiltins.ArithmeticError

.. autoclass:: ubuiltins.LookupError

.. autoclass:: ubuiltins.AssertionError

.. autoclass:: ubuiltins.AttributeError

.. autoclass:: ubuiltins.EOFError

.. autoclass:: ubuiltins.GeneratorExit

.. autoclass:: ubuiltins.ImportError

.. autoclass:: ubuiltins.IndentationError

.. autoclass:: ubuiltins.IndexError

.. autoclass:: ubuiltins.KeyError

.. autoclass:: ubuiltins.KeyboardInterrupt

.. autoclass:: ubuiltins.MemoryError

.. autoclass:: ubuiltins.NameError

.. autoclass:: ubuiltins.NotImplementedError

.. autoclass:: ubuiltins.OverflowError

.. autoclass:: ubuiltins.RuntimeError

.. autoclass:: ubuiltins.StopIteration

.. autoclass:: ubuiltins.SyntaxError

.. autoclass:: ubuiltins.SystemExit

.. autoclass:: ubuiltins.TypeError

.. autoclass:: ubuiltins.ValueError

.. autoclass:: ubuiltins.ZeroDivisionError

OSError
--------

.. autoclass:: ubuiltins.OSError


.. rubric:: uerrno module

.. module:: uerrno

The ``errno`` attribute of an ``OSError`` indicates why the exception was
raised. It has one of the following values, which can be imported from the
``uerrno`` module:

.. autodata:: uerrno.EAGAIN

.. autodata:: uerrno.EBUSY

.. autodata:: uerrno.ECANCELED

.. autodata:: uerrno.EINVAL

.. autodata:: uerrno.EIO

.. autodata:: uerrno.ENODEV

.. autodata:: uerrno.EOPNOTSUPP

.. autodata:: uerrno.EPERM

.. autodata:: uerrno.ETIMEDOUT

.. autodata:: uerrno.errorcode

Examples
---------------------

Detect devices using ``OSError``
*****************************************

.. literalinclude::
    ../../../examples/micropython/oserror.py
