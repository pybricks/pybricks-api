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

    .. rubric:: Settings

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. rubric:: Advanced Settings

    The :meth:`.settings` method can be used to adjust the most commonly used
    settings. It interacts with both of the attributes below to set the
    desired speed and acceleration values. You can also adjust the control
    settings manually using these attributes.

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:
