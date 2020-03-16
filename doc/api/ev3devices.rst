:mod:`ev3devices <pybricks.ev3devices>` -- EV3 Devices
======================================================

.. automodule:: pybricks.ev3devices
    :no-members:

Motor
^^^^^^^^^^^^

.. autoclass:: pybricks.ev3devices.Motor
    :no-members:

    .. rubric:: Measuring

    .. automethod:: pybricks.ev3devices.Motor.speed

    .. automethod:: pybricks.ev3devices.Motor.angle

    .. automethod:: pybricks.ev3devices.Motor.reset_angle

    .. rubric:: Stopping

    .. automethod:: pybricks.ev3devices.Motor.stop

    .. automethod:: pybricks.ev3devices.Motor.brake

    .. automethod:: pybricks.ev3devices.Motor.hold

    .. rubric:: Action

    .. automethod:: pybricks.ev3devices.Motor.run

    .. automethod:: pybricks.ev3devices.Motor.run_time

    .. automethod:: pybricks.ev3devices.Motor.run_angle

    .. automethod:: pybricks.ev3devices.Motor.run_target

    .. automethod:: pybricks.ev3devices.Motor.run_until_stalled

    .. automethod:: pybricks.ev3devices.Motor.dc

    .. rubric:: Advanced motion control

    .. automethod:: pybricks.ev3devices.Motor.track_target

    .. autoattribute:: pybricks.ev3devices.Motor.control
        :annotation:


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
