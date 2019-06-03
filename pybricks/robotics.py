"""Robotics module for the Pybricks API."""

from parameters import Stop, Direction


class DriveBase():
    """Class representing a robotic vehicle with two powered wheels and optional wheel caster(s)."""

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor): The motor that drives the left wheel.
            right_motor (Motor): The motor that drives the right wheel.
            wheel_diameter (:ref:`dimension`): Diameter of the wheels.
            axle_track (:ref:`dimension`): Distance between the midpoints of the two wheels.

        """

    def drive(self, speed, steering):
        """Start driving at the specified speed and turnrate, both measured at the center point between the wheels of the robot.

        Arguments:
            speed (:ref:`travelspeed`): Forward speed of the robot.
            steering (:ref:`speed`): Turn rate of the robot.
        """
        pass

    def drive_time(self, speed, steering, time):
        """Drive at the specified speed and turnrate for a given amount of time, and then stop.

        Arguments:
            speed (:ref:`travelspeed`): Forward speed of the robot.
            steering (:ref:`speed`): Turn rate of the robot.
            time (:ref:`time`): Duration of the maneuver.

        """
        pass

    def stop(self, stop_type=Stop.COAST):
        """stop(stop_type=Stop.COAST)

        Stop the robot.

        Arguments:
            stop_type (Stop): Whether to coast, brake, or hold (*Default*: :class:`Stop.COAST <parameters.Stop>`).
        """
        pass
