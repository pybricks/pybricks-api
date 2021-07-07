City Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/cityhub.png
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
    ../../../examples/pup/hub_cityhub/light_off.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_cityhub/light_hsv.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_cityhub/light_blink.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_cityhub/light_animate.py

Button and system examples
----------------------------------

Using the stop button during your program
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_cityhub/button_single.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_cityhub/system_shutdown.py
