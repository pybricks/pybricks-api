from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port
from pybricks.tools import wait


class MyTemperatureSensor:
    def __init__(self, port):
        # Initialize the NXT Temperature Sensor as a custom I2C device.
        self.i2c = I2CDevice(port, address=0x4C, mode=I2CDevice.CUSTOM_NXT)

        # Write to the configuration register (0x01) to set the resolution.
        self.i2c.write(reg=0x01, data=bytes([0x40]))

    def scale_temperature(self, data):
        # Combine the bytes into a signed value in 1/256 degrees Celsius.
        value = (data[0] << 8) | data[1]
        if value >= 0x8000:
            value -= 0x10000
        return value / 256

    def temperature(self):
        # Read two bytes from the temperature register (0x00) and
        # convert them to degrees Celsius.
        return self.i2c.read(reg=0x00, length=2, map=self.scale_temperature)


sensor = MyTemperatureSensor(Port.S1)

while True:
    print(sensor.temperature())
    wait(500)
