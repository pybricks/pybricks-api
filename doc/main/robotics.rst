:mod:`robotics <pybricks.robotics>` -- Robotics and drive bases
===============================================================

.. automodule:: pybricks.robotics
    :no-members:

.. pybricks-requirements::

.. blockimg:: pybricks_variables_set_drive_base

.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: Driving by a given distance or angle

    Use the following commands to drive a given distance, or turn by a
    given angle.

    This is measured using the internal rotation sensors. Because wheels may
    slip while moving, the traveled distance and angle are only estimates.

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_straight

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_turn

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_curve

    .. automethod:: pybricks.robotics.DriveBase.curve

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_straight_speed

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_straight_acceleration

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_turn_rate

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_turn_acceleration

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. automethod:: pybricks.robotics.DriveBase.done

    .. rubric:: Drive forever

    Use :meth:`.drive` to begin driving at a desired speed and steering.

    It keeps going until you use :meth:`.stop` or change course by
    using :meth:`.drive` again. For example, you can drive until a
    sensor is triggered and then stop or turn around.

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_forever

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. blockimg:: pybricks_blockDriveBaseStop_coast

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. blockimg:: pybricks_blockDriveBaseStop_brake

    .. automethod:: pybricks.robotics.DriveBase.brake

    .. blockimg:: pybricks_blockDriveBaseStop_hold

    .. rubric:: Measuring

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_distance

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_angle

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_speed

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_turn_rate

    .. automethod:: pybricks.robotics.DriveBase.state

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. automethod:: pybricks.robotics.DriveBase.stalled

    .. pybricks-requirements:: gyro

    .. rubric:: Driving with the gyro

    .. blockimg:: pybricks_blockDriveBaseUseGyro

    .. automethod:: pybricks.robotics.DriveBase.use_gyro

    If your hub is not mounted flat in your robot, make sure to specify
    the ``top_side`` and ``front_side`` parameters when you initialize the
    :class:`PrimeHub() <pybricks.hubs.PrimeHub>`,
    :class:`InventorHub() <pybricks.hubs.PrimeHub>`,
    :class:`EssentialHub() <pybricks.hubs.EssentialHub>`, or
    :class:`TechnicHub() <pybricks.hubs.TechnicHub>`. This way your robot
    knows which rotation to measure when turning.

    The gyro in each hub is a bit different, which can cause it to be a few
    degrees off for big turns, or many small turns in the same
    direction. For example, you may need to use
    :meth:`turn(357) <pybricks.robotics.DriveBase.turn>` or
    :meth:`turn(362) <pybricks.robotics.DriveBase.turn>`
    on your robot to make a full turn.

    By default, this class tries to maintain the robot's position after a move
    completes. This means the wheels will spin if you pick the robot up, in an
    effort to maintain its heading angle. To avoid this, you can choose
    ``then=Stop.COAST`` in your last
    :meth:`straight <pybricks.robotics.DriveBase.straight>`,
    :meth:`turn <pybricks.robotics.DriveBase.turn>`, or
    :meth:`curve <pybricks.robotics.DriveBase.curve>` command.

    .. _measuring:

    .. rubric:: Measuring and validating the robot dimensions

    As a first estimate, you can measure the ``wheel_diameter`` and the
    ``axle_track`` with a ruler. Because it is hard to see where the wheels
    effectively touch the ground, you can estimate the ``axle_track`` as
    the distance between the midpoint of the wheels.

    If you don't have a ruler, you can use a LEGO beam to measure. The
    center-to-center distance of the holes is 8 mm. For some tyres, the
    diameter is printed on the side. For example, 62.4 x 20 means that the
    diameter is 62.4mm and that the width is 20 mm.

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

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:

    .. versionchanged:: 3.2

        The :meth:`done` and :meth:`stalled` methods have been moved.

.. pybricks-requirements:: pybricks-frozen

.. blockimg:: pybricks_variables_set_car

.. autoclass:: pybricks.robotics.Car
    :no-members:

    .. blockimg:: pybricks_blockCarSteer

    .. automethod:: pybricks.robotics.Car.steer

    .. blockimg:: pybricks_blockCarDrive_car_drive_at_power

    .. automethod:: pybricks.robotics.Car.drive_power

    .. blockimg:: pybricks_blockCarDrive_car_drive_at_speed

    .. automethod:: pybricks.robotics.Car.drive_speed

Examples
-------------------

Driving straight and turning in place with a drive base
********************************************************

This program shows the basics of driving and turning.

.. literalinclude::
    ../../examples/pup/robotics/drivebase_basics.py

Remote controlling a car with front wheel steering
**************************************************

This program shows how you can drive a car with front wheel steering
using the :class:`remote control <pybricks.pupdevices.Remote>`.

In this program, the ports match those of the `LEGO Technic 42099 Off-Roader
<https://pybricks.com/projects/sets/technic/42099-off-roader/>`_, but you can
use any other car with front wheel steering. If your vehicle has only one
drive motor, you can use a single motor instead of a tuple of the motors used
below.

.. literalinclude::
    ../../examples/pup/robotics/car_remote.py
