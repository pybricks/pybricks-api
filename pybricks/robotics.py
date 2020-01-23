"""Robotics module for the Pybricks API."""

from .parameters import Stop


class DriveBase():
    """Class representing a robotic vehicle with two powered wheels and
    optional wheel caster(s)."""

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

    def drive(self, speed, steering):
        """Start driving at the specified speed and turn rate, both measured at
        the center point between the wheels of the robot.

        This method is useful in applications where you often change the speed
        and steering. For example, when following a line using a light sensor.

        Arguments:
            speed (:ref:`linspeed`): Speed of the robot. Positive is forward,
                negative is backward.
            steering (:ref:`speed`): Turn rate of the robot. Positive is to the
                right, negative is to the left.
        """
        pass

    def arc(self, speed, radius):
        """Start driving along an arc/circle with a given radius.

        This method is useful in applications where you want to drive smoothly
        around a known obstacle. Instead of going straight, turning, and then
        straight again. For example, you can make it drive in a semi-circle
        with a given radius and stop when a sensor detects an obstacle.

        Arguments:
            speed (:ref:`linspeed`): Speed of the robot along the arc.
                Positive is forward, negative is backward.
            radius (:ref:`dimension`): Radius of the arc. A positive radius
                value makes your robot go right. A negative radius value makes
                it go left.
        """
        pass

    def tank(self, left, right):
        """Start driving with the given speed for each wheel.

        This method is useful in applications where you just want to set the
        speed of the wheels or tank tracks, rather than the speed of the
        whole drive base.

        Arguments:
            left (:ref:`speed`): Speed of the left wheel.
            right (:ref:`speed`): Speed of the right wheel.
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

    def reset(self):
        """Reset the estimated driven distance and angle to 0."""
        pass

    def set_drive_settings(self, drive_speed, drive_acceleration, turn_rate,
                           turn_acceleration, stop_type):
        """Configure the default speed and acceleration.

        Arguments:
            drive_speed (:ref:`linspeed`): Drive speed of the robot.
            drive_acceleration (:ref:`linacceleration`): Linear acceleration
                of the robot.
            turn_rate (:ref:`speed`): Turn rate of the robot.
            turn_acceleration (:ref:`acceleration`): Angular acceleration of
                the robot.
            stop_type (Stop): Whether to coast, brake, or hold after
                a given command is complete.
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
