from pybricks.hubs import EV3Brick
from pybricks.iodevices import AnalogSensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait


class RCXTouchSensor(AnalogSensor):
    def pressed(self):
        return self.resistance() < 50 * 1000


ev3 = EV3Brick()
btn = RCXTouchSensor(Port.S1)

while True:
    if btn.pressed():
        ev3.light.on(Color.ORANGE)
    else:
        ev3.light.off()
    wait(10)
