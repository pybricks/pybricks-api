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

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Displaying images**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/display_image.py

        **Example 2: Displaying numbers**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/display_number.py

        **Example 3: Displaying text**

        .. literalinclude::
           ../../../examples/pup/hub_inventorhub/display_text.py

        **Example 4: Displaying individual pixels**

        .. literalinclude::
           ../../../examples/pup/hub_inventorhub/display_pixel.py

        **Example 5: Changing the display orientation**

        .. literalinclude::
           ../../../examples/pup/hub_inventorhub/display_orientation.py

        **Example 6: Making your own images**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/display_matrix.py

        **Example 7: Combining images to make expressions**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/display_expression.py

        **Example 8: Displaying animations**

        .. literalinclude::
           ../../../examples/pup/hub_inventorhub/display_animate.py

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

    .. toggle-header::
        :header: **Show/hide examples**

        **Example: Detecting button presses**

        .. literalinclude::
            ../../../examples/pup/hub_inventorhub/button_main.py

    .. automethod:: pybricks.hubs::InventorHub.buttons.pressed

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::InventorHub.battery.voltage

    .. automethod:: pybricks.hubs::InventorHub.battery.current

