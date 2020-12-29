Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/sensor_colordistance.png
   :width: 35 %

.. toggle-header::
    :header: **Show/hide examples**


    **Example 1: Measuring color**

    .. literalinclude::
        ../../../examples/pup/sensor_color_distance/color_print.py


    **Example 2: Waiting for a color**

    .. literalinclude::
        ../../../examples/pup/sensor_color_distance/wait_for_color.py

    **Example 3: Measuring distance**

    .. literalinclude::
        ../../../examples/pup/sensor_color_distance/distance_blink.py

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. rubric:: Advanced color sensing

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Reading hue, saturation, and value**

        .. literalinclude::
            ../../../examples/pup/sensor_color_distance/hsv.py


        **Example 2: Changing the detectable colors**

        By default, the sensor is configured to detect red, yellow, green,
        blue, white, or ``None``, which suits many applications.

        For better results in your application, you can measure your desired
        colors in advance, and tell the sensor to look only for those colors.
        Be sure to measure them at the **same distance and light conditions**
        as in your final application. Then you'll get very accurate results
        even for colors that are otherwise hard to detect.

        .. literalinclude::
            ../../../examples/pup/sensor_color_distance/detectable_colors.py

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.detectable_colors

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. toggle-header::
        :header: **Show/hide examples**

        **Example: Blinking the built-in light**

        .. literalinclude::
            ../../../examples/pup/sensor_color_distance/distance_blink.py

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.off
