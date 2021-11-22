.. pybricks-requirements:: technichub

Technic Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/images/technichub.png
    :height: 15 em

.. class:: TechnicHub

    LEGO® Technic Hub.

    .. rubric:: Using the hub status light

    .. automethod:: pybricks.hubs::TechnicHub.light.on

    .. automethod:: pybricks.hubs::TechnicHub.light.off

    .. automethod:: pybricks.hubs::TechnicHub.light.blink

    .. automethod:: pybricks.hubs::TechnicHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::TechnicHub.battery.voltage

    .. automethod:: pybricks.hubs::TechnicHub.battery.current

    .. rubric:: Button and system control

    .. automethod:: pybricks.hubs::TechnicHub.button.pressed

    .. automethod:: pybricks.hubs::TechnicHub.system.set_stop_button

    .. automethod:: pybricks.hubs::TechnicHub.system.name

    .. automethod:: pybricks.hubs::TechnicHub.system.shutdown

    .. automethod:: pybricks.hubs::TechnicHub.system.reset_reason

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

Button and system examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/button_single.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_technichub/system_shutdown.py
