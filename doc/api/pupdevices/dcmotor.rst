Motors without Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupdcmotors:

.. figure:: ../../api/images/pupdcmotors_label.png
   :width: 70 %
   :alt: pupmotors
   :align: center

   Powered Up motors without rotation sensors. The arrows indicate the default
   positive direction.

.. autoclass:: pybricks.pupdevices.DCMotor
    :no-members:

    .. automethod:: pybricks.pupdevices.DCMotor.dc
        :noindex:

    .. automethod:: pybricks.pupdevices.DCMotor.stop
        :noindex:

    .. automethod:: pybricks.pupdevices.DCMotor.brake
        :noindex:

Examples
-------------------

Making the motor move back and forth
************************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_init_basic.py

Changing the positive direction
*******************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_init_direction.py

Starting and stopping
*********************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_stop.py
