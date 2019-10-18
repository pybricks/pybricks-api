:mod:`pup/nxt/ev3` -- Motors
===========================================

.. _motorclass:

Motor
------

.. autoclass:: pybricks.builtins.Motor
    :no-members:

    Example::

        # Initialize a motor (by default this means is, without any gears).
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, [12, 36])

    .. rubric:: Methods for motors without rotation sensors

    .. automethod:: pybricks.builtins.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: pybricks.builtins.Motor.angle

    .. automethod:: pybricks.builtins.Motor.reset_angle

    .. automethod:: pybricks.builtins.Motor.speed

    .. automethod:: pybricks.builtins.Motor.stop

    .. automethod:: pybricks.builtins.Motor.run

    .. automethod:: pybricks.builtins.Motor.run_time

    .. automethod:: pybricks.builtins.Motor.run_angle

    .. automethod:: pybricks.builtins.Motor.run_target

    .. rubric:: Advanced methods for motors with rotation sensors

    .. automethod:: pybricks.builtins.Motor.track_target

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

    .. automethod:: pybricks.builtins.Motor.stalled

    .. automethod:: pybricks.builtins.Motor.run_until_stalled

    .. automethod:: pybricks.builtins.Motor.set_dc_settings

    .. automethod:: pybricks.builtins.Motor.set_run_settings

        Example::

            # Set the maximum speed to 200 deg/s and
            # acceleration to 400 deg/s/s.
            example_motor.set_run_settings(200, 400)

            # Make the motor run for 5 seconds. Even though the
            # speed argument is 300 deg/s in this example, the
            # motor will move at only 200 deg/s because of
            # the settings above.
            example_motor.run_time(300, 5000)

    .. automethod:: pybricks.builtins.Motor.set_pid_settings

