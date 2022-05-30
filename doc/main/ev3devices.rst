:mod:`ev3devices <pybricks.ev3devices>` -- EV3 devices
======================================================

.. automodule:: pybricks.ev3devices
    :no-members:

Motors
^^^^^^^^^^^^

.. _fig_ev3motors:

.. figure:: ../main/images/ev3motors_label.png
   :width: 100 %

   EV3-compatible motors. The arrows indicate the default positive direction.

.. autoclass:: pybricks.ev3devices.Motor
    :noindex:
    :no-members:

    .. rubric:: Measuring

    .. automethod:: pybricks.ev3devices.Motor.speed

    .. automethod:: pybricks.ev3devices.Motor.angle

    .. automethod:: pybricks.ev3devices.Motor.reset_angle

    .. rubric:: Stopping

    .. automethod:: pybricks.ev3devices.Motor.stop

    .. automethod:: pybricks.ev3devices.Motor.brake

    .. automethod:: pybricks.ev3devices.Motor.hold

    .. rubric:: Action

    .. automethod:: pybricks.ev3devices.Motor.run

    .. automethod:: pybricks.ev3devices.Motor.run_time

    .. automethod:: pybricks.ev3devices.Motor.run_angle

    .. automethod:: pybricks.ev3devices.Motor.run_target

    .. automethod:: pybricks.ev3devices.Motor.track_target

    .. automethod:: pybricks.ev3devices.Motor.run_until_stalled

    .. automethod:: pybricks.ev3devices.Motor.dc

    .. rubric:: Motor status

    .. attribute:: control.scale

        Number of degrees that the motor turns to complete one degree at the
        output of the gear train. This is the gear ratio determined from the
        ``gears`` argument when initializing the motor.

    .. automethod:: pybricks.ev3devices.Motor.control.done

    .. automethod:: pybricks.ev3devices.Motor.control.stalled

    .. automethod:: pybricks.ev3devices.Motor.control.load

    .. rubric:: Motor settings

    You can only change these settings while the controller is stopped. For
    example, you can change them at the start of your program. Alternatively,
    first call :meth:`stop() <pybricks.ev3devices.Motor.stop>`, and then change
    the settings.

    .. automethod:: pybricks.ev3devices.Motor.settings

    .. automethod:: pybricks.ev3devices.Motor.control.limits

    .. automethod:: pybricks.ev3devices.Motor.control.pid

    .. automethod:: pybricks.ev3devices.Motor.control.target_tolerances

    .. automethod:: pybricks.ev3devices.Motor.control.stall_tolerances

Touch Sensor
^^^^^^^^^^^^

.. figure:: ../main/images/sensor_ev3_touch.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.TouchSensor

Color Sensor
^^^^^^^^^^^^

.. figure:: ../main/images/sensor_ev3_color.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.ColorSensor

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each method of this class puts the sensor in a different *mode*. Switching
modes takes about one second on this sensor. To make sure that your program
runs quickly, use only of these methods in your program.

.. figure:: ../main/images/sensor_ev3_ir.png
   :width: 60 %

.. autoclass:: pybricks.ev3devices.InfraredSensor

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^

.. figure:: ../main/images/sensor_ev3_ultrasonic.png
   :width: 22 %

.. autoclass:: pybricks.ev3devices.UltrasonicSensor

Gyroscopic Sensor
^^^^^^^^^^^^^^^^^

.. figure:: ../main/images/sensor_ev3_gyro.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.GyroSensor
    :no-members:

    .. automethod:: pybricks.ev3devices.GyroSensor.speed

    .. automethod:: pybricks.ev3devices.GyroSensor.angle

         If you use the :meth:`.angle` method, you cannot use the
         :meth:`.speed` method in the same program. Doing so would reset the
         sensor angle to zero every time you read the speed.

    .. automethod:: pybricks.ev3devices.GyroSensor.reset_angle
