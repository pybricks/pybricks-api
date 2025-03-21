.. pybricks-requirements:: pybricks-iodevices

Powered Up Device
^^^^^^^^^^^^^^^^^

.. figure:: ../cad/output/iodevice-pupdevice.png
   :width: 60 %

.. autoclass:: pybricks.iodevices.PUPDevice
    :no-members:

    .. automethod:: pybricks.iodevices.PUPDevice.info

    .. automethod:: pybricks.iodevices.PUPDevice.read

    .. automethod:: pybricks.iodevices.PUPDevice.write

Examples
-------------------

Detecting devices
******************************

.. literalinclude::
    ../../../examples/pup/iodevices_pupdevice/port_info.py

Diagnostics: bringing examples together.
****************************************************************************************

``HubInit()`` automatically connects to any of the known hubs and reports its features
in ``hub_info``.
``GetPorts()`` and ``ConnectToDevice()`` are used to connect any available device.
The later also initiates a class object belonging to that device.
A remote can control 2 variables; CH A/1 in range(-100,100) and CH B/2 in range(0,100).
These could be used to control 1 or more motors, lights, etc.
On ``DIAGNOSTICS_PERIOD`` IMU and 4 different sensors values are read if available.
Also hub voltage and current are printed at that time.
Also ``ch1_val`` is applied as dc() value on motors if there are any.

.. literalinclude::
    ../../../examples/pup/iodevices_pupdevice/diagnostics.py
