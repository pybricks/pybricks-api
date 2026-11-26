from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port
from pybricks.tools import wait

# SparkFun SerLCD commands.
COMMAND_SETTING = 0x7C
COMMAND_CLEAR = 0x2D
COMMAND_SET_RGB = 0x2B

# Initialize the display in Qwiic mode at 50 kHz.
lcd = I2CDevice(Port.A, address=0x72, mode=I2CDevice.CUSTOM_QWIIC, frequency=50000)

# Clear display and home cursor.
lcd.write(reg=None, data=bytes([COMMAND_SETTING, COMMAND_CLEAR]))

# Write some text.
lcd.write(reg=None, data=b"Hello Pybricks!")

# Cycle backlight red, green, blue, white.
for r, g, b in [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]:
    lcd.write(reg=None, data=bytes([COMMAND_SETTING, COMMAND_SET_RGB, r, g, b]))
    wait(1000)
