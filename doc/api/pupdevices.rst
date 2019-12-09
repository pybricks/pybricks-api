:mod:`pupdevices` -- Powered Up Devices
===========================================================

.. automodule:: pybricks.pupdevices
    :no-members:

Motor
^^^^^^^^^^^^

.. autoclass:: pybricks._instances.Motor
    :noindex:
    :no-members:

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: pybricks._instances.Motor.angle
        :noindex:

    .. automethod:: pybricks._instances.Motor.reset_angle
        :noindex:

    .. automethod:: pybricks._instances.Motor.speed
        :noindex:

    .. automethod:: pybricks._instances.Motor.stop
        :noindex:

    .. automethod:: pybricks._instances.Motor.run
        :noindex:

    .. automethod:: pybricks._instances.Motor.run_time
        :noindex:

    .. automethod:: pybricks._instances.Motor.run_angle
        :noindex:

    .. automethod:: pybricks._instances.Motor.run_target
        :noindex:


Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.rgb

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. automethod:: pybricks._instances.light.on

    .. automethod:: pybricks._instances.light.off


Tilt Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.pupdevices.TiltSensor
    :no-members:

    .. automethod:: neutral

    .. automethod:: acceleration

    .. automethod:: tilt

    .. automethod:: up


Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.pupdevices.RemoteControl
    :no-members:

    .. automethod:: pybricks._instances.light.on

    .. automethod:: pybricks._instances.light.off

    .. automethod:: pybricks._instances.buttons.pressed
