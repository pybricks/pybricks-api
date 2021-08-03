.. pybricks-requirements::

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/images/sensor_ultrasonic_lights_label.png
   :width: 80 %

.. autoclass:: pybricks.pupdevices.UltrasonicSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.distance

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.presence

    .. rubric:: Built-in lights

    This sensor has 4 built-in lights. You can adjust the brightness of each
    light.

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.on

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.off

Examples
-------------------

Measuring distance and switching on the lights
**********************************************

.. literalinclude::
    ../../../examples/pup/sensor_ultrasonic/basics.py

Gradually change the brightness of the lights
**********************************************

.. literalinclude::
    ../../../examples/pup/sensor_ultrasonic/math.py
