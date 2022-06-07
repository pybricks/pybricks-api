# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors

"""Robotics module for the Pybricks API."""

from ._common import Control, Motor, Number

from .parameters import Stop as _Stop

from typing import Tuple, Optional, overload


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

    distance_control = Control()
    """The traveled distance and drive speed are controlled by a PID
    controller. You can use this attribute to change its settings.
    See the :ref:`motor control <settings>` attribute for an overview of
    available methods. The ``distance_control`` attribute has the same
    functionality, but the settings apply to every millimeter driven by the
    drive base, instead of degrees turned by one motor."""

    heading_control = Control()
    """The robot turn angle and turn rate are controlled by a PID
    controller. You can use this attribute to change its settings.
    See the :ref:`motor control <settings>` attribute for an overview of
    available methods. The ``heading_control`` attribute has the same
    functionality, but the settings apply to every degree of rotation of the
    whole drive base (viewed from the top) instead of degrees turned by one
    motor."""

    def __init__(
        self,
        left_motor: Motor,
        right_motor: Motor,
        wheel_diameter: Number,
        axle_track: Number,
    ):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                The motor that drives the left wheel.
            right_motor (Motor):
                The motor that drives the right wheel.
            wheel_diameter (Number, mm): Diameter of the wheels.
            axle_track (Number, mm): Distance between the points where
                both wheels touch the ground.
        """

    def drive(self, speed: Number, turn_rate: Number) -> None:
        """drive(speed, turn_rate)

        Starts driving at the specified speed and turn rate. Both values are
        measured at the center point between the wheels of the robot.

        Arguments:
            speed (Number, mm/s): Speed of the robot.
            turn_rate (Number, deg/s): Turn rate of the robot.
        """
        pass

    def stop(self) -> None:
        """stop()

        Stops the robot by letting the motors spin freely."""
        pass

    def distance(self) -> int:
        """distance() -> int: mm

        Gets the estimated driven distance.

        Returns:
            Driven distance since last reset.
        """
        pass

    def angle(self) -> int:
        """angle() -> int: deg

        Gets the estimated rotation angle of the drive base.

        Returns:
            Accumulated angle since last reset.
        """
        pass

    def state(self) -> Tuple[int, int, int, int]:
        """state() -> Tuple[int, int, int, int]

        Gets the state of the robot.

        Returns:
            Tuple of distance, drive speed, angle, and turn rate of the robot.
        """
        pass

    def reset(self) -> None:
        """reset()

        Resets the estimated driven distance and angle to 0."""
        pass

    @overload
    def settings(
        self,
        straight_speed: Optional[Number],
        straight_acceleration: Optional[Number],
        turn_rate: Optional[Number],
        turn_acceleration: Optional[Number],
    ) -> None:
        ...

    @overload
    def settings(self) -> Tuple[int, int, int, int]:
        ...

    def settings(self, *args):
        """settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        settings() -> Tuple[int, int, int, int]

        Configures the speed and acceleration used
        by :meth:`.straight`, :meth:`.turn`, and  :meth:`.curve`.

        If you give no arguments, this returns the current values as a tuple.

        Arguments:
            straight_speed (Number, mm/s): Straight-line speed of the robot.
            straight_acceleration (Number, mm/s²): Straight-line
                acceleration and deceleration of the robot.
            turn_rate (Number, deg/s): Turn rate of the robot.
            turn_acceleration (Number, deg/s²): Angular acceleration and
                deceleration of the robot.
        """
        pass

    def straight(self, distance, then=_Stop.HOLD, wait=True) -> None:
        """straight(distance, then=Stop.HOLD, wait=True)

        Drives straight for a given distance and then stops.

        Arguments:
            distance (Number, mm): Distance to travel
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass

    def turn(self, angle, then=_Stop.HOLD, wait=True) -> None:
        """turn(angle, then=Stop.HOLD, wait=True)

        Turns in place by a given angle and then stops.

        Arguments:
            angle (Number, deg): Angle of the turn.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass

    def curve(self, radius, angle, then=_Stop.HOLD, wait=True) -> None:
        """curve(radius, angle, then=Stop.HOLD, wait=True)

        Drives an arc along a circle of a given radius, by a given angle.

        Arguments:
            radius (Number, mm): Radius of the circle.
            angle (Number, deg): Angle along the circle.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """
        pass
