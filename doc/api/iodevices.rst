:mod:`iodevices <pybricks.iodevices>` -- Generic I/O Devices
============================================================

.. automodule:: pybricks.iodevices
    :no-members:

.. note::

    This module provides classes to interact with unofficial motors, sensors,
    and other custom electronics. You should only connect custom electronics
    or unofficial devices if you know what you are doing. Proceed with caution.


Powered Up Device
^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_pup.png
   :width: 70 %

.. autoclass:: pybricks.iodevices.PUPDevice


.. raw:: html

   <h1>EV3 Only</h1>

The classes listed below are **only supported on the EV3** at this time. Some
classes, such as ``UARTDevice``, ``I2CDevice`` and ``DCMotor`` could be added
to Powered Up hubs in a future release.

If you'd like to see this happen, be sure to ask us on our `support page`_.

.. include:: iodevices_ev3.inc

.. _support page: https://github.com/pybricks/support/issues/
