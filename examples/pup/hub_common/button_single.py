# ThisHub = MoveHub CityHub TechnicHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color, Button
from pybricks.tools import wait, StopWatch

# Initialize the hub.
hub = ThisHub()

# Disable the stop button.
hub.system.set_stop_button(None)

# Check the button for 5 seconds.
watch = StopWatch()
while watch.time() < 5000:

    # Set light to green if pressed, else red.
    if hub.buttons.pressed():
        hub.light.on(Color.GREEN)
    else:
        hub.light.on(Color.RED)

# Enable the stop button again.
hub.system.set_stop_button(Button.CENTER)

# Now you can press the stop button as usual.
wait(5000)
