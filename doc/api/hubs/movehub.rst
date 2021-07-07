Move Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_movehub:

.. figure:: ../../api/images/movehub_label.png
    :height: 15 em

.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: Using the hub status light

    .. automethod:: pybricks.hubs::MoveHub.light.on

    .. automethod:: pybricks.hubs::MoveHub.light.off

    .. automethod:: pybricks.hubs::MoveHub.light.blink

    .. automethod:: pybricks.hubs::MoveHub.light.animate

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::MoveHub.imu.up

    .. automethod:: pybricks.hubs::MoveHub.imu.acceleration

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::MoveHub.battery.voltage

    .. automethod:: pybricks.hubs::MoveHub.battery.current

    .. rubric:: Button and system control

    .. automethod:: pybricks.hubs::MoveHub.button.pressed

    .. automethod:: pybricks.hubs::MoveHub.system.set_stop_button

    .. automethod:: pybricks.hubs::MoveHub.system.name

    .. automethod:: pybricks.hubs::MoveHub.system.shutdown

    .. automethod:: pybricks.hubs::MoveHub.system.reset_reason

Status light examples
---------------------

Turning the light on and off
******************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/light_off.py

Making the light blink
******************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/light_blink.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/imu_up.py

Reading acceleration
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/imu_read_acceleration.py

Button and system examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/button_single.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/system_shutdown.py
