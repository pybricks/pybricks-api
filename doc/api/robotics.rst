:mod:`robotics <pybricks.robotics>` -- Robotics module
======================================================

.. automodule:: pybricks.robotics
    :no-members:


.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: Driving for a given distance or by an angle

    Use these commands to drive a given distance, or turn by a given angle.

    This is measured using the internal rotation sensors. Because wheels may
    slip while moving, the traveled distance and angle are only estimates.

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. automethod:: pybricks.robotics.DriveBase.settings

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

    .. rubric:: Advanced Settings

    The :meth:`.settings` method is used to adjust commonly used settings like
    the default speed and acceleration for straight maneuvers and turns.
    Use the following attributes to adjust more advanced control setttings.

    You can only change the settings while the robot is stopped. This is
    either before you begin driving or after you call :meth:`.stop`.

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:
