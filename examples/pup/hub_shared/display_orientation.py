from pybricks.hubs import ExampleHub
from pybricks.tools import wait
from pybricks.parameters import Side

# Initialize the hub.
hub = ExampleHub()

# Rotate the display. Now right is up.
hub.display.orientation(up=Side.RIGHT)

# Display a number. This will be shown sideways.
hub.display.number(23)

# Wait so we can see what is displayed.
wait(10000)
