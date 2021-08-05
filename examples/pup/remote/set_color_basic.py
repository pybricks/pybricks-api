from pybricks.pupdevices import Remote
from pybricks.parameters import Color
from pybricks.tools import wait

# Connect to the remote.
remote = Remote()

while True:
    # Set the color to red.
    remote.light.on(Color.RED)
    wait(1000)

    # Set the color to blue.
    remote.light.on(Color.BLUE)
    wait(1000)
