# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors

"""Robotics module for the Pybricks API."""

from ._common import Control as _Control

from .parameters import Stop as _Stop


class DriveBase:
    """A robotic vehicle with two powered wheels and an optional support
    wheel or caster.

    By specifying the dimensions of your robot, this class
    makes it easy to drive a given distance in millimeters or turn by a given
    number of degrees.

    **Positive** distances, radii, or drive speeds mean
    driving **forward**. **Negative** means **backward**.

    **Positive** angles and turn rates mean turning **right**.
    **Negative** means **left**. So when viewed from the top,
    positive means clockwise and negative means counterclockwise.

    """

    distance_control = _Control()
    """The traveled distance and drive speed are controlled by a PID
    controller. You can use this attribute to change its settings.
    See the :ref:`motor control <settings>` attribute for an overview of
    available methods. The ``distance_control`` attribute has the same
    functionality, but the settings apply to every millimeter driven by the
    drive base, instead of degrees turned by one motor."""

    heading_control = _Control()
    """The robot turn angle and turn rate are controlled by a PID
    controller. You can use this attribute to change its settings.
    See the :ref:`motor control <settings>` attribute for an overview of
    available methods. The ``heading_control`` attribute has the same
    functionality, but the settings apply to every degree of rotation of the
    whole drive base (viewed from the top) instead of degrees turned by one
    motor."""

    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                The motor that drives the left wheel.
            right_motor (Motor):
                The motor that drives the right wheel.
            wheel_diameter (:ref:`dimension`): Diameter of the wheels.
            axle_track (:ref:`dimension`): Distance between the points where
                both wheels touch the ground.
        """

    def drive(self, speed, turn_rate):
        """Starts driving at the specified speed and turn rate. Both values are
        measured at the center point between the wheels of the robot.

        Arguments:
            speed (:ref:`linspeed`): Speed of the robot.
            turn_rate (:ref:`speed`): Turn rate of the robot.
        """
        pass

    def stop(self):
        """Stops the robot by letting the motors spin freely."""
        pass

    def distance(self):
        """Gets the estimated driven distance.

        Returns:
            :ref:`distance`: Driven distance since last reset.
        """
        pass

    def angle(self):
        """Gets the estimated rotation angle of the drive base.

        Returns:
            :ref:`angle`: Accumulated angle since last reset.
        """
        pass

    def state(self):
        """Gets the state of the robot.

        This returns the current :meth:`.distance`, the drive speed, the
        :meth:`.angle`, and the turn rate.

        :returns: Distance, drive speed, angle, turn rate
        :rtype: (:ref:`distance`, :ref:`linspeed`, :ref:`angle`, :ref:`speed`)
        """
        pass

    def reset(self):
        """Resets the estimated driven distance and angle to 0."""
        pass

    def settings(
        self, straight_speed, straight_acceleration, turn_rate, turn_acceleration
    ):
        """Configures the speed and acceleration used
        by :meth:`.straight`, :meth:`.turn`, and  :meth:`.curve`.

        If you give no arguments, this returns the current values as a tuple.

        You can only change the settings while the robot is stopped. This is
        either before you begin driving or after you call :meth:`.stop`.

        Arguments:
            straight_speed (:ref:`linspeed`): Straight-line speed of the robot.
            straight_acceleration (:ref:`linacceleration`): Straight-line
                acceleration and deceleration of the robot.
            turn_rate (:ref:`speed`): Turn rate of the robot.
            turn_acceleration (:ref:`acceleration`): Angular acceleration and
                deceleration of the robot.
        """
        pass

    def straight(self, distance, then=_Stop.HOLD, wait=True):
        """Drives straight for a given distance and then stops.

        Arguments:
            distance (:ref:`distance`): Distance to travel
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass

    def turn(self, angle, then=_Stop.HOLD, wait=True):
        """Turns in place by a given angle and then stops.

        Arguments:
            angle (:ref:`angle`): Angle of the turn.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass

    def curve(self, radius, angle, then=_Stop.HOLD, wait=True):
        """Drives an arc along a circle of a given radius, by a given angle.

        Arguments:
            radius (:ref:`dimension`): Radius of the circle.
            angle (:ref:`angle`): Angle along the circle.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass
