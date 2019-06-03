:mod:`robotics` -- Robotics module
===========================================

.. automodule:: robotics
    :no-members:


.. autoclass:: robotics.DriveBase
    :no-members:

    Example::

        # Initialize two motors and a drive base
        left = Motor(Port.B)
        right = Motor(Port.C)
        robot = DriveBase(left, right, 56, 114)

    .. automethod:: robotics.DriveBase.drive

        Example::

            # Initialize two motors and a drive base
            left = Motor(Port.B)
            right = Motor(Port.C)
            robot = DriveBase(left, right, 56, 114)

            # Initialize a sensor
            sensor = UltrasonicSensor(Port.S4)

            # Drive forward until an object is detected
            robot.drive(100, 0)
            while sensor.distance() > 500:
                wait(10)
            robot.stop()

    .. automethod:: robotics.DriveBase.drive_time

        Example::

            # Drive forward at 100 mm/s for two seconds
            robot.drive_time(100, 0, 2000)

            # Turn at 45 deg/s for three seconds
            robot.drive_time(0, 45, 3000)

    .. automethod:: robotics.DriveBase.stop
