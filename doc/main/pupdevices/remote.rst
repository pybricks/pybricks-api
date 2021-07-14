Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/images/pupremote.png
   :width: 60 %

.. autoclass:: pybricks.pupdevices.Remote
  :no-members:

  .. autoattribute:: pybricks.pupdevices::Remote.address
       :annotation:

  .. automethod:: pybricks.pupdevices::Remote.light.on

  .. automethod:: pybricks.pupdevices::Remote.light.off

  .. automethod:: pybricks.pupdevices::Remote.buttons.pressed

.. note::

    The ``light`` and ``address`` features are not yet supported.

Examples
-------------------

Check which buttons are pressed
*******************************

.. literalinclude::
    ../../../examples/pup/remote/basics.py
