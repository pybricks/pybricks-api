.. pybricks-requirements::

Color Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_color_lights.png
   :width: 70 %

.. blockimg:: pybricks_variables_set_color_sensor_colorsensor_default

.. blockimg:: pybricks_variables_set_color_sensor_colorsensor_detectable_colors

.. autoclass:: pybricks.pupdevices.ColorSensor
    :no-members:

    .. blockimg:: pybricks_blockColor_ColorSensor_color

    .. automethod:: pybricks.pupdevices.ColorSensor.color

    .. blockimg:: pybricks_blockLightReflection_ColorSensor

    .. automethod:: pybricks.pupdevices.ColorSensor.reflection

    .. blockimg:: pybricks_blockLightAmbient_ColorSensor

    .. automethod:: pybricks.pupdevices.ColorSensor.ambient

    .. rubric:: Advanced color sensing

    .. blockimg:: pybricks_blockColor_ColorSensor_hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.detectable_colors

    .. rubric:: Built-in lights

    This sensor has 3 built-in lights. You can adjust the brightness of each
    light. If you use the sensor to measure something, the lights will
    be turned on or off as needed for the measurement.

    .. blockimg:: pybricks_blockLightOn_colorsensor_on

    .. blockimg:: pybricks_blockLightOn_colorsensor_on_list
        :stack:

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.on

    .. blockimg:: pybricks_blockLightOn_colorsensor_off

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.off


Examples
-------------------

Measuring color and reflection
******************************

.. literalinclude::
    ../../../examples/pup/sensor_color/color_print.py


Waiting for a color
*******************

.. literalinclude::
    ../../../examples/pup/sensor_color/wait_for_color.py


Reading *reflected* hue, saturation, and value
************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/hsv.py


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
    ../../../examples/pup/sensor_color/detectable_colors.py

Reading *ambient* hue, saturation, value, and color
***************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/color_ambient.py

Blinking the built-in lights
****************************

.. literalinclude::
    ../../../examples/pup/sensor_color/lights_blink.py

Turning off the lights when the program ends
**********************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/cleanup.py
