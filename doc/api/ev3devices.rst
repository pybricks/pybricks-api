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

        # Initialize a motor (by default this means is, without any gears).
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, [12, 36])

    .. rubric:: Methods for motors without rotation sensors

    .. automethod:: pybricks.ev3devices.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: pybricks.ev3devices.Motor.angle

    .. automethod:: pybricks.ev3devices.Motor.reset_angle

    .. automethod:: pybricks.ev3devices.Motor.speed

    .. automethod:: pybricks.ev3devices.Motor.stop

    .. automethod:: pybricks.ev3devices.Motor.run

    .. automethod:: pybricks.ev3devices.Motor.run_time

    .. automethod:: pybricks.ev3devices.Motor.run_angle

    .. automethod:: pybricks.ev3devices.Motor.run_target


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

Analog Sensor
^^^^^^^^^^^^^
.. autoclass:: pybricks.ev3devices.AnalogSensor
