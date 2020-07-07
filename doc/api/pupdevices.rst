:mod:`pupdevices <pybricks.pupdevices>` -- Powered Up Devices
=============================================================

.. automodule:: pybricks.pupdevices
    :no-members:

Motors without Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupdcmotors:

.. figure:: ../api/images/pupdcmotors_label.png
   :width: 70 %
   :alt: pupmotors
   :align: center

   Powered Up motors without rotation sensors. The arrows indicate the default
   positive direction.

.. autoclass:: pybricks._common.DCMotor
    :noindex:
    :no-members:

    .. automethod:: pybricks._common.DCMotor.dc
        :noindex:

    .. automethod:: pybricks._common.DCMotor.stop
        :noindex:

    .. automethod:: pybricks._common.DCMotor.brake
        :noindex:

Motors with Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupmotors:

.. figure:: ../api/images/pupmotors_label.png
   :width: 100 %
   :alt: pupmotors
   :align: left

   Powered Up motors with rotation sensors. The arrows indicate the default
   positive direction. See the :mod:`hubs <pybricks.hubs>` module for default
   directions of built-in motors.

.. autoclass:: pybricks.pupdevices.Motor
    :noindex:
    :no-members:

    .. rubric:: Measuring

    .. automethod:: pybricks.pupdevices.Motor.speed

    .. automethod:: pybricks.pupdevices.Motor.angle

    .. automethod:: pybricks.pupdevices.Motor.reset_angle

    .. rubric:: Stopping

    .. automethod:: pybricks.pupdevices.Motor.stop

    .. automethod:: pybricks.pupdevices.Motor.brake

    .. automethod:: pybricks.pupdevices.Motor.hold

    .. rubric:: Action

    .. automethod:: pybricks.pupdevices.Motor.run

    .. automethod:: pybricks.pupdevices.Motor.run_time

    .. automethod:: pybricks.pupdevices.Motor.run_angle

    .. automethod:: pybricks.pupdevices.Motor.run_target

    .. automethod:: pybricks.pupdevices.Motor.run_until_stalled

    .. automethod:: pybricks.pupdevices.Motor.dc

    .. rubric:: Advanced motion control

    .. automethod:: pybricks.pupdevices.Motor.track_target

    .. autoattribute:: pybricks.ev3devices.Motor.control
        :annotation:
        :noindex:

.. FIXME: above should point to pupdevices but inherited class attributes
   do not work yet (https://github.com/sphinx-doc/sphinx/issues/741).


Color and Distance Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_colordistance.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.remote

    .. rubric:: Built-in light

    This sensor has a built-in light. You can make it red, green, blue, or turn
    it off. If you use the sensor to measure something afterwards, the light
    automatically turns back on at the default color for that sensing method.

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.off


Color Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_color_lights_label.png
   :width: 70 %

.. autoclass:: pybricks.pupdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorSensor.color

    .. automethod:: pybricks.pupdevices.ColorSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.color_map

    .. automethod:: pybricks.pupdevices.ColorSensor.ambient

    .. automethod:: pybricks.pupdevices.ColorSensor.reflection

    .. rubric:: Built-in lights

    This sensor has 3 built-in lights. You can adjust the brightness of each
    light. If you use the sensor to measure something, the lights will
    be turned on or off as needed for the measurement.

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.on

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.off


Ultrasonic Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_ultrasonic_lights_label.png
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

Force Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_force.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.ForceSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ForceSensor.force

    .. automethod:: pybricks.pupdevices.ForceSensor.distance

    .. automethod:: pybricks.pupdevices.ForceSensor.pressed

    .. automethod:: pybricks.pupdevices.ForceSensor.touched

Infrared Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_proximity.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.InfraredSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.InfraredSensor.distance

    .. automethod:: pybricks.pupdevices.InfraredSensor.reflection

    .. automethod:: pybricks.pupdevices.InfraredSensor.count


Tilt Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/sensor_tilt.png
   :width: 35 %


.. autoclass:: pybricks.pupdevices.TiltSensor
    :no-members:

    .. automethod:: tilt

..    .. automethod:: neutral

..    .. automethod:: acceleration

..    .. automethod:: up


.. Remote Control
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. autoclass:: pybricks.pupdevices.RemoteControl
    :no-members:

    .. automethod:: pybricks.pupdevices::RemoteControl.light.on

    .. automethod:: pybricks.pupdevices::RemoteControl.light.off

    .. automethod:: pybricks.pupdevices::RemoteControl.buttons.pressed

Light
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../api/images/light.png
   :width: 90 %

.. autoclass:: pybricks.pupdevices.Light
    :no-members:

    .. automethod:: pybricks.pupdevices.Light.on

    .. automethod:: pybricks.pupdevices.Light.off

..    .. automethod:: pybricks.pupdevices.Light.pattern
