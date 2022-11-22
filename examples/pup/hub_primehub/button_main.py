from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Wait for any button to be pressed, and save the result.
pressed = []
while not any(pressed):
    pressed = hub.buttons.pressed()
    wait(10)

# Display a circle.
hub.display.icon(Icon.CIRCLE)

# Wait for all buttons to be released.
while any(hub.buttons.pressed()):
    wait(10)

# Display an arrow to indicate which button was pressed.
if Button.LEFT in pressed:
    hub.display.icon(Icon.ARROW_LEFT_DOWN)
elif Button.RIGHT in pressed:
    hub.display.icon(Icon.ARROW_RIGHT_DOWN)
elif Button.BLUETOOTH in pressed:
    hub.display.icon(Icon.ARROW_RIGHT_UP)

wait(3000)
