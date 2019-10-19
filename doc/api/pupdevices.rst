:mod:`pupdevices` -- Powered Up Devices
===========================================================

.. automodule:: pybricks.pupdevices
    :no-members:

Motor
^^^^^^^^^^^^

.. autoclass:: pybricks.pupdevices.Motor
    :no-members:

    Example::

        # Initialize a motor (by default this means is, without any gears).
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, [12, 36])

    .. rubric:: Methods for motors without rotation sensors

    .. automethod:: pybricks.pupdevices.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: pybricks.pupdevices.Motor.angle

    .. automethod:: pybricks.pupdevices.Motor.reset_angle

    .. automethod:: pybricks.pupdevices.Motor.speed

    .. automethod:: pybricks.pupdevices.Motor.stop

    .. automethod:: pybricks.pupdevices.Motor.run

    .. automethod:: pybricks.pupdevices.Motor.run_time

    .. automethod:: pybricks.pupdevices.Motor.run_angle

    .. automethod:: pybricks.pupdevices.Motor.run_target

    .. rubric:: Advanced methods for motors with rotation sensors

    .. automethod:: pybricks.pupdevices.Motor.track_target

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

    .. automethod:: pybricks.pupdevices.Motor.stalled

    .. automethod:: pybricks.pupdevices.Motor.run_until_stalled

    .. automethod:: pybricks.pupdevices.Motor.set_dc_settings

    .. automethod:: pybricks.pupdevices.Motor.set_run_settings

        Example::

            # Set the maximum speed to 200 deg/s and
            # acceleration to 400 deg/s/s.
            example_motor.set_run_settings(200, 400)

            # Make the motor run for 5 seconds. Even though the
            # speed argument is 300 deg/s in this example, the
            # motor will move at only 200 deg/s because of
            # the settings above.
            example_motor.run_time(300, 5000)

    .. automethod:: pybricks.pupdevices.Motor.set_pid_settings

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
