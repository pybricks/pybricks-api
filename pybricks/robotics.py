"""Robotics module for the Pybricks API."""

from .parameters import Stop
from .builtins import Control


class DriveBase():
    """A robotic vehicle with two powered wheels and an optional support
    wheel or caster."""

    distance_control = Control()
    """PID control is used to track the desired speed and travel the control
    required distance You can change the behavior through this attribute.
    See :ref:`control` for an overview of available methods."""

    heading_control = Control()
    """PID control is used to synchronize the wheel speed,
    track the turn rate, and reach the turn angle. You can change the control
    behavior through this attribute. See :ref:`control` for an overview of
    available methods."""

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                The motor that drives the left wheel.
            right_motor (Motor):
                The motor that drives the right wheel.
            wheel_diameter (:ref:`dimension`): Diameter of the wheels.
            axle_track (:ref:`dimension`): Distance between the midpoints of
                                           the two wheels.
        """

    def drive(self, drive_speed, turn_rate):
        """Start driving at the specified speed and turn rate. Both values are
        measured at the center point between the wheels of the robot.

        Arguments:
            drive_speed (:ref:`linspeed`): Speed of the robot. Positive is forward,
                negative is backward.
            turn_rate (:ref:`speed`): Turn rate of the robot. Positive is to the
                right, negative is to the left.
        """
        pass

    def stop(self, stop_type=Stop.COAST):
        """Stop the robot.

        Arguments:
            stop_type (Stop): Whether to coast, brake, or hold (*Default*:
                              :class:`Stop.COAST <.parameters.Stop>`).
        """
        pass

    def distance(self):
        """Get the estimated driven distance.

        Returns:
            :ref:`distance`: Driven distance since last reset.
        """
        pass

    def angle(self):
        """Get the estimated rotation angle of the drive base.

        Returns:
            :ref:`angle`: Accumulated angle since last reset.
        """
        pass

    def state(self):
        """Get the instantaneous physical state.

        This returns the current :meth:`.distance`, the drive speed, the
        :meth:`.angle`, and the turn rate.

        :returns: Distance, drive speed, angle, turn rate
        :rtype: (:ref:`distance`, :ref:`linspeed`, :ref:`angle`, :ref:`speed`)
        """
        pass

    def reset(self):
        """Reset the estimated driven distance and angle to 0."""
        pass

    def settings(self, drive_speed, drive_acceleration, turn_rate,
                 turn_acceleration):
        """Configure the acceleration and maximum speed used
        by :meth:`.straight`, :meth:`.turn`, and :meth:`.drive`.

        If you give no arguments, this returns the current values as a tuple.

        Arguments:
            drive_speed (:ref:`linspeed`): Drive speed of the robot.
            drive_acceleration (:ref:`linacceleration`): Linear acceleration
                of the robot.
            turn_rate (:ref:`speed`): Turn rate of the robot.
            turn_acceleration (:ref:`acceleration`): Angular acceleration of
                the robot.
        """
        pass

    def straight(self, distance):
        """Drive straight for a given distance and then stop.

        Arguments:
            distance (:ref:`distance`): Distance to travel.
        """
        pass

    def turn(self, angle):
        """Turn in place by a given angle and then stop.

        Arguments:
            angle (:ref:`angle`): Angle of the turn.
        """
        pass
