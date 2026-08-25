# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Robotics module for the Pybricks API."""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

from . import _common
from .parameters import Stop

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, Motor
    from .parameters import Number


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

    See the `measuring`_ section for tips to measure and adjust the diameter
    and axle track values.
    """

    distance_control = _common.Control()
    """The traveled distance and drive speed are controlled by a PID
    controller. You can use this attribute to change its settings. See the
    :meth:`motor control <pybricks.pupdevices.Motor.control.limits>` attribute
    for an overview of available methods. The ``distance_control`` attribute
    has the same functionality, but the settings apply to every millimeter
    driven by the drive base, instead of degrees turned by one motor."""

    heading_control = _common.Control()
    """The robot turn angle and turn rate are controlled by a PID
    controller. You can use this attribute to change its settings. See the
    :meth:`motor control <pybricks.pupdevices.Motor.control.limits>` attribute
    for an overview of available methods. The ``heading_control`` attribute
    has the same functionality, but the settings apply to every degree of
    rotation of the whole drive base (viewed from the top) instead of degrees
    turned by one motor."""

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

    def stop(self) -> None:
        """stop()

        Stops the robot by letting the motors spin freely."""

    def brake(self) -> None:
        """brake()

        Stops the robot by passively braking the motors.
        """

    def hold(self) -> None:
        """hold()

        Stops the robot and actively holds it in place.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Gets the estimated driven distance.

        Returns:
            Driven distance since last reset.
        """

    def angle(self) -> float:
        """angle() -> float: deg

        Gets the estimated rotation angle of the drive base.

        When the gyro is used for this drive base, this gives the gyro angle.
        Otherwise, it gives the estimated angle estimated from the motor
        displacement.

        Returns:
            Accumulated angle since last reset.
        """

    def state(self) -> tuple[int, int, int, int]:
        """state() -> tuple[int, int, int, int]

        Gets the state of the robot.

        As with the :meth:`.angle` methods, the reported angle and turn rate
        are those of the gyro if the gyro is used. Otherwise they are
        estimated from the motor displacement.

        Returns:
            Tuple of distance, drive speed, angle, and turn rate of the robot.
        """

    def reset(self, distance: Number = 0, angle: Number = 0) -> None:
        """reset(distance=0, angle=0)

        Resets the estimated driven distance and heading angle.

        This also calls :meth:`.stop` to stop ongoing movements.
        If your robot is controlled with :meth:`.use_gyro` set to ``True``,
        calling this method will `also` set the gyro to the given angle.

        Arguments:
            distance (Number, mm): New value of the driven distance.
            angle (Number, deg): New heading angle of the robot.
        """

    @overload
    def settings(
        self,
        straight_speed: Number | None = None,
        straight_acceleration: Number | tuple[Number, Number] | None = None,
        turn_rate: Number | None = None,
        turn_acceleration: Number | tuple[Number, Number] | None = None,
    ) -> None: ...

    @overload
    def settings(
        self,
    ) -> tuple[int, int | tuple[int, int], int, int | tuple[int, int]]: ...

    def settings(self, *args):
        """
        settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        settings() -> tuple[int, int, int, int]
        settings() -> tuple[int, tuple[int, int], int, tuple[int, int]]

        Configures the drive base speed and acceleration.

        If you give no arguments, this returns the current values as a tuple.

        The initial values are automatically configured based on your wheel
        diameter and axle track. They are selected such that your robot
        drives at about 40% of its maximum speed.

        The speed values given here do not apply to the :meth:`.drive` method,
        since you provide your own speed values as arguments in that method.

        Speed and rate values are treated as absolute; negative values are
        converted to positive automatically.

        Arguments:
            straight_speed (Number, mm/s): Straight-line speed of the robot.
            straight_acceleration (Number or tuple[Number, Number], mm/s²):
                Straight-line acceleration and deceleration of the robot.
                Provide a single value to use the same acceleration and
                deceleration. Provide a tuple with two values to set them
                separately.
            turn_rate (Number, deg/s): Turn rate of the robot.
            turn_acceleration (Number or tuple[Number, Number], deg/s²):
                Angular acceleration and deceleration of the robot.
                Provide a single value to use the same acceleration and
                deceleration. Provide a tuple with two values to set them
                separately.
        """

    def straight(
        self, distance: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """straight(distance, then=Stop.HOLD, wait=True)

        Drives straight for a given distance and then stops.

        Arguments:
            distance (Number, mm): Distance to travel
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        """

    def turn(
        self,
        angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
        absolute: bool = False,
    ) -> MaybeAwaitable:
        """turn(angle, then=Stop.HOLD, wait=True, absolute=False)

        Turns in place by a given angle and then stops.

        Arguments:
            angle (Number, deg): Angle of the turn.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
            absolute (bool): If ``False`` (default), the robot turns _by_ the
                given angle relative to its current heading. If ``True``,
                the robot turns to the given absolute heading angle.
        """

    def arc(
        self,
        radius: Number,
        angle: Number = None,
        distance: Number = None,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """arc(radius, angle=None, distance=None, then=Stop.HOLD, wait=True)

        Drives an arc (a partial circle) with a given radius. You can specify
        how far to drive using either an angle or a distance.

        With a positive radius, the robot drives along a circle to its right.
        With a negative radius, the robot drives along a circle to its left.

        You can specify how far to travel along that circle as an angle
        (degrees) or distance (mm). A positive value means driving forward
        along the circle. Negative means driving in reverse.

        Arguments:
            radius (Number, mm): Radius of the circle.
            angle (Number, deg): Angle to drive along the circle.
            distance (Number, mm): Distance to drive along the circle,
                                   measured at the center of the robot.
            then (Stop): What to do after coming to a standstill.
            wait (bool): Wait for the maneuver to complete before continuing
                         with the rest of the program.
        Raises:
            ValueError:
                You must specify ``angle`` or ``distance``, but not both. The
                radius cannot be zero. Use :meth:`.turn` for in-place turns.
        """

    def done(self) -> bool:
        """done() -> bool

        Checks if an ongoing command or maneuver is done.

        Returns:
            ``True`` if the command is done, ``False`` if not.
        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Checks if the drive base is currently stalled.

        It is stalled when it cannot reach the target speed or position, even
        with the maximum actuation signal.

        Returns:
            ``True`` if the drive base is stalled, ``False`` if not.
        """

    def move_by(self, dx: Number, dy: Number, then: Stop = Stop.HOLD) -> MaybeAwaitable:
        """move_by(dx, dy, then=Stop.HOLD)

        Moves the robot by an amount given as X-and-Y coordinates on the robot
        drive area. The X-axis is what was forward when the program started.
        The Y-axis is 90° left of that. You can reset this by resetting the heading.

        The robot first turns to the required heading and then drives the
        straight-line distance. Because the heading target is absolute, the
        result is independent of the robot's current heading.

        Arguments:
            dx (Number, mm): X-distance on the drive area.
            dy (Number, mm): Y-distance on the drive area.
            then (Stop): What to do after coming to a standstill.

        Raises:
            ValueError: If one of the distances is more than 30 m.
        """

    def use_gyro(self, use_gyro: bool) -> None:
        """use_gyro(use_gyro)

        Choose ``True`` to use the gyro sensor for turning and driving
        straight. Choose ``False`` to rely only on the motor's built-in
        rotation sensors.

        This method will automatically call :meth:`.stop` to stop ongoing
        movements.

        Arguments:
            use_gyro (bool): ``True`` to enable, ``False`` to disable.
        """


class Car:
    """A vehicle with one steering motor, and one or more motors for driving.

    When you use this class, the steering motor will automatically find the
    center position. This also determines which angle corresponds to 100%
    steering.
    """

    def __init__(
        self,
        steer_motor: Motor,
        drive_motors: Motor | tuple[Motor, ...],
        torque_limit: Number = 100,
    ):
        """Car(steer_motor, drive_motors, torque_limit=100)

        Arguments:
            steer_motor (Motor):
                The motor that steers the front wheels.
            drive_motors (Motor): The motor that drives the wheels. Use a tuple
                for multiple motors.
            torque_limit (Number, %): The maximum torque limit used to find the
                endpoints for the steering mechanism, as a percentage of the
                maximum torque of the steering motor.
        """

    def steer(self, percentage: Number) -> None:
        """steer(percentage)

        Steers the front wheels by a given amount. For 100% steering, it
        steers right by the angle that was determined on initialization.
        For -100% steering, it steers left and 0% means straight.

        Arguments:
            steering (Number, %): Amount to steer the front wheels.
        """

    def drive_power(self, power: Number) -> None:
        """drive_power(power)

        Drives the car at a given power level. Positive values drive forward,
        negative values drive backward.

        The ``power`` value is used to set the motor voltage as a percentage of
        the battery voltage. Below 10%, the car will coast the wheels in order
        to roll out smoothly instead of braking abruptly.

        This command is useful for remote control applications where you want
        instant response to button presses or joystick movements.

        Arguments:
            speed (Number, %): Speed of the car.
        """

    def drive_speed(self, speed: Number) -> None:
        """drive_speed(speed)

        Drives the car at a given motor speed. Positive values drive forward,
        negative values drive backward.

        This command is useful for more precise driving with gentle
        acceleration and deceleration. This automatically increases the power
        to maintain speed as you drive across obstacles.

        Arguments:
            speed (Number, deg/s): Angular velocity of the drive motors.
        """


# Hide type-only names from jedi completions in the module namespace.
if TYPE_CHECKING:
    del MaybeAwaitable
    del Motor
    del Number
    del Stop
