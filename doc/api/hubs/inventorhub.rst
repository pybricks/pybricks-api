MINDSTORMS Inventor Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/inventorhub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.InventorHub
    :no-members:

    This class is identical to the
    :class:`PrimeHub <pybricks.hubs.PrimeHub>` class, except
    for the name.

    .. rubric:: Using the hub status light

    .. figure:: ../../api/images/primehub_light_label.png
        :width: 22 em

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Turning the light on and off**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/light_off.py

        **Example 2: Changing brightness and using custom colors**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/light_hsv.py

        **Example 3: Making the light blink**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/light_blink.py

        **Example 4: Creating light animations**

        .. literalinclude::
           ../../../examples/pup/hub_inventorhub/light_animate.py

    .. automethod:: pybricks.hubs::InventorHub.light.on

    .. automethod:: pybricks.hubs::InventorHub.light.off

    .. automethod:: pybricks.hubs::InventorHub.light.blink

    .. automethod:: pybricks.hubs::InventorHub.light.animate

    .. rubric:: Using the light matrix display

    .. figure:: ../../api/images/primehub_display_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::InventorHub.display.orientation

    .. automethod:: pybricks.hubs::InventorHub.display.off

    .. automethod:: pybricks.hubs::InventorHub.display.pixel

    .. automethod:: pybricks.hubs::InventorHub.display.image

    .. automethod:: pybricks.hubs::InventorHub.display.animate

    .. automethod:: pybricks.hubs::InventorHub.display.number

    .. automethod:: pybricks.hubs::InventorHub.display.char

    .. automethod:: pybricks.hubs::InventorHub.display.text

    .. rubric:: Using the buttons

    .. figure:: ../../api/images/primehub_buttons_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::InventorHub.buttons.pressed

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::InventorHub.battery.voltage

    .. automethod:: pybricks.hubs::InventorHub.battery.current

