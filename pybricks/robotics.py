# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Robotics module for the Pybricks API."""

from .parameters import Stop
from .builtins import Control


class DriveBase():
    """A robotic vehicle with two powered wheels and an optional support
    wheel or caster."""

    distance_control = Control()
    """The traveled distance and drive speed are controlled by a PID
    controller. You can use this attribute to change its settings.
    See :ref:`control` for an overview of available methods."""

    heading_control = Control()
    """The robot turn angle and turn rate are controlled by a PID
    controller. You can use this attribute to change its settings.
    See :ref:`control` for an overview of available methods."""

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
        """Get the state of the robot.

        This returns the current :meth:`.distance`, the drive speed, the
        :meth:`.angle`, and the turn rate.

        :returns: Distance, drive speed, angle, turn rate
        :rtype: (:ref:`distance`, :ref:`linspeed`, :ref:`angle`, :ref:`speed`)
        """
        pass

    def reset(self):
        """Reset the estimated driven distance and angle to 0."""
        pass

    def settings(self, straight_speed, straight_acceleration, turn_rate,
                 turn_acceleration):
        """Configure the speed and acceleration used
        by :meth:`.straight` and :meth:`.turn`.

        If you give no arguments, this returns the current values as a tuple.

        Arguments:
            straight_speed (:ref:`linspeed`): Speed of the robot during
                :meth:`.straight`.
            straight_acceleration (:ref:`linacceleration`): Acceleration and
                deceleration of the robot at the start and end
                of :meth:`.straight`.
            turn_rate (:ref:`speed`): Turn rate of the robot
                during :meth:`.turn`.
            turn_acceleration (:ref:`acceleration`): Angular acceleration and
                deceleration of the robot at the start and end
                of :meth:`.turn`.
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
