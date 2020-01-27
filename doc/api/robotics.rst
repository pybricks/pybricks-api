:mod:`robotics <pybricks.robotics>` -- Robotics module
======================================================

.. automodule:: pybricks.robotics
    :no-members:


.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. automethod:: pybricks.robotics.DriveBase.drive

.. .. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: Automatic drive control

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. rubric:: Manual drive control

    The methods :meth:`.drive`, :meth:`.arc`, and :meth:`.tank` make your
    drive base move at a desired speed and and steering level. It keeps moving
    until you stop it. For example, you can keep moving until an obstacle is
    detected with a sensor.
    Then use :meth:`.stop` to make your drive base stop.

    The only difference between :meth:`.drive`, :meth:`.arc`, and :meth:`.tank`
    is how you specify the desired speed and steering. You can choose the
    method which fits your application best.

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. automethod:: pybricks.robotics.DriveBase.arc

    .. automethod:: pybricks.robotics.DriveBase.tank

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. rubric:: Measuring

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. rubric:: Settings

    .. automethod:: pybricks.robotics.DriveBase.set_drive_settings
