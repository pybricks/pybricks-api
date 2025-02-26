.. pybricks-requirements:: stm32-extra

:mod:`micropython` -- MicroPython internals
===========================================

.. automodule:: micropython
    :no-members:

.. autofunction:: micropython.const

.. autofunction:: micropython.heap_lock

.. autofunction:: micropython.heap_unlock

.. autofunction:: micropython.kbd_intr

.. autofunction:: micropython.mem_info

.. autofunction:: micropython.opt_level

.. autofunction:: micropython.qstr_info

.. autofunction:: micropython.stack_use


Examples
---------------------

Using constants for efficiency
******************************

.. translated-literalinclude::
    ../../../examples/micropython/const.py

Checking free RAM
******************************

.. translated-literalinclude::
    ../../../examples/micropython/memuse.py

This prints information in the format shown below. In this example for the
SPIKE Prime Hub, there are 257696 bytes (251 KB) worth of memory remaining for
the variables in your code. ::

    stack: 372 out of 40184
    GC: total: 258048, used: 352, free: 257696
    No. of 1-blocks: 4, 2-blocks: 2, max blk sz: 8, max free sz: 16103


Handling keyboard interrupts
******************************

.. translated-literalinclude::
    ../../../examples/micropython/keyboard_interrupt.py

Getting more memory statistics
******************************

.. translated-literalinclude::
    ../../../examples/micropython/memstat.py
