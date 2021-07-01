Technic Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/technichub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.TechnicHub
    :no-members:

    .. rubric:: Using the hub status light

    .. automethod:: pybricks.hubs::TechnicHub.light.on

    .. automethod:: pybricks.hubs::TechnicHub.light.off

    .. automethod:: pybricks.hubs::TechnicHub.light.blink

    .. automethod:: pybricks.hubs::TechnicHub.light.animate

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::TechnicHub.imu.up

    .. automethod:: pybricks.hubs::TechnicHub.imu.tilt

    .. automethod:: pybricks.hubs::TechnicHub.imu.acceleration

    .. automethod:: pybricks.hubs::TechnicHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::TechnicHub.imu.heading

    .. automethod:: pybricks.hubs::TechnicHub.imu.reset_heading

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::TechnicHub.battery.voltage

    .. automethod:: pybricks.hubs::TechnicHub.battery.current

    .. rubric:: System control

    .. automethod:: pybricks.hubs::MoveHub.system.reset

    .. automethod:: pybricks.hubs::MoveHub.system.reset_reason

    .. automethod:: pybricks.hubs::MoveHub.system.set_stop_button

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/light_off.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/light_hsv.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_technichub/light_blink.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/light_animate.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/imu_up.py


Reading the tilt value
********************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/imu_tilt.py

Using a custom hub orientation
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/imu_tilt_blast.py

Reading acceleration and angular velocity vectors
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/imu_read_vector.py

Reading acceleration and angular velocity on one axis
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/imu_read_scalar.py
