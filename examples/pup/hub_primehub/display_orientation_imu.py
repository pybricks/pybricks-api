from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

while True:

    # Check which side of the hub is up.
    up_side = hub.imu.up()

    # Use this side to set the display orientation.
    hub.display.orientation(up_side)

    # Display something, like an arrow.
    hub.display.icon(Icon.UP)

    wait(10)
