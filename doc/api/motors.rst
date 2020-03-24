More about Motors
===========================================

Motor Tips & Tricks
^^^^^^^^^^^^^^^^^^^

.. The difference between ``run_angle`` and ``run_target``
.. -------------------------------------------------------

.. *TODO*

.. _absangles:

Absolute angles
----------------------------

.. todo::

    This section will be included in a future release.

.. _stalled:

Using stall detection
---------------------

.. todo::

    This section will be included in a future release.

.. When a motor cannot move any further despite using the maximally allowed
.. torque we say that the motor is stalled. Something could be blocking the
.. motor, or the load is just too heavy. For example, if you manually hold
.. the motor shaft still while the motor is busy executing a command, the
.. motor will stall.

.. What can I do with stall detection?
.. +++++++++++++++++++++++++++++++++++

.. Stall detection is useful to detect that a motor can't move any further.
.. This can be used to detect an endpoint of a mechanism. For example, you
.. can detect whether a robotic hand is fully closed, because the gripper
.. motor simply can't go further. This way, you don't need a touch or light
.. sensor to detect this.

.. *TODO: How, what, why. Explain run_until_stalled. Rack & pinion example.*

.. When is a motor stalled?
.. ++++++++++++++++++++++++

.. TODO

.. _gears:

Using gears
-----------------

.. todo::

    This section will be included in a future release.

.. Many LEGO robots use mechanisms with gears to change the speed and torque
.. output of a motor. Let's consider the following dial mechanism.

.. *TODO: INSERT PICTURE OF MOTOR WITH 12z gear AND 36z gear.*

.. This gear train slows down the dial on the output axle by a factor of 3.
.. Therefore, if you want to rotate the dial by 90 degrees, the motor has to
.. rotate by 270 degrees. To turn at 200 degrees per second, the motor has to
.. turn at 600 degrees per second, and so on.

.. To avoid using this factor 3 everywhere in your program, you can use the
.. `gears` setting of the ``Motor`` object, as shown in this example::

..     # This example uses the EV3 brick, but the same
..     # technique applies to other programmable hubs.
..     ev3 = EV3Brick()

..     # Initialize the motor. See picture above.
..     dial = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[12, 36])

..     # Turn the dial by 90-degrees
..     dial.run_angle(500, 90)

..     # Print the dial angle
..     print(dial.angle())

..     # Turn the dial back to the original position
..     dial.run_target(500, 0)

.. When you use any of the other methods, the same scaling is applied. For
.. example, you can print the angle of the dial as shown above. This will print
.. 90 (approximately), even though the motor has turned 270 degrees.

.. Notice that there is no magic going on. It is just a convenient scaling
.. function. This helps you organize your code. For example, if you change
.. your mechanism to use different gears, you only have to change the first
.. line of this example.

.. _control:

The Control Class
^^^^^^^^^^^^^^^^^

The ``Motor`` class uses PID control to accurately track your commanded target
angles. Similarly, the ``DriveBase`` class uses two of such controllers:
one to control the heading and one to control the traveled distance.

You can change the control settings through the following attributes, which are
instances of the ``Control`` class given below.:

    - ``Motor.control``
    - ``DriveBase.heading_control``
    - ``DriveBase.distance_control``

You can only change the settings while the controller is stopped. For example,
you can set the settings at the beginning of your program. Alternatively, first
call ``stop()`` to make your ``Motor`` or ``DriveBase`` stop, and then change
the settings.

.. autoclass:: pybricks.builtins.Control
    :no-members:

    .. rubric:: Status

    .. automethod:: pybricks.builtins.Control.done

    .. automethod:: pybricks.builtins.Control.stalled

    .. rubric:: Settings

    .. automethod:: pybricks.builtins.Control.limits

    .. automethod:: pybricks.builtins.Control.pid

    .. automethod:: pybricks.builtins.Control.target_tolerances

    .. automethod:: pybricks.builtins.Control.stall_tolerances
