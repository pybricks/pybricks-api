:mod:`nxtdevices <pybricks.nxtdevices>` -- NXT devices
======================================================

.. automodule:: pybricks.nxtdevices
    :no-members:

NXT Motor
^^^^^^^^^^^^^^^^
This motor works just like a LEGO MINDSTORMS EV3 Large Motor. You can use it in
your programs using the :mod:`Motor <.ev3devices>` class.

NXT Touch Sensor
^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-touch.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.TouchSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.TouchSensor.pressed

NXT Light Sensor
^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-light.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.LightSensor

NXT Color Sensor
^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-color.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.ColorSensor.color

    .. automethod:: pybricks.nxtdevices.ColorSensor.ambient

    .. automethod:: pybricks.nxtdevices.ColorSensor.reflection

    .. automethod:: pybricks.nxtdevices.ColorSensor.rgb

    .. rubric:: Advanced color sensing

    .. automethod:: pybricks.nxtdevices.ColorSensor.hsv

    .. automethod:: pybricks.nxtdevices.ColorSensor.detectable_colors

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off.

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.on

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.off

NXT Ultrasonic Sensor
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-ultrasonic.png
   :width: 24 %

.. autoclass:: pybricks.nxtdevices.UltrasonicSensor

NXT Sound Sensor
^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-sound.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.SoundSensor

NXT Temperature Sensor
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-temperature.png
   :width: 32 %

.. autoclass:: pybricks.nxtdevices.TemperatureSensor

NXT Energy Meter
^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-energy.png
   :width: 30 %

.. autoclass:: pybricks.nxtdevices.EnergyMeter

Vernier Adapter
^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.nxtdevices.VernierAdapter

**Example: Using the Surface Temperature Sensor.**

.. literalinclude:: ../../examples/ev3/vernier_surface_temperature/main.py
