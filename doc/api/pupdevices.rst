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

    .. autoattribute:: pybricks.pupdevices.Motor.control
        :annotation:


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

.. todo:: Support for this sensor is not yet implemented. API is experimental.

    Add image with numbered labels for light index

.. figure:: ../api/images/sensor_color.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.ColorSensor
    :no-members:

    .. rubric:: Built-in lights

    This sensor has 3 built-in lights. You can adjust the brightness of each
    light. If you use the sensor to measure something afterwards, the light
    automatically turns back on as needed for the measurement.

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.on

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.off


Ultrasonic Sensor
^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: Support for this sensor is not yet implemented. API is experimental.

    Flip image to ensure top/bottom left/right description is correct

.. figure:: ../api/images/sensor_ultrasonic.png
   :width: 35 %

.. autoclass:: pybricks.pupdevices.UltrasonicSensor
    :no-members:

    .. rubric:: Built-in lights

    This sensor has 4 built-in lights. You can adjust the brightness of each
    light.

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.on

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.off


.. Tilt Sensor
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. autoclass:: pybricks.pupdevices.TiltSensor
    :no-members:

    .. automethod:: neutral

    .. automethod:: acceleration

    .. automethod:: tilt

    .. automethod:: up


.. Remote Control
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. autoclass:: pybricks.pupdevices.RemoteControl
    :no-members:

    .. automethod:: pybricks.pupdevices::RemoteControl.light.on

    .. automethod:: pybricks.pupdevices::RemoteControl.light.off

    .. automethod:: pybricks.pupdevices::RemoteControl.buttons.pressed
