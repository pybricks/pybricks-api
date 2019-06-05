:mod:`robotics` -- Robotics module
===========================================

.. automodule:: pybricks.robotics
    :no-members:


.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    Example::

        # Initialize two motors and a drive base
        left = Motor(Port.A)
        right = Motor(Port.B)
        robot = DriveBase(left, right, 56, 114)

    .. automethod:: pybricks.robotics.DriveBase.drive

        Example::

            # Initialize a sensor
            sensor = ColorDistanceSensor(Port.C)

            # Drive forward until an object is detected
            robot.drive(100, 0)
            while sensor.distance() > 30:
                wait(10)
            robot.stop()

    .. automethod:: pybricks.robotics.DriveBase.drive_time

        Example::

            # Drive forward at 100 mm/s for two seconds
            robot.drive_time(100, 0, 2000)

            # Turn at 45 deg/s for three seconds
            robot.drive_time(0, 45, 3000)

    .. automethod:: pybricks.robotics.DriveBase.stop
