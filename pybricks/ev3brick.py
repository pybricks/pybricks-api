"""LEGO® MINDSTORMS® EV3 Brick."""

from parameters import Color
from _common import Speaker, Display, Battery


def buttons():
    """Check which buttons on the EV3 Brick are currently pressed.

    :returns: List of pressed buttons.
    :rtype: List of :class:`Button <parameters.Button>`

    """
    pass


def light(color):
    """Set the color of the brick light.

    Arguments:
        color (Color): Color of the light. Choose ``Color.BLACK`` or ``None``
                       to turn the light off.
    """
    pass


sound = Speaker()
display = Display()
battery = Battery()
