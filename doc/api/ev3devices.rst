:mod:`ev3devices` -- EV3 Devices
===========================================

.. automodule:: pybricks.ev3devices
    :no-members:

Motor
^^^^^^^^^^^^

.. autoclass:: pybricks._instances.Motor
    :noindex:
    :no-members:

    Example::

        # Initialize a motor.
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

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


Touch Sensor
^^^^^^^^^^^^
.. autoclass:: pybricks.ev3devices.TouchSensor

Color Sensor
^^^^^^^^^^^^
.. autoclass:: pybricks.ev3devices.ColorSensor

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.ev3devices.InfraredSensor

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.ev3devices.UltrasonicSensor

Gyroscopic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.ev3devices.GyroSensor
