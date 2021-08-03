.. pybricks-requirements::

Power Functions
^^^^^^^^^^^^^^^^^^^^^^^^^

The :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>` can
send infrared signals to control Power Functions infrared receivers. You can
use this technique to control medium, large, extra large, and train
motors. The infrared range is limited to about 30 cm, depending on the angle
and ambient conditions.

.. figure:: ../../main/images/pfmotor.png
   :width: 95 %

   Powered Up
   :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`
   (left), Power Functions infrared receiver (middle), and a Power Functions
   motor (right). Here, the receiver uses channel
   1 with a motor on the red port.

.. autoclass:: pybricks.pupdevices.PFMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks.pupdevices.PFMotor.dc
        :noindex:

    .. automethod:: pybricks.pupdevices.PFMotor.stop
        :noindex:

    .. automethod:: pybricks.pupdevices.PFMotor.brake
        :noindex:

Examples
-------------------

Control a Power Functions motor
*******************************

.. literalinclude::
    ../../../examples/pup/motor_pf/motor_pf_basics.py

Controlling multiple Power Functions motors
*******************************************

.. literalinclude::
    ../../../examples/pup/motor_pf/motor_pf_pwm.py
