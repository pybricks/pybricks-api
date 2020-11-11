from pybricks.hubs import ExampleHub
from pybricks.tools import wait
from pybricks.parameters import Icon

# Initialize the hub.
hub = ExampleHub()

# Display a big arrow pointing up.
hub.display.image(Icon.UP)

# Wait so we can see what is displayed.
wait(2000)

# Display a heart at half brightness.
hub.display.image(Icon.HEART / 2)

# Wait so we can see what is displayed.
wait(2000)
