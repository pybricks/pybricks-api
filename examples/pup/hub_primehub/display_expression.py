from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Side
from pybricks.tools import wait

from urandom import randint

# Initialize the hub.
hub = PrimeHub()
hub.display.orientation(up=Side.RIGHT)

while True:

    # Start with random left brow: up or down.
    if randint(0, 100) < 70:
        brows = Icon.EYE_LEFT_BROW * 0.5
    else:
        brows = Icon.EYE_LEFT_BROW_UP * 0.5

    # Add random right brow: up or down.
    if randint(0, 100) < 70:
        brows += Icon.EYE_RIGHT_BROW * 0.5
    else:
        brows += Icon.EYE_RIGHT_BROW_UP * 0.5

    for i in range(3):
        # Display eyes open plus the random brows.
        hub.display.icon(Icon.EYE_LEFT + Icon.EYE_RIGHT + brows)
        wait(2000)

        # Display eyes blinked plus the random brows.
        hub.display.icon(Icon.EYE_LEFT_BLINK * 0.7 + Icon.EYE_RIGHT_BLINK * 0.7 + brows)
        wait(200)
