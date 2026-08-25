.. pybricks-requirements::

Motors with rotation sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupmotors:

.. figure:: ../../main/diagrams/pupmotors.png
   :width: 100 %
   :alt: pupmotors

   Powered Up motors with rotation sensors. The arrows indicate the default
   positive direction. See the :mod:`hubs <pybricks.hubs>` module for default
   directions of built-in motors.

.. blockimg:: pybricks_variables_set_motor

.. autoclass:: pybricks.pupdevices.Motor
    :no-members:

    .. rubric:: Measuring

    .. blockimg:: pybricks_blockMotorMeasure_motor_angle

    .. automethod:: angle

    .. blockimg:: pybricks_blockMotorResetAngle

    .. automethod:: reset_angle

    .. blockimg:: pybricks_blockMotorMeasure_motor_speed

    .. blockimg:: pybricks_blockMotorMeasure_motor_get_speed_average

    .. automethod:: speed

    .. blockimg:: pybricks_blockMotorMeasure_motor_load

    .. automethod:: load

    .. blockimg:: pybricks_blockMotorMeasure_motor_stalled

    .. automethod:: stalled

    .. rubric:: Stopping

    .. blockimg:: pybricks_blockMotorStop_Motor_coast

    .. automethod:: stop

    .. blockimg:: pybricks_blockMotorStop_Motor_brake

    .. automethod:: brake

    .. blockimg:: pybricks_blockMotorStop_Motor_hold

    .. automethod:: hold

    .. rubric:: Running forever

    .. blockimg:: pybricks_blockMotorRun_run

    .. automethod:: run

    .. blockimg:: pybricks_blockMotorDuty_Motor

    .. automethod:: dc

    .. rubric:: Running by a fixed amount

    .. automethod:: run_time

    .. blockimg:: pybricks_blockMotorRun_run_angle

    .. automethod:: run_angle

    .. blockimg:: pybricks_blockMotorRun_run_target

    .. automethod:: run_target

    .. blockimg:: pybricks_blockMotorRun_run_until_stalled

    .. automethod:: run_until_stalled

    .. blockimg:: pybricks_blockMotorTrack

    .. automethod:: track_target

    .. automethod:: done

    .. _settings:

    .. rubric:: Motor settings

    .. blockimg:: pybricks_blockMotorConfigure_motor_max_voltage

    .. automethod:: settings

    .. automethod:: close

    .. rubric:: Control settings

    .. pybricks-requirements:: pybricks-common-control

    .. blockimg:: pybricks_blockMotorConfigure_motor_max_speed

    .. blockimg:: pybricks_blockMotorConfigure_motor_acceleration

    .. blockimg:: pybricks_blockMotorConfigure_motor_max_torque

    .. autonestedmethod:: control.limits

    .. pybricks-requirements:: pybricks-common-control

    .. autonestedmethod:: control.pid

    .. pybricks-requirements:: pybricks-common-control

    .. blockimg:: pybricks_blockMotorConfigure_motor_target_tolerances

    .. autonestedmethod:: control.target_tolerances

    .. pybricks-requirements:: pybricks-common-control

    .. autonestedmethod:: control.stall_tolerances

    .. pybricks-requirements:: pybricks-common-control

    .. attribute:: control.scale

        Number of degrees that the motor turns to complete one degree at the
        output of the gear train. This is the gear ratio determined from the
        ``gears`` argument when initializing the motor.

    .. versionchanged:: 3.2

        The :meth:`done`, :meth:`stalled` and :meth:`load` methods have been
        moved.

    .. pybricks-requirements:: pybricks-common-control

    .. autonestedmethod:: model.state

    .. pybricks-requirements:: pybricks-common-control

    .. autonestedmethod:: model.settings

Initialization examples
-----------------------

Making the motor move back and forth
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_basic.py

Initializing multiple motors
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_multiple.py

Setting the positive direction as counterclockwise
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_direction.py

Using gears
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_gears.py

Measurement examples
-----------------------

Measuring the angle and speed
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_measure.py

Resetting the measured angle
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_reset_angle.py

Getting the absolute angle
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_absolute.py


Movement examples
-----------------------

Basic usage of all run methods
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_basic.py

Stopping ongoing movements in different ways
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_stop.py

Using the ``then`` argument to change how a run command stops
*************************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_then.py

Stall examples
-----------------------

Running a motor until a mechanical endpoint
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_until_stalled.py

Centering a steering mechanism
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_until_stalled_center.py


Parallel movement examples
--------------------------

Using the ``wait`` argument to run motors in parallel
*********************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_wait.py

Waiting for two parallel actions to complete
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_wait_advanced.py
