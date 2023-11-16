.. pybricks-requirements:: essentialhub

Essential Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-essential.png
    :width: 30%

.. blockimg:: pybricks_variables_set_essential_hub_option0

.. blockimg:: pybricks_variables_set_essential_hub_option4
    :stack:

.. autoclass:: pybricks.hubs.EssentialHub
    :no-members:

    .. rubric:: Using the hub status light

    .. blockimg:: pybricks_blockLightOnColor_essentialhub_on

    .. automethod:: pybricks.hubs::EssentialHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_essentialhub_off

    .. automethod:: pybricks.hubs::EssentialHub.light.off

    .. automethod:: pybricks.hubs::EssentialHub.light.blink

    .. automethod:: pybricks.hubs::EssentialHub.light.animate

    .. rubric:: Using the button

    .. blockimg:: pybricks_blockButtonIsPressed_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.button.pressed

    .. automethod:: pybricks.hubs::EssentialHub.system.set_stop_button

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::EssentialHub.imu.ready

    .. automethod:: pybricks.hubs::EssentialHub.imu.stationary

    .. automethod:: pybricks.hubs::EssentialHub.imu.up

    .. blockimg:: pybricks_blockTilt_EssentialHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_EssentialHub_imu.tilt.roll
        :stack:

    .. automethod:: pybricks.hubs::EssentialHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.acceleration

    .. blockimg:: pybricks_blockImuRotation_EssentialHub_imu.angular_velocity

    .. automethod:: pybricks.hubs::EssentialHub.imu.angular_velocity

    .. blockimg:: pybricks_blockImuGetHeading_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.heading

    .. blockimg:: pybricks_blockImuResetHeading_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.reset_heading

    .. blockimg:: pybricks_blockImuRotation_EssentialHub_imu.rotation

    .. automethod:: pybricks.hubs::EssentialHub.imu.rotation

    .. automethod:: pybricks.hubs::EssentialHub.imu.orientation

    .. automethod:: pybricks.hubs::EssentialHub.imu.settings

    .. rubric:: Using connectionless Bluetooth messaging

    .. blockimg:: pybricks_blockBleBroadcast_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.ble.observe

    .. automethod:: pybricks.hubs::EssentialHub.ble.signal_strength

    .. automethod:: pybricks.hubs::EssentialHub.ble.version

    .. rubric:: Using the battery

    .. blockimg:: pybricks_blockBatteryMeasure_EssentialHub_battery.voltage

    .. automethod:: pybricks.hubs::EssentialHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_EssentialHub_battery.current

    .. automethod:: pybricks.hubs::EssentialHub.battery.current

    .. rubric:: Getting the charger status

    .. automethod:: pybricks.hubs::EssentialHub.charger.connected

    .. automethod:: pybricks.hubs::EssentialHub.charger.current

    .. automethod:: pybricks.hubs::EssentialHub.charger.status

    .. rubric:: System control

    .. automethod:: pybricks.hubs::EssentialHub.system.name

    .. automethod:: pybricks.hubs::EssentialHub.system.storage

        You can store up to 512 bytes of data on this hub.

    .. automethod:: pybricks.hubs::EssentialHub.system.shutdown

    .. automethod:: pybricks.hubs::EssentialHub.system.reset_reason

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_essentialhub.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_essentialhub.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_essentialhub.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_essentialhub.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_essentialhub.py


Reading the tilt value
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_essentialhub.py

Using a custom hub orientation
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_essentialhub.py

Reading acceleration and angular velocity vectors
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_essentialhub.py

Reading acceleration and angular velocity on one axis
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_essentialhub.py


Bluetooth examples
------------------

Broadcasting data to other hubs
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_essentialhub.py

Observing data from other hubs
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_essentialhub.py


System examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_essentialhub.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_essentialhub.py
