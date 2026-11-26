from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Initialize a device that uses 16-bit register addresses.
device = I2CDevice(Port.A, address=0x29, mode=I2CDevice.CUSTOM_QWIIC, reg_len=2)

# Read 2 bytes starting at register 0x010F.
result = device.read(reg=0x010F, length=2)

# Write 1 byte to register 0x0087.
device.write(reg=0x0087, data=b"\x40")
