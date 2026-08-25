.. pybricks-requirements:: ev3

NXT Color Sensor
^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/nxtdevice-color.png
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
