Analog Sensor
^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_rj12_brown.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.AnalogSensor

I2C Device
^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_rj12_bluegreen.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.I2CDevice

.. toggle-header::
    :header: **Show/hide example**

    **Example: Read and write to an I2C device.**

    .. literalinclude:: ../../examples/ev3/i2c_basics/main.py

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

    .. literalinclude:: ../../examples/ev3/i2c_extra/main.py

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

.. figure:: ../api/images/sensor_rj12_gray.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.UARTDevice

.. toggle-header::
    :header: **Show/hide example**

    **Example: Read and write to a UART device.**

    .. literalinclude::
        ../../examples/ev3/uart_basics/main.py

DC Motor
^^^^^^^^^^^^

.. figure:: ../api/images/rcxmotor.png
   :width: 40 %

.. autoclass:: pybricks._common.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks._common.DCMotor.dc
        :noindex:

    .. automethod:: pybricks._common.DCMotor.stop
        :noindex:

Ev3dev sensors
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ev3dev.png
   :width: 70 %

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

.. autoclass:: pybricks.iodevices.Ev3devSensor
    :no-members:

    .. autoattribute:: pybricks.iodevices.Ev3devSensor.sensor_index
        :annotation:

    .. autoattribute:: pybricks.iodevices.Ev3devSensor.port_index
        :annotation:

    .. automethod:: pybricks.iodevices.Ev3devSensor.read

.. toggle-header::
    :header: **Show/hide example: Reading values with the Ev3devSensor class**

    **Example**

    In this example we use the LEGO MINDSTORMS EV3 Color Sensor with the raw
    RGB mode. This gives uncalibrated red, green, and blue reflection values.

    .. literalinclude::
        ../../examples/ev3/ev3devsensor/main.py

.. toggle-header::
    :header: **Show/hide example: Extending the Ev3devSensor class**

    **Example**

    This example shows how to extend the ``Ev3devSensor`` class by accessing
    additional features found in the Linux system folder for this device.

    .. literalinclude::
        ../../examples/ev3/ev3devsensor/class_example.py

.. _ev3dev sensors: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html
.. _Mode name: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html
.. _lego-sensor: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html#the-lego-sensor-subsytem
.. _lego-port: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ports.html#the-lego-port-subsystem
