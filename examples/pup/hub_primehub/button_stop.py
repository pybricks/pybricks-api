from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

# Initialize the hub.
hub = PrimeHub()

# Configure the stop button combination. Now, your program stops
# if you press the center and Bluetooth buttons simultaneously.
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

# Now we can use the center button as a normal button.
while True:

    # Play a sound if the center button is pressed.
    if Button.CENTER in hub.buttons.pressed():
        hub.speaker.beep()
