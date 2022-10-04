.. pybricks-requirements::

Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-remote.png
   :width: 60 %

.. autoclass:: pybricks.pupdevices.Remote
  :no-members:

  .. automethod:: pybricks.pupdevices::Remote.name

  .. automethod:: pybricks.pupdevices::Remote.light.on

  .. automethod:: pybricks.pupdevices::Remote.light.off

  .. automethod:: pybricks.pupdevices::Remote.buttons.pressed

Examples
-------------------

Checking which buttons are pressed
**********************************

.. literalinclude::
    ../../../examples/pup/remote/basics.py

Changing the remote light color
**********************************

.. literalinclude::
    ../../../examples/pup/remote/set_color_basic.py

Changing the light color using the buttons
*******************************************

.. literalinclude::
    ../../../examples/pup/remote/set_color.py


Using the timeout setting
**********************************

You can use the ``timeout`` argument to change for how long the hub searches
for the remote. If you choose ``None``, it will search forever.

.. literalinclude::
    ../../../examples/pup/remote/timeout_none.py


If the remote was not found within the specified ``timeout``,
an :ref:`OSError <OSError>` is raised. You can catch this exception to run
other code if the remote is not available.


.. literalinclude::
    ../../../examples/pup/remote/timeout_exception.py

Changing the name of the remote
*******************************

You can change the Bluetooth name of the remote. The factory default name is
``Handset``.

.. literalinclude::
    ../../../examples/pup/remote/set_name.py

You can specify this name when connecting to the remote.
This lets you pick the right one if multiple remotes are nearby.

.. literalinclude::
    ../../../examples/pup/remote/use_name.py
