.. pybricks-requirements:: cityhub

City Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/images/cityhub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.CityHub
    :no-members:

    .. rubric:: Using the hub status light

    .. automethod:: pybricks.hubs::CityHub.light.on

    .. automethod:: pybricks.hubs::CityHub.light.off

    .. automethod:: pybricks.hubs::CityHub.light.blink

    .. automethod:: pybricks.hubs::CityHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::CityHub.battery.voltage

    .. automethod:: pybricks.hubs::CityHub.battery.current

    .. rubric:: Button and system control

    .. automethod:: pybricks.hubs::CityHub.button.pressed

    .. automethod:: pybricks.hubs::CityHub.system.set_stop_button

    .. automethod:: pybricks.hubs::CityHub.system.name

    .. automethod:: pybricks.hubs::CityHub.system.shutdown

    .. automethod:: pybricks.hubs::CityHub.system.reset_reason

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_cityhub.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_cityhub.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_cityhub.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_cityhub.py

Button and system examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_cityhub.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_cityhub.py
