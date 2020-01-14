:mod:`nxtdevices <pybricks.nxtdevices>` -- NXT Devices
======================================================

.. automodule:: pybricks.nxtdevices
    :no-members:

NXT Motor
^^^^^^^^^^^^^^^^
This motor works just like a LEGO MINDSTORMS EV3 Large Motor. You can use it in
your programs using the :mod:`Motor <.ev3devices>` class.

NXT Touch Sensor
^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.nxtdevices.TouchSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.TouchSensor.pressed

    .. toggle-header::
        :header: **Using older NXT Touch Sensors**

        **Example: Using a first-generation NXT Touch Sensor.**

        Normally, the EV3 brick always verifies that a sensor is attached
        before you can use it. This means that your program stops if a sensor
        that you selected was not found. The very first generation of NXT Touch
        Sensors did not support this functionality.
        To use these sensors, set ``verify_type=False`` as follows::

            from pybricks.nxtdevices import TouchSensor
            from pybricks.parameters import Port
            my_sensor = TouchSensor(Port.S1, verify_type=False)
