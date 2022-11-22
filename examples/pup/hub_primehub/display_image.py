from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Icon

# Initialize the hub.
hub = PrimeHub()

# Display a big arrow pointing up.
hub.display.icon(Icon.UP)

# Wait so we can see what is displayed.
wait(2000)

# Display a heart at half brightness.
hub.display.icon(Icon.HEART / 2)

# Wait so we can see what is displayed.
wait(2000)
