Motors without Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupdcmotors:

.. figure:: ../../api/images/pupdcmotors_label.png
   :width: 70 %
   :alt: pupmotors
   :align: center

   Powered Up motors without rotation sensors. The arrows indicate the default
   positive direction.

.. toggle-header::
    :header: **Show/hide examples**

    **Example 1: Making the motor move back and forth**

    .. literalinclude::
        ../../../examples/pup/motor_dc/motor_dc_init_basic.py

    **Example 2: Setting the positive direction as counterclockwise**

    .. literalinclude::
        ../../../examples/pup/motor_dc/motor_dc_init_direction.py

    **Example 3: Starting and stopping**

    .. literalinclude::
        ../../../examples/pup/motor_dc/motor_dc_stop.py

.. autoclass:: pybricks._common.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks._common.DCMotor.dc
        :noindex:

    .. automethod:: pybricks._common.DCMotor.stop
        :noindex:

    .. automethod:: pybricks._common.DCMotor.brake
        :noindex:
