"""Robotics module for the Pybricks API."""

from .parameters import Stop


class DriveBase():
    """Class representing a robotic vehicle with two powered wheels and
    optional wheel caster(s)."""

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (:class:`Motor <.pupdevices.Motor>`):
                The motor that drives the left wheel.
            right_motor (:class:`Motor <.pupdevices.Motor>`):
                The motor that drives the right wheel.
            wheel_diameter (:ref:`dimension`): Diameter of the wheels.
            axle_track (:ref:`dimension`): Distance between the midpoints of
                                           the two wheels.

        """

    def start(self, drive_speed, turn_rate):
        """Start driving at the specified speed and turnrate, both measured at
        the center point between the wheels of the robot.

        Arguments:
            drive_speed (:ref:`linspeed`): Forward speed of the robot.
            turn_rate (:ref:`speed`): Turn rate of the robot.
        """
        pass

    def stop(self, stop_type=Stop.COAST):
        """stop(stop_type=Stop.COAST)

        Stop the robot.

        Arguments:
            stop_type (Stop): Whether to coast, brake, or hold (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
        """
        pass

    def distance(self):
        """Get the estimated accumulated driven distance.

        Returns:
            :ref:`distance`: Driven distance since last reset.
        """
        pass

    def angle(self):
        """Get the estimated accumulated rotation angle of the drivebase.

        Returns:
            :ref:`angle`: Accumulated angle since last reset.
        """
        pass

    def reset(self):
        """Reset the accumulated driven distance and angle to 0."""
        pass

    def set_drive_settings(self, drive_speed, drive_acceleration, turn_rate,
                           turn_acceleration, stop_type):
        """Configure the behavior of the :meth:`.straight`, :meth:`.turn`,
        and :meth:`.arc` methods.

        Arguments:
            drive_speed (:ref:`linspeed`): Forward speed of the robot.
            drive_acceleration (:ref:`linacceleration`): Forward acceleration
                of the robot.
            turn_rate (:ref:`speed`): Turn rate of the robot. Applies
                to :meth:`.turn` method only.
            turn_acceleration (:ref:`acceleration`): Angular acceleration of
                the robot. Applies to :meth:`.turn` method only.
            stop_type (Stop): Whether to coast, brake, or hold after
                a given command is complete.
        """
        pass

    def straight(self, distance):
        """Drive straight for a given distance.

        Arguments:
            distance (:ref:`distance`): Distance to travel.
        """
        pass

    def turn(self, angle):
        """Turn in place by a given angle.

        Arguments:
            angle (:ref:`angle`): Angle of the turn.
        """
        pass

    def arc(self, radius, angle):
        """Drive along an arc with a given radius by a given angle. An arc is
        a segment of a circle.

        A positive radius value makes your robot go right. A negative radius
        makes it go left.

        Arguments:
            radius (:ref:`dimension`): Radius of the circle.
            angle (:ref:`angle`): Angle traversed along the circle.
        """
        pass
