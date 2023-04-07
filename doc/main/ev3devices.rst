:mod:`ev3devices <pybricks.ev3devices>` -- EV3 devices
======================================================

.. automodule:: pybricks.ev3devices
    :no-members:

Motors
^^^^^^^^^^^^

.. _fig_ev3motors:

.. figure:: ../main/diagrams/ev3motors.png
   :width: 100 %

   EV3-compatible motors. The arrows indicate the default positive direction.

.. autoclass:: pybricks.ev3devices.Motor
    :noindex:
    :no-members:

    .. rubric:: Measuring

    .. automethod:: pybricks.ev3devices.Motor.angle

    .. automethod:: pybricks.ev3devices.Motor.reset_angle

    .. automethod:: pybricks.ev3devices.Motor.speed

    .. automethod:: pybricks.ev3devices.Motor.load

    .. automethod:: pybricks.ev3devices.Motor.stalled

    .. rubric:: Stopping

    .. automethod:: pybricks.ev3devices.Motor.stop

    .. automethod:: pybricks.ev3devices.Motor.brake

    .. automethod:: pybricks.ev3devices.Motor.hold

    .. rubric:: Running forever

    .. automethod:: pybricks.ev3devices.Motor.run

    .. automethod:: pybricks.ev3devices.Motor.dc

    .. rubric:: Running by a fixed amount

    .. automethod:: pybricks.ev3devices.Motor.run_time

    .. automethod:: pybricks.ev3devices.Motor.run_angle

    .. automethod:: pybricks.ev3devices.Motor.run_target

    .. automethod:: pybricks.ev3devices.Motor.track_target

    .. automethod:: pybricks.ev3devices.Motor.run_until_stalled

    .. automethod:: pybricks.ev3devices.Motor.done

    .. rubric:: Motor settings

    .. automethod:: pybricks.ev3devices.Motor.settings

    .. rubric:: Control settings

    .. automethod:: pybricks.ev3devices.Motor.control.limits

    .. automethod:: pybricks.ev3devices.Motor.control.pid

    .. automethod:: pybricks.ev3devices.Motor.control.target_tolerances

    .. automethod:: pybricks.ev3devices.Motor.control.stall_tolerances

    .. attribute:: control.scale

        Number of degrees that the motor turns to complete one degree at the
        output of the gear train. This is the gear ratio determined from the
        ``gears`` argument when initializing the motor.

Touch Sensor
^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-touch.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.TouchSensor

Color Sensor
^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-color.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.ColorSensor

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each method of this class puts the sensor in a different *mode*. Switching
modes takes about one second on this sensor. To make sure that your program
runs quickly, use only of these methods in your program.

.. figure:: ../main/cad/output/ev3device-infrared.png
   :width: 60 %

.. autoclass:: pybricks.ev3devices.InfraredSensor

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-ultrasonic.png
   :width: 22 %

.. autoclass:: pybricks.ev3devices.UltrasonicSensor

Gyroscopic Sensor
^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-gyro.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.GyroSensor
    :no-members:

    .. automethod:: pybricks.ev3devices.GyroSensor.speed

    .. automethod:: pybricks.ev3devices.GyroSensor.angle

         If you use the :meth:`.angle` method, you cannot use the
         :meth:`.speed` method in the same program. Doing so would reset the
         sensor angle to zero every time you read the speed.

    .. automethod:: pybricks.ev3devices.GyroSensor.reset_angle
