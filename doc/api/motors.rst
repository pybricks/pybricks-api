More about Motors
===========================================

The Motor Class
^^^^^^^^^^^^^^^

.. autoclass:: pybricks.builtins.Motor
    :no-members:

    Example::

        # Initialize a motor with default settings.
        example_motor = Motor(Port.A)

        # Initialize a motor with positive speed as counterclockwise.
        right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # Initialize a motor with a gear train, consisting of a 12-tooth gear
        # and a 36-tooth gear. This normally slows down your output axle by a
        # factor 3. But when you specify gears like this, the motor will
        # compensate for them. For example, `robot_arm.run_angle(200, 90)` will
        # now make the motor move faster and farther so that your output axle
        # will still turn at the desired 200 deg/s for 90 degrees.
        robot_arm = Motor(Port.C, Direction.CLOCKWISE, gears=[12, 36])

    .. rubric:: Measuring

    .. automethod:: pybricks.builtins.Motor.speed

    .. automethod:: pybricks.builtins.Motor.angle

    .. automethod:: pybricks.builtins.Motor.reset_angle

    .. automethod:: pybricks.builtins.Motor.stalled

    .. rubric:: Moving the motor

    .. automethod:: pybricks.builtins.Motor.stop

    .. automethod:: pybricks.builtins.Motor.run

    .. automethod:: pybricks.builtins.Motor.run_time

    .. automethod:: pybricks.builtins.Motor.run_angle

    .. automethod:: pybricks.builtins.Motor.run_target

    .. automethod:: pybricks.builtins.Motor.dc

        Example::

            # Set the motor duty cycle to 75%.
            example_motor.duty(75)

    .. rubric:: Moving the motor (advanced)

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

    .. automethod:: pybricks.builtins.Motor.run_until_stalled

    .. rubric:: Changing motor settings

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

    .. automethod:: pybricks.builtins.Motor.set_dc_settings

    .. automethod:: pybricks.builtins.Motor.set_pid_settings


Motor Tips & Tricks
^^^^^^^^^^^^^^^^^^^

The difference between ``run_angle`` and ``run_target``
-------------------------------------------------------

*TODO*

.. _stalled:

Using stall detection
---------------------

When a motor cannot move any further despite using the maximally allowed torque
we say that the motor is stalled. Something could be blocking the motor, or the
load is just too heavy. For example, if you manually hold the motor shaft still
while the motor is busy executing a command, the motor will stall.

What can I do with stall detection?
+++++++++++++++++++++++++++++++++++

Stall detection is useful to detect that a motor can't move any further. This
can be used to detect an endpoint of a mechanism. For example, you can detect
whether a robotic hand is fully closed, because the gripper motor simply can't
go further. This way, you don't need a touch or light sensor to detect this.

*TODO: How, what, why. Also explain run_until_stalled. Rack & pinion example.*

When is a motor stalled?
++++++++++++++++++++++++

When the motor is stalled, the :meth:`.stalled` will return ``True``.
Specifically, the motor is stalled when the duty cycle computed by the
PID controllers has reached the maximum (so ``duty`` = ``duty_limit``)
and still the motor cannot reach a minimal speed
(so ``speed`` < ``stall_speed``) for a period of at
least ``stall_time``.

You can change the ``duty_limit``, ``stall_speed``, and ``stall_time``
settings using  and :meth:`.set_pid_settings`
in order to change the sensitivity to being stalled.

.. _gears:

Using gears
-----------------
Many LEGO robots use mechanisms with gears to change the speed and torque
output of a motor. Let's consider the following dial mechanism.

*TODO: INSERT PICTURE OF MOTOR WITH 12z gear AND 36z gear.*

This gear train slows down the dial on the output axle by a factor of 3.
Therefore, if you want to rotate the dial by 90 degrees, the motor has to
rotate by 270 degrees. To turn at 200 degrees per second, the motor has to
turn at 600 degrees per second, and so on.

To avoid using this factor 3 everywhere in your program, you can use the
`gears` setting of the :class:`.Motor` object, as shown in this example::

    # This example uses the EV3 brick, but the same
    # technique applies to other programmable hubs.
    ev3 = EV3Brick()

    # Initialize the motor. See picture above.
    dial = Motor(ev3.Port.C, Direction.COUNTERCLOCKWISE, gears=[12, 36])

    # Turn the dial by 90-degrees
    dial.run_angle(500, 90)

    # Print the dial angle
    print(dial.angle())

    # Turn the dial back to the original position
    dial.run_target(500, 0)

When you use any of the other methods, the same scaling is applied. For
example, you can print the angle of the dial as shown above. This will print
90 (approximately), even though the motor has turned 270 degrees.

Notice that there is no magic going on. It is just a convenient scaling
function. This helps you organize your code. For example, if you change
your mechanism to use different gears, you only have to change the first line
of this example.
