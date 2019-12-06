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
---------------------
Some rudimentary I2C devices do not require a register argument or even any
data. You can achieve this behavior as shown in the examples below.

**Initialize**

::

    # Initialize
    ev3 = EV3Brick()
    dev = I2CDevice(ev3.Port.S2, address=0x69)

**Advanced read methods**

::

    # Recommended for reading:
    result, = dev.read(reg=0x0F, length=1)

    # Read 1 byte from no particular register:
    dev.read(reg=None, length=1)

    # Read 0 bytes from no particular register:
    dev.read(reg=None, length=0)


**Advanced write methods**

::

    # Recommended for writing:
    dev.write(reg=0x22, data=b'\x08')

    # Write 1 byte to no particular register:
    dev.write(reg=None, data=b'\x08')

    # Write 0 bytes to no particular register:
    dev.write(reg=None, data=None)

**Additional technical resources**

The ``I2CDevice`` class methods call functions from the Linux SMBus driver.
To find out which commands are called under the hood, check the
`Pybricks source code`_.
More details about using I2C without MicroPython can be found on
the `ev3dev I2C`_ page.

.. _ev3dev I2C: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/i2c.html
.. _Pybricks source code: https://github.com/pybricks/pybricks-micropython


UART Device
^^^^^^^^^^^^^
.. autoclass:: pybricks.customdevices.UARTDevice
