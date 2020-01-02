:mod:`iodevices` -- Generic I/O Devices
===========================================

.. automodule:: pybricks.iodevices
    :no-members:

LUMPDevice
^^^^^^^^^^^^^
.. autoclass:: pybricks.iodevices.LUMPDevice

Analog Sensor
^^^^^^^^^^^^^
.. autoclass:: pybricks.iodevices.AnalogSensor

I2C Device
^^^^^^^^^^^^^
.. autoclass:: pybricks.iodevices.I2CDevice

.. toggle-header::
    :header: **Show/hide example**

    **Example: Read and write to an I2C device.**

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/i2c_basics/main.py

.. _i2caddress:

I2C Addresses
---------------
I2C addresses are 7-bit values. However, most vendors who make LEGO compatible
sensors provide an 8-bit address in their documentation.
To use those addresses, you must shift them by 1 bit.
For example, if the documented address is ``0xD2``, you can do
``address = 0xD2 >> 1``.

Advanced I2C Commands
---------------------
Some rudimentary I2C devices do not require a register argument or even any
data. You can achieve this behavior as shown in the examples below.

.. toggle-header::
    :header: **Show/hide example**

    **Example: Advanced I2C read and write techniques.**

    .. literalinclude:: ../../pybricks-projects/snippets/ev3/i2c_extra/main.py

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
.. autoclass:: pybricks.iodevices.UARTDevice

.. toggle-header::
    :header: **Show/hide example**

    **Example: Read and write to a UART device.**

    .. literalinclude::
        ../../pybricks-projects/snippets/ev3/uart_basics/main.py

DC Motor
^^^^^^^^^^^^

.. autoclass:: pybricks.builtins.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks.builtins.DCMotor.dc
        :noindex:

    .. automethod:: pybricks.builtins.DCMotor.set_dc_settings
        :noindex:
