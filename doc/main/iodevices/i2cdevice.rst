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

**Example: Read and write to an I2C device**

.. literalinclude:: ../../../examples/ev3/i2c_basics/main.py

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

**Example: Advanced I2C read and write techniques**

.. literalinclude:: ../../../examples/ev3/i2c_extra/main.py
