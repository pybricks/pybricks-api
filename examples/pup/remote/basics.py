from pybricks.pupdevices import Remote
from pybricks.parameters import Button
from pybricks.tools import wait

# Connect to the remote.
my_remote = Remote()

while True:
    # Check which buttons are pressed.
    pressed = my_remote.buttons.pressed()

    # Show the result.
    print("pressed:", pressed)

    # Check a specific button.
    if Button.CENTER in pressed:
        print("You pressed the center button!")

    # Wait so we can see the result.
    wait(100)
