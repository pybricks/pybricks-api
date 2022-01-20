from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor on port A.
example_motor = Motor(Port.A)

while True:

    # Get the default angle value.
    angle = example_motor.angle()

    # Get the angle between 0 and 360.
    absolute_angle = example_motor.angle() % 360

    # Get the angle between -180 and 179.
    wrapped_angle = (example_motor.angle() + 180) % 360 - 180

    # Print the results.
    print(angle, absolute_angle, wrapped_angle)
    wait(100)
