from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the NXT Temperature Sensor as a custom I2C device.
sensor = I2CDevice(Port.S1, address=0x4C, mode=I2CDevice.CUSTOM_NXT)

# Write to the configuration register (0x01) to set the resolution.
sensor.write(reg=0x01, data=bytes([0x40]))

while True:
    # Read two bytes from the temperature register (0x00).
    high, low = sensor.read(reg=0x00, length=2)

    # Combine the bytes into a signed value in 1/256 degrees Celsius.
    value = (high << 8) | low
    if value >= 0x8000:
        value -= 0x10000
    print(value / 256)

    wait(500)
