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
******************************

``HubInit()`` automatically connects to any of the known hubs and reports its features in ``hub_info``
The init loops over all the available ports and ``ConnectToDevice()`` connects with available devices.
The remote, if there is one, controls 2 variables; in range(-100,100), the other in range(0,100).
These could be used to control 1 or more motors, lights, etc.
On ``DIAGNOSTICS_PERIOD`` 4 different sensors values are read if available together with hub voltage and current. 
Also ``ch1_val`` is applied as dc() value on motors if there are any.

.. literalinclude::
    ../../../examples/pup/iodevices_pupdevice/diagnostics.py
