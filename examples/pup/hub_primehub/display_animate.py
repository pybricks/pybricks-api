from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Turn the hub light off (optional).
hub.light.off()

# Create a list of intensities from 0 to 100 and back.
brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))

# Create an animation of the heart icon with changing brightness.
hub.display.animate([Icon.HEART * i / 100 for i in brightness], 30)

# The animation repeats in the background. Here we just wait.
while True:
    wait(100)
