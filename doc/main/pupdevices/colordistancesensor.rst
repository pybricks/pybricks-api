.. pybricks-requirements::

Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-colordistance.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_color_distance_sensor_colordistancesensor_default

.. blockimg:: pybricks_variables_set_color_distance_sensor_colordistancesensor_detectable_colors

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. blockimg:: pybricks_blockColor_ColorDistanceSensor_color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. blockimg:: pybricks_blockLightReflection_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. blockimg:: pybricks_blockLightAmbient_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. blockimg:: pybricks_blockDistance_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. blockimg:: pybricks_blockColor_ColorDistanceSensor_hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.detectable_colors

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. blockimg:: pybricks_blockLightOnColor_colordistancesensor_on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. blockimg:: pybricks_blockLightOnColor_colordistancesensor_off

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
