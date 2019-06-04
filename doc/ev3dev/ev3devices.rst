:mod:`ev3devices` -- EV3 Motors and Sensors
===========================================

.. automodule:: ev3devices
    :no-members:

Motors
------

.. autoclass:: ev3devices.Motor
    :no-members:

    Example::

        # Initialize a motor (by default this means is, without any gears).
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, [12, 36])

    .. rubric:: Methods for motors without rotation sensors

    .. automethod:: ev3devices.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: ev3devices.Motor.angle

    .. automethod:: ev3devices.Motor.reset_angle

    .. automethod:: ev3devices.Motor.speed

    .. automethod:: ev3devices.Motor.stop

    .. automethod:: ev3devices.Motor.run

    .. automethod:: ev3devices.Motor.run_time

    .. automethod:: ev3devices.Motor.run_angle

    .. automethod:: ev3devices.Motor.run_target

    .. rubric:: Advanced methods for motors with rotation sensors

    .. automethod:: ev3devices.Motor.track_target

        Example::

            # Initialize motor and timer
            from math import sin
            motor = Motor(Port.A)
            watch = StopWatch()
            amplitude = 90

            # In a fast loop, compute a reference angle
            # and make the motor track it.
            while True:
                # Get the time in seconds
                seconds = watch.time()/1000
                # Compute a reference angle. This produces
                # a sine wave that makes the motor move
                # smoothly between -90 and +90 degrees.
                angle_now = sin(seconds)*amplitude
                # Make the motor track the given angle
                motor.track_target(angle_now)

    .. automethod:: ev3devices.Motor.stalled

    .. automethod:: ev3devices.Motor.run_until_stalled

    .. automethod:: ev3devices.Motor.set_dc_settings

    .. automethod:: ev3devices.Motor.set_run_settings

        Example::

            # Set the maximum speed to 200 deg/s and
            # acceleration to 400 deg/s/s.
            example_motor.set_run_settings(200, 400)

            # Make the motor run for 5 seconds. Even though the
            # speed argument is 300 deg/s in this example, the
            # motor will move at only 200 deg/s because of
            # the settings above.
            example_motor.run_time(300, 5000)

    .. automethod:: ev3devices.Motor.set_pid_settings

Sensors
-------

Touch Sensor
^^^^^^^^^^^^
.. autoclass:: ev3devices.TouchSensor

Color Sensor
^^^^^^^^^^^^
.. autoclass:: ev3devices.ColorSensor

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices.InfraredSensor

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices.UltrasonicSensor

Gyroscopic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices.GyroSensor
