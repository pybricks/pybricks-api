.. pybricks-requirements:: technichub

Technic Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-technic.png
    :width: 40%

.. blockimg:: pybricks_variables_set_technic_hub_option0

.. blockimg:: pybricks_variables_set_technic_hub_option4

.. autoclass:: pybricks.hubs.TechnicHub
    :no-members:

    .. rubric:: Using the hub status light

    .. blockimg:: pybricks_blockLightOnColor_technichub_on

    .. automethod:: pybricks.hubs::TechnicHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_technichub_off

    .. automethod:: pybricks.hubs::TechnicHub.light.off

    .. automethod:: pybricks.hubs::TechnicHub.light.blink

    .. automethod:: pybricks.hubs::TechnicHub.light.animate

    .. rubric:: Using the IMU

    .. versionchanged:: 3.6

        The methods below now return calibrated data by default. Depending on
        the method used, this combines data from the accelerometer, gyroscope,
        with your calibration values. Use ``calibrated=False`` where applicable
        to get the raw data you got before.

    .. blockimg:: pybricks_blockImuStatus_TechnicHub_ready

    .. automethod:: pybricks.hubs::TechnicHub.imu.ready

    .. blockimg:: pybricks_blockImuStatus_TechnicHub_stationary

    .. automethod:: pybricks.hubs::TechnicHub.imu.stationary

    .. blockimg:: pybricks_blockImuUp_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.up

    .. blockimg:: pybricks_blockTilt_TechnicHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_TechnicHub_imu.tilt.roll
    
    .. automethod:: pybricks.hubs::TechnicHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.acceleration

    .. blockimg:: pybricks_blockImuRotation_TechnicHub_imu.angular_velocity

    .. automethod:: pybricks.hubs::TechnicHub.imu.angular_velocity

    .. blockimg:: pybricks_blockImuGetHeading_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.heading

    .. blockimg:: pybricks_blockImuResetHeading_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.reset_heading

    .. blockimg:: pybricks_blockImuRotation_TechnicHub_imu.rotation

    .. automethod:: pybricks.hubs::TechnicHub.imu.rotation

    .. automethod:: pybricks.hubs::TechnicHub.imu.orientation

    .. blockimg:: pybricks_blockImuConfigure_TechnicHub_imu.settings_heading_correction
    
    .. blockimg:: pybricks_blockImuConfigure_TechnicHub_imu.settings_angular_velocity_threshold
    
    .. blockimg:: pybricks_blockImuConfigure_TechnicHub_imu.settings_acceleration_threshold
    
    .. automethod:: pybricks.hubs::TechnicHub.imu.settings

    .. rubric:: Using connectionless Bluetooth messaging

    .. blockimg:: pybricks_blockBleBroadcast_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.ble.observe

    .. automethod:: pybricks.hubs::TechnicHub.ble.signal_strength

    .. automethod:: pybricks.hubs::TechnicHub.ble.version

    .. rubric:: Using the battery

    .. blockimg:: pybricks_blockBatteryMeasure_TechnicHub_battery.voltage

    .. automethod:: pybricks.hubs::TechnicHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_TechnicHub_battery.current

    .. automethod:: pybricks.hubs::TechnicHub.battery.current

    .. rubric:: Button and system control

    .. blockimg:: pybricks_blockButtonIsPressed_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.buttons.pressed

    .. blockimg:: pybricks_blockHubStopButton_TechnicHub

    .. blockimg:: pybricks_blockHubStopButton_TechnicHub_none
    
    .. automethod:: pybricks.hubs::TechnicHub.system.set_stop_button

    .. automethod:: pybricks.hubs::TechnicHub.system.storage

        You can store up to 128 bytes of data on this hub. The data is cleared
        when you update the Pybricks firmware or if you restore the original
        firmware.

    .. automethod:: pybricks.hubs::TechnicHub.system.reset_storage

    .. blockimg:: pybricks_blockHubShutdown_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.system.shutdown

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_technichub.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_technichub.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_technichub.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_technichub.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_technichub.py


Reading the tilt value
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_technichub.py

Using a custom hub orientation
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_technichub.py

Reading acceleration and angular velocity vectors
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_technichub.py

Reading acceleration and angular velocity on one axis
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_technichub.py


Bluetooth examples
------------------

Broadcasting data to other hubs
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_technichub.py

Observing data from other hubs
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_technichub.py


Button and system examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_technichub.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_technichub.py
