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

This class can be used to control classic LEGO motors using converter cables.

.. autoclass:: pybricks.builtins.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks.builtins.DCMotor.dc
        :noindex:

Ev3dev sensors
^^^^^^^^^^^^^^^^^^^^^

EV3 MicroPython is built on top of ev3dev, which means that a sensor
may be supported even if it is not listed in this documentation. If so, you can
use it with the ``Ev3devSensor`` class. This is easier and faster than using
the custom device classes given above.

To check whether you can use the ``Ev3devSensor`` class:

    * Plug the sensor into your EV3 Brick.
    * Go to the main menu of the EV3 Brick.
    * Select `Device Browser` and then `Sensors`.
    * If your sensor shows up, you can use it.

Now select your sensor from the menu and choose `set mode`. This shows all
available modes for this sensor. You can use these mode names as the ``mode``
setting below.

To learn more about compatible devices and what each mode does,
visit the `ev3dev sensors`_ page.

.. _ev3dev sensors: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html

.. autoclass:: pybricks.iodevices.Ev3devSensor
