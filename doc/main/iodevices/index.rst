:mod:`iodevices <pybricks.iodevices>` -- Custom devices
============================================================

.. module:: pybricks.iodevices

This module has classes for generic and custom input/output devices.

Wireless devices
----------------

.. toctree::
   :maxdepth: 1
   :hidden:

   xboxcontroller
   playstationcontroller

.. pybricks-requirements:: xbox-controller

.. pybricks-classlink:: XboxController

.. figure:: ../../main/diagrams_source/xboxcontroller.png
   :width: 40 %
   :target: xboxcontroller.html

.. pybricks-requirements:: playstation-controller

.. pybricks-classlink:: PlayStationController

LEGO protocol devices
---------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   lwp3device
   lumpdevice
   pupdevice

.. pybricks-requirements:: pybricks-iodevices

.. pybricks-classlink:: LWP3Device

.. figure:: ../../main/cad/output/hub-lwp3.png
   :width: 80 %
   :target: lwp3device.html

.. pybricks-requirements:: pybricks-iodevices

.. pybricks-classlink:: LUMPDevice

.. figure:: ../../main/cad/output/iodevice-rj12green.png
   :width: 20 %
   :target: lumpdevice.html

.. pybricks-requirements:: pybricks-iodevices

.. pybricks-classlink:: PUPDevice

.. figure:: ../../main/cad/output/iodevice-pupdevice.png
   :width: 50 %
   :target: pupdevice.html

Generic protocols
-----------------

.. toctree::
   :maxdepth: 1
   :hidden:

   uartdevice
   i2cdevice
   analogsensor
   dcmotor

.. pybricks-requirements:: pybricks-iodevices

.. pybricks-classlink:: UARTDevice

.. |rj12grey| image:: ../../main/cad/output/iodevice-rj12grey.png
   :width: 20 %
   :target: uartdevice.html

.. |rj12cyan| image:: ../../main/cad/output/iodevice-rj12cyan.png
   :width: 20 %
   :target: i2cdevice.html

.. |custom-pup-uart| image:: ../../main/cad/output/iodevice-pupdevice.png
   :width: 50 %
   :target: uartdevice.html

.. |custom-pup-i2c| image:: ../../main/cad/output/iodevice-pupdevice.png
   :width: 50 %
   :target: i2cdevice.html

|rj12grey| |custom-pup-uart|

.. pybricks-requirements:: i2c-device

.. pybricks-classlink:: I2CDevice

|rj12cyan| |custom-pup-i2c|

.. pybricks-requirements:: pybricks-iodevices

.. pybricks-classlink:: AnalogSensor

.. figure:: ../../main/cad/output/iodevice-rj12brown.png
   :width: 20 %
   :target: analogsensor.html

.. pybricks-requirements:: pybricks-iodevices

.. pybricks-classlink:: DCMotor

.. figure:: ../../main/cad/output/iodevice-dcmotor.png
   :width: 40 %
   :target: dcmotor.html
