"""Sphinx workaround to document instance attributes such as self.light"""

from .builtins import (Motor, Speaker, Display, Battery, ColorLight,
                       KeyPad, LightArray)
from .parameters import Direction
from types import ModuleType


def make_instance(classdef):
    """Make a class instance to look like a module so Sphinx can parse it."""
    name = ''
    mod = ModuleType(name)
    for m in classdef.__dict__.values():
        if callable(m):
            setattr(mod, m.__name__, m)
    return mod


light = make_instance(ColorLight)

lights = make_instance(LightArray)

buttons = make_instance(KeyPad)

battery = make_instance(Battery)

speaker = make_instance(Speaker)

display = make_instance(Display)


class Motor(Motor):

    def __init__(self, port, direction=Direction.CLOCKWISE):
        """Motor(port, direction=Direction.CLOCKWISE)

        Create a motor instance.

        Arguments:
            port (Port): Port to which the motor is connected.
            direction (Direction): Positive speed direction
                                   (*Default*: `Direction.CLOCKWISE`).
        """
        pass
