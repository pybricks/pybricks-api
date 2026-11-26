.. pybricks-requirements:: i2c-device

Generic I2C Device
^^^^^^^^^^^^^^^^^^

Connect I2C and Qwiic devices to your LEGO MINDSTORMS or SPIKE hub.
Use custom electronics at your own risk!

.. _i2cpinout:

The pinout is shown below. Note the orientation of the connector. For EV3, the
internal wire colors match those on the diagram below.

.. image:: pinout_numbered.jpg
   :width: 50 %

.. list-table::
   :header-rows: 1

   * - Pin
     - EV3 (``CUSTOM_NXT``)
     - Powered Up (``CUSTOM_NXT``)
     - Powered Up (``CUSTOM_QWIIC``)
   * - 1 (white)
     - Optional battery power
     - Motor Terminal 1
     - Motor Terminal 1
   * - 2 (black)
     - N/A
     - Motor Terminal 2
     - Motor Terminal 2
   * - 3 (red)
     - Ground
     - Ground
     - Ground
   * - 4 (green)
     - VCC (5 V)
     - VCC (3.3 V)
     - VCC (3.3 V)
   * - 5 (yellow)
     - SCL (master) (3.3 V)
     - SCL (master) (3.3 V)
     - SDA (master) (3.3 V)
   * - 6 (blue)
     - SDA (master) (3.3 V)
     - SDA (master) (3.3 V)
     - SCL (master) (3.3 V)

Do not power 3.3V devices from the EV3 5V VCC if your device does not support it.

.. autoclass:: pybricks.iodevices.I2CDevice
   :no-members:

   .. automethod:: read

   .. automethod:: write

Examples
-------------------

Reading a custom I2C sensor
***************************

This example uses the NXT Temperature Sensor as if it were a custom I2C
device. It sets the resolution once, and then reads the temperature in a loop.

.. literalinclude::
    ../../../examples/pup/iodevices_i2cdevice/temperature_basics.py

Making your own sensor class
****************************

This is the same example, but now wrapped in a class. The ``map`` argument
converts the raw bytes to degrees Celsius, so ``temperature()`` returns the
value you are interested in. The ``temperature()`` method can then also be used
with `await` when multitasking.

.. literalinclude::
    ../../../examples/pup/iodevices_i2cdevice/temperature_class.py

Using a Qwiic device
********************

This example shows text on a SparkFun SerLCD display, connected using the
Qwiic convention. It also shows how to choose a custom I2C frequency.

.. literalinclude::
    ../../../examples/pup/iodevices_i2cdevice/qwiic_display.py

Overview of all I2C options
***************************

This example does not represent a real device. It shows all the ways you
can read and write data. Some rudimentary devices do not require a register
argument or even any data, as shown below.

.. literalinclude::
    ../../../examples/pup/iodevices_i2cdevice/api_overview.py

Some devices use 16-bit register addresses. Use ``reg_len=2`` for these, and
then use registers as usual.

.. literalinclude::
    ../../../examples/pup/iodevices_i2cdevice/api_overview_reg16.py

.. _i2caddress:

I2C Addresses
---------------
I2C addresses are 7-bit values. However, some vendors who make LEGO compatible
sensors provide an 8-bit address in their documentation.
To use those addresses, you must shift them by 1 bit.
For example, if the documented address is ``0xD2``, you can do
``address = 0xD2 >> 1``.
