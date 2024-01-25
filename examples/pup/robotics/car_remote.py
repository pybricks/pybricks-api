from pybricks.parameters import Direction, Port, Button
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up motors.
front = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rear = Motor(Port.B, Direction.COUNTERCLOCKWISE)
steer = Motor(Port.C, Direction.CLOCKWISE)

# Connect to the remote.
remote = Remote()

# Set up the car.
car = Car(steer, [front, rear])

# The main program starts here.
while True:
    # Read remote state.
    pressed = remote.buttons.pressed()

    # Steer using the left pad. Steering is the percentage
    # of the angle determined while initializing.
    steering = 0
    if Button.LEFT_PLUS in pressed:
        steering += 100
    elif Button.LEFT_MINUS in pressed:
        steering -= 100
    car.steer(steering)

    # Drive using the right pad.
    power = 0
    if Button.RIGHT_PLUS in pressed:
        power += 100
    elif Button.RIGHT_MINUS in pressed:
        power -= 100
    car.drive_power(power)

    # Wait briefly.
    wait(10)
