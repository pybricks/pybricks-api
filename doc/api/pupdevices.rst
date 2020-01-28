:mod:`pupdevices <pybricks.pupdevices>` -- Powered Up Devices
=============================================================

.. automodule:: pybricks.pupdevices
    :no-members:

Motors without Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.builtins.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks.builtins.DCMotor.dc
        :noindex:

Motors with Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.pupdevices.Motor
    :noindex:
    :no-members:

    .. rubric:: Measuring

    .. automethod:: pybricks.pupdevices.Motor.speed

    .. automethod:: pybricks.pupdevices.Motor.angle

    .. automethod:: pybricks.pupdevices.Motor.reset_angle

    .. automethod:: pybricks.pupdevices.Motor.stalled

    .. rubric:: Action

    .. automethod:: pybricks.pupdevices.Motor.stop

    .. automethod:: pybricks.pupdevices.Motor.run

    .. automethod:: pybricks.pupdevices.Motor.run_time

    .. automethod:: pybricks.pupdevices.Motor.run_angle

    .. automethod:: pybricks.pupdevices.Motor.run_target

    .. automethod:: pybricks.pupdevices.Motor.run_until_stalled

    .. automethod:: pybricks.pupdevices.Motor.dc

    .. rubric:: Advanced motion control

    .. automethod:: pybricks.pupdevices.Motor.track_target

    .. autoattribute:: pybricks.pupdevices.Motor.control
        :annotation:


Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.off


.. Tilt Sensor
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. autoclass:: pybricks.pupdevices.TiltSensor
    :no-members:

    .. automethod:: neutral

    .. automethod:: acceleration

    .. automethod:: tilt

    .. automethod:: up


.. Remote Control
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. autoclass:: pybricks.pupdevices.RemoteControl
    :no-members:

    .. automethod:: pybricks.pupdevices::RemoteControl.light.on

    .. automethod:: pybricks.pupdevices::RemoteControl.light.off

    .. automethod:: pybricks.pupdevices::RemoteControl.buttons.pressed
