.. pybricks-requirements::

Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/images/sensor_colordistance.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.detectable_colors

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.off

Examples
-------------------

Measuring color
***************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/color_print.py


Waiting for a color
*******************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/wait_for_color.py

Measuring distance and blinking the light
*****************************************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/distance_blink.py

Reading hue, saturation, value
**********************************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/hsv.py

Changing the detectable colors
******************************

By default, the sensor is configured to detect red, yellow, green,
blue, white, or no color, which suits many applications.

For better results in your application, you can measure your desired
colors in advance, and tell the sensor to look only for those colors.
Be sure to measure them at the **same distance and light conditions**
as in your final application. Then you'll get very accurate results
even for colors that are otherwise hard to detect.

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/detectable_colors.py
