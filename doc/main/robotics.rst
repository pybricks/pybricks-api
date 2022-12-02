.. pybricks-requirements::

:mod:`robotics <pybricks.robotics>` -- Robotics
======================================================

.. automodule:: pybricks.robotics
    :no-members:


.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: Driving by a given distance or angle

    Use the following commands to drive a given distance, or turn by a
    given angle.

    This is measured using the internal rotation sensors. Because wheels may
    slip while moving, the traveled distance and angle are only estimates.

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. automethod:: pybricks.robotics.DriveBase.curve

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. automethod:: pybricks.robotics.DriveBase.done

    .. rubric:: Drive forever

    Use :meth:`.drive` to begin driving at a desired speed and steering.

    It keeps going until you use :meth:`.stop` or change course by
    using :meth:`.drive` again. For example, you can drive until a
    sensor is triggered and then stop or turn around.

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. rubric:: Measuring

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. automethod:: pybricks.robotics.DriveBase.state

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. automethod:: pybricks.robotics.DriveBase.stalled

    .. rubric:: Measuring and validating the robot dimensions

    As a first estimate, you can measure the ``wheel_diameter`` and the
    ``axle_track`` with a ruler. Because it is hard to see where the wheels
    effectively touch the ground, you can estimate the ``axle_track`` as
    the distance between the midpoint of the wheels.

    In practice, most wheels compress slightly under the weight of your robot.
    To verify, make your robot drive 1000 mm using ``my_robot.straight(1000)``
    and measure how far it really traveled. Compensate as follows:

        - If your robot drives **not far enough**, **decrease** the
          ``wheel_diameter`` value slightly.
        - If your robot drives **too far**, **increase** the
          ``wheel_diameter`` value slightly.

    Motor shafts and axles bend slightly under the load of the
    robot, causing the ground contact point of the wheels to be closer to the
    midpoint of your robot. To verify, make your robot turn 360 degrees
    using ``my_robot.turn(360)`` and check that it is back in the same place:

        - If your robot turns **not far enough**, **increase** the
          ``axle_track`` value slightly.
        - If your robot turns **too far**, **decrease** the ``axle_track``
          value slightly.

    When making these adjustments, always adjust the
    ``wheel_diameter`` first, as done above. Be sure to test both turning
    and driving straight after you are done.

    .. rubric:: Using the DriveBase motors individually

    After creating a :class:`.DriveBase` object, you can still use its two
    motors individually. If you start one motor, the other motor will
    automatically stop. Likewise, if a motor is already running and you make
    the drive base move, the original maneuver is cancelled and the drive base
    will take over.

    .. rubric:: Advanced settings

    The :meth:`.settings` method is used to adjust commonly used settings like
    the default speed and acceleration for straight maneuvers and turns.
    Use the following attributes to adjust more advanced control settings.

    You can only change the settings while the robot is stopped. This is
    either before you begin driving or after you call :meth:`.stop`.

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:

    .. versionchanged:: 3.2

        The :meth:`done` and :meth:`stalled` methods have been moved.

Examples
-------------------

Driving straight and turning in place
**********************************************

.. literalinclude::
    ../../examples/pup/robotics/drivebase_basics.py
