from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Initialize a device using the NXT pinout convention.
device = I2CDevice(Port.A, address=0x42, mode=I2CDevice.CUSTOM_NXT)

# Read 1 byte from register 0x10.
result = device.read(reg=0x10)

# Read 4 bytes starting at register 0x10.
result = device.read(reg=0x10, length=4)

# Read 2 bytes and convert them to a number before returning.
result = device.read(reg=0x10, length=2, map=lambda data: data[0] << 8 | data[1])

# Read 1 byte from no particular register.
result = device.read(reg=None, length=1)

# Read 0 bytes from no particular register.
device.read(reg=None, length=0)

# Write 1 byte to register 0x20.
device.write(reg=0x20, data=b"\x08")

# Write 3 bytes starting at register 0x20.
device.write(reg=0x20, data=bytes([1, 2, 3]))

# Write 1 byte to no particular register.
device.write(reg=None, data=b"\x08")

# Write 0 bytes to register 0x20.
device.write(reg=0x20, data=None)

# Write 0 bytes to no particular register.
device.write(reg=None, data=None)
