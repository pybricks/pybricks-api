from pybricks.messaging import BLERadio
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# Initialize the hub.
radio = BLERadio(observe_channels=[1])

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

while True:
    # Receive broadcast from the other hub.

    data = radio.observe(1)

    if data is not None:
        # Data was received and is less that one second old.
        # It contains the same values in the same order
        # that were passed to radio.broadcast() on the
        # other hub.
        left_angle, right_angle = data

        # Make the motors on this hub mirror the position of the
        # motors on the other hub.
        left_motor.track_target(left_angle)
        right_motor.track_target(right_angle)

    # Broadcasts are only sent every 100 milliseconds, so there is
    # no reason to call the observe() method more often than that.
    wait(100)
