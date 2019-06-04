:mod:`lpf2devices` -- Power Function 2.0 Motors and Sensors
===========================================================

.. automodule:: lpf2devices
    :no-members:

Motors
------

.. autoclass:: lpf2devices.Motor
    :no-members:

    Example::

        # Initialize a motor (by default this means is, without any gears).
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, [12, 36])

    .. rubric:: Methods for motors without rotation sensors

    .. automethod:: lpf2devices.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: lpf2devices.Motor.angle

    .. automethod:: lpf2devices.Motor.reset_angle

    .. automethod:: lpf2devices.Motor.speed

    .. automethod:: lpf2devices.Motor.stop

    .. automethod:: lpf2devices.Motor.run

    .. automethod:: lpf2devices.Motor.run_time

    .. automethod:: lpf2devices.Motor.run_angle

    .. automethod:: lpf2devices.Motor.run_target

    .. rubric:: Advanced methods for motors with rotation sensors

    .. automethod:: lpf2devices.Motor.track_target

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

    .. automethod:: lpf2devices.Motor.stalled

    .. automethod:: lpf2devices.Motor.run_until_stalled

    .. automethod:: lpf2devices.Motor.set_dc_settings

    .. automethod:: lpf2devices.Motor.set_run_settings

        Example::

            # Set the maximum speed to 200 deg/s and
            # acceleration to 400 deg/s/s.
            example_motor.set_run_settings(200, 400)

            # Make the motor run for 5 seconds. Even though the
            # speed argument is 300 deg/s in this example, the
            # motor will move at only 200 deg/s because of
            # the settings above.
            example_motor.run_time(300, 5000)

    .. automethod:: lpf2devices.Motor.set_pid_settings

Sensors
-------

Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: lpf2devices.ColorDistanceSensor
