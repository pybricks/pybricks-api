.. pybricks-requirements:: essentialhub

Essential Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/images/primehub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.EssentialHub
    :no-members:

    .. rubric:: Using the hub status light

    .. figure:: ../../main/images/primehub_light_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::EssentialHub.light.on

    .. automethod:: pybricks.hubs::EssentialHub.light.off

    .. automethod:: pybricks.hubs::EssentialHub.light.blink

    .. automethod:: pybricks.hubs::EssentialHub.light.animate

    .. rubric:: Using the button

    .. figure:: ../../main/images/primehub_buttons_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::EssentialHub.button.pressed

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::EssentialHub.imu.up

    .. automethod:: pybricks.hubs::EssentialHub.imu.tilt

    .. automethod:: pybricks.hubs::EssentialHub.imu.acceleration

    .. automethod:: pybricks.hubs::EssentialHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::EssentialHub.imu.heading

    .. automethod:: pybricks.hubs::EssentialHub.imu.reset_heading

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::EssentialHub.battery.voltage

    .. automethod:: pybricks.hubs::EssentialHub.battery.current

    .. rubric:: Getting the charger status

    .. automethod:: pybricks.hubs::EssentialHub.charger.connected

    .. automethod:: pybricks.hubs::EssentialHub.charger.current

    .. automethod:: pybricks.hubs::EssentialHub.charger.status

    .. rubric:: System control

    .. automethod:: pybricks.hubs::EssentialHub.system.set_stop_button

    .. automethod:: pybricks.hubs::EssentialHub.system.name

    .. automethod:: pybricks.hubs::EssentialHub.system.shutdown

    .. automethod:: pybricks.hubs::EssentialHub.system.reset_reason

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/light_off.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/light_hsv.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/light_blink.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/light_animate.py

Button examples
---------------

Detecting button presses
************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/button_single.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/imu_up.py


Reading the tilt value
********************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/imu_tilt.py

Using a custom hub orientation
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/imu_tilt_blast.py

Reading acceleration and angular velocity vectors
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/imu_read_vector.py

Reading acceleration and angular velocity on one axis
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/imu_read_scalar.py

System examples
----------------------------------

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_essentialhub/system_shutdown.py
