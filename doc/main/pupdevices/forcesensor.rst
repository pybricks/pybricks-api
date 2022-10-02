.. pybricks-requirements::

Force Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-force.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.ForceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ForceSensor.force

    .. automethod:: pybricks.pupdevices.ForceSensor.distance

    .. automethod:: pybricks.pupdevices.ForceSensor.pressed

    .. automethod:: pybricks.pupdevices.ForceSensor.touched

Examples
-------------------

Measuring force and movement
****************************

.. literalinclude::
    ../../../examples/pup/sensor_force/basics.py

Measuring peak force
********************

.. literalinclude::
    ../../../examples/pup/sensor_force/peak.py
