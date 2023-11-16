.. pybricks-requirements:: movehub

Move Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_movehub:

.. figure:: ../../main/diagrams/movehub.png
    :width: 100%

.. blockimg:: pybricks_variables_set_move_hub_option0

.. blockimg:: pybricks_variables_set_move_hub_option4
    :stack:

.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: Using the hub status light

    .. blockimg:: pybricks_blockLightOnColor_movehub_on

    .. automethod:: pybricks.hubs::MoveHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_movehub_off

    .. automethod:: pybricks.hubs::MoveHub.light.off

    .. automethod:: pybricks.hubs::MoveHub.light.blink

    .. automethod:: pybricks.hubs::MoveHub.light.animate

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::MoveHub.imu.up

    .. blockimg:: pybricks_blockTilt_MoveHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_MoveHub_imu.tilt.roll
        :stack:

    .. automethod:: pybricks.hubs::MoveHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_MoveHub

    .. automethod:: pybricks.hubs::MoveHub.imu.acceleration

        .. versionchanged:: 3.2

            Changed acceleration units from m/s² to mm/s².

    .. rubric:: Using connectionless Bluetooth messaging

    .. blockimg:: pybricks_blockBleBroadcast_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.ble.observe

    .. automethod:: pybricks.hubs::MoveHub.ble.signal_strength

    .. automethod:: pybricks.hubs::MoveHub.ble.version

    .. rubric:: Using the battery

    .. blockimg:: pybricks_blockBatteryMeasure_MoveHub_battery.voltage

    .. automethod:: pybricks.hubs::MoveHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_MoveHub_battery.current

    .. automethod:: pybricks.hubs::MoveHub.battery.current

    .. rubric:: Button and system control

    .. blockimg:: pybricks_blockButtonIsPressed_PrimeHub

    .. automethod:: pybricks.hubs::MoveHub.button.pressed

    .. automethod:: pybricks.hubs::MoveHub.system.set_stop_button

    .. automethod:: pybricks.hubs::MoveHub.system.name

    .. automethod:: pybricks.hubs::MoveHub.system.storage

        You can store up to 128 bytes of data on this hub. The data is cleared
        when you update the Pybricks firmware or if you restore the original
        firmware.

    .. automethod:: pybricks.hubs::MoveHub.system.shutdown

    .. automethod:: pybricks.hubs::MoveHub.system.reset_reason

Status light examples
---------------------

Turning the light on and off
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_movehub.py

Making the light blink
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_movehub.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_movehub.py

Reading acceleration
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/imu_read_acceleration.py


Bluetooth examples
------------------

Broadcasting data to other hubs
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_movehub.py

Observing data from other hubs
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_movehub.py


Button and system examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_movehub.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_movehub.py

Making random numbers
**************************************************

The Move Hub does not include the :mod:`urandom` module. If you need random
numbers in your application, you can try a variation of the following example.

To make it work better, change the initial value of ``_rand`` to something
that is truly random in your application. You could use the IMU acceleration
or a sensor value, for example.

.. literalinclude::
    ../../../examples/pup/hub_movehub/randint_implementation.py
