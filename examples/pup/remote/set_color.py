from pybricks.pupdevices import Remote
from pybricks.parameters import Button, Color


def button_to_color(buttons):

    # Return a color depending on the button.
    if Button.LEFT_PLUS in buttons:
        return Color.RED
    if Button.LEFT_MINUS in buttons:
        return Color.GREEN
    if Button.LEFT in buttons:
        return Color.ORANGE
    if Button.RIGHT_PLUS in buttons:
        return Color.BLUE
    if Button.RIGHT_MINUS in buttons:
        return Color.YELLOW
    if Button.RIGHT in buttons:
        return Color.CYAN
    if Button.CENTER in buttons:
        return Color.VIOLET

    # Return no color by default.
    return Color.NONE


# Connect to the remote.
remote = Remote()

while True:
    # Wait until a button is pressed.
    pressed = ()
    while not pressed:
        pressed = remote.buttons.pressed()

    # Convert button code to color.
    color = button_to_color(pressed)

    # Set the remote light color.
    remote.light.on(color)

    # Wait until all buttons are released.
    while pressed:
        pressed = remote.buttons.pressed()
