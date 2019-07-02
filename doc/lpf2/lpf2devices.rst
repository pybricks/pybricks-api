:mod:`lpf2devices` -- Power Function 2.0 Motors and Sensors
===========================================================

.. automodule:: pybricks.lpf2devices
    :no-members:

Motors
------

.. autoclass:: pybricks.lpf2devices.Motor
    :no-members:

    Example::

        # Initialize a motor (by default this means is, without any gears).
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, [12, 36])

    .. rubric:: Methods for motors without rotation sensors

    .. automethod:: pybricks.lpf2devices.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Methods for motors with rotation sensors

    .. automethod:: pybricks.lpf2devices.Motor.angle

    .. automethod:: pybricks.lpf2devices.Motor.reset_angle

    .. automethod:: pybricks.lpf2devices.Motor.speed

    .. automethod:: pybricks.lpf2devices.Motor.stop

    .. automethod:: pybricks.lpf2devices.Motor.run

    .. automethod:: pybricks.lpf2devices.Motor.run_time

    .. automethod:: pybricks.lpf2devices.Motor.run_angle

    .. automethod:: pybricks.lpf2devices.Motor.run_target

    .. rubric:: Advanced methods for motors with rotation sensors

    .. automethod:: pybricks.lpf2devices.Motor.track_target

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

    .. automethod:: pybricks.lpf2devices.Motor.stalled

    .. automethod:: pybricks.lpf2devices.Motor.run_until_stalled

    .. automethod:: pybricks.lpf2devices.Motor.set_dc_settings

    .. automethod:: pybricks.lpf2devices.Motor.set_run_settings

        Example::

            # Set the maximum speed to 200 deg/s and
            # acceleration to 400 deg/s/s.
            example_motor.set_run_settings(200, 400)

            # Make the motor run for 5 seconds. Even though the
            # speed argument is 300 deg/s in this example, the
            # motor will move at only 200 deg/s because of
            # the settings above.
            example_motor.run_time(300, 5000)

    .. automethod:: pybricks.lpf2devices.Motor.set_pid_settings

Sensors
-------

Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.lpf2devices.ColorDistanceSensor
    :no-members:

    .. automethod:: pybricks.lpf2devices.ColorDistanceSensor.color

    .. automethod:: pybricks.lpf2devices.ColorDistanceSensor.ambient

    .. automethod:: pybricks.lpf2devices.ColorDistanceSensor.reflection

    .. automethod:: pybricks.lpf2devices.ColorDistanceSensor.rgb

    .. automethod:: pybricks.lpf2devices.ColorDistanceSensor.distance

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. automethod:: pybricks._common.light.on

    .. automethod:: pybricks._common.light.off


Tilt Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.lpf2devices.TiltSensor
    :no-members:

    .. automethod:: acceleration

Other Devices
---------------

Remote Control
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.lpf2devices.RemoteControl
    :no-members:

    .. automethod:: pybricks._common.light.on

    .. automethod:: pybricks._common.light.off

    .. automethod:: pybricks._common.buttons.pressed
