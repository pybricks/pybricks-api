Motors with Rotation Sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupmotors:

.. figure:: ../../api/images/pupmotors_label.png
   :width: 100 %
   :alt: pupmotors
   :align: left

   Powered Up motors with rotation sensors. The arrows indicate the default
   positive direction. See the :mod:`hubs <pybricks.hubs>` module for default
   directions of built-in motors.

.. autoclass:: pybricks.pupdevices.Motor
    :noindex:
    :no-members:

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Making the motor move back and forth**

        .. literalinclude::
            ../../../examples/pup/motor/motor_init_basic.py

        **Example 2: Using more than one motor**

        .. literalinclude::
            ../../../examples/pup/motor/motor_init_multiple.py

        **Example 3: Setting the positive direction as counterclockwise**

        .. literalinclude::
            ../../../examples/pup/motor/motor_init_direction.py

        **Example 4: Using gears**

        .. literalinclude::
            ../../../examples/pup/motor/motor_init_gears.py

    .. rubric:: Measuring

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Measuring the angle and speed**

        .. literalinclude::
            ../../../examples/pup/motor/motor_measure.py

        **Example 2: Resetting the measured angle**

        .. literalinclude::
            ../../../examples/pup/motor/motor_reset_angle.py

    .. automethod:: pybricks.pupdevices.Motor.speed

    .. automethod:: pybricks.pupdevices.Motor.angle

    .. automethod:: pybricks.pupdevices.Motor.reset_angle

    .. rubric:: Stopping

    .. toggle-header::
        :header: **Show/hide example**

        **Example: Stopping the motor in different ways**

        .. literalinclude::
            ../../../examples/pup/motor/motor_stop.py

    .. automethod:: pybricks.pupdevices.Motor.stop

    .. automethod:: pybricks.pupdevices.Motor.brake

    .. automethod:: pybricks.pupdevices.Motor.hold

    .. rubric:: Action

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Basic usage of all action methods**

        .. literalinclude::
            ../../../examples/pup/motor/motor_action_basic.py

        **Example 2: Using the** ``then`` **argument to change how a motor stops**

        .. literalinclude::
            ../../../examples/pup/motor/motor_action_then.py

        **Example 3: Using the** ``wait`` **argument to run motors in parallel**

        .. literalinclude::
            ../../../examples/pup/motor/motor_action_wait.py

        **Example 4: Waiting for two actions to complete in parallel**

        .. literalinclude::
            ../../../examples/pup/motor/motor_action_wait_advanced.py

        **Example 5: Running a motor until a mechanical endpoint**

        .. literalinclude::
            ../../../examples/pup/motor/motor_until_stalled.py

        **Example 6: Centering a steering mechanism**

        .. literalinclude::
            ../../../examples/pup/motor/motor_until_stalled.py


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
