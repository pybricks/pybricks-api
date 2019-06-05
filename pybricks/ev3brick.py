"""LEGO® MINDSTORMS® EV3 Brick."""

from ._common import Speaker, Display, Battery, ColorLight


def buttons():
    """Check which buttons on the EV3 Brick are currently pressed.

    :returns: List of pressed buttons.
    :rtype: List of :class:`Button <parameters.Button>`

    """
    pass


sound = Speaker()
display = Display()
battery = Battery()
light = ColorLight()
