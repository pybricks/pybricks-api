:mod:`customdevices` -- Custom Devices
===========================================

.. automodule:: pybricks.customdevices
    :no-members:

Analog Sensor
^^^^^^^^^^^^^
.. autoclass:: pybricks.customdevices.AnalogSensor

I2C Device
^^^^^^^^^^^^^
.. autoclass:: pybricks.customdevices.I2CDevice

.. _i2caddress:

I2C Addresses
---------------
I2C addresses are 7-bit values. However, most vendors who make LEGO compatible
sensors provide an 8-bit address in their documentation.
To use those addresses, you must shift them by 1 bit.
For example, if the documented address is ``0xD2``, you must do::

    ev3 = EV3Brick()
    dev = I2CDevice(ev3.Port.S2, address=0xD2>>1)

Advanced I2C Commands
----------------------
The ``I2CDevice`` class methods call functions from the Linux SMBus driver.
The snippet below illustrates which functions get called exactly.
Some rudimentary I2C devices do not require a register/command argument. You
can get this behavior by setting ``reg=None``. This is shown below.

**Initialize**

::

    # Initialize
    ev3 = EV3Brick()
    dev = I2CDevice(ev3.Port.S2, address=0x69)

**Advanced read methods**

::

    # Recommended for reading. This calls i2c_smbus_read_i2c_block_data.
    result, = dev.read(reg=0x0F, length=1)

    # No register, read 1 byte. This calls i2c_smbus_read_byte.
    dev.read(reg=None, length=1)

    # No register, read, no data.
    # This calls i2c_smbus_write_quick wth I2C_SMBUS_READ.
    dev.read(reg=None, length=0)


**Advanced write methods**

::

    # Recommended for writing. This calls i2c_smbus_write_i2c_block_data.
    dev.write(reg=0x22, data=(0x08,))

    # No register, write 1 byte. This calls i2c_smbus_write_byte.
    dev.write(reg=None, data=(0x05,))

    # No register, write, no data.
    # This calls i2c_smbus_write_quick with I2C_SMBUS_WRITE.
    dev.write(reg=None, data=None)

More details about using I2C without MicroPython can be found on
the `ev3dev I2C`_ page.

.. _ev3dev I2C: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/i2c.html
