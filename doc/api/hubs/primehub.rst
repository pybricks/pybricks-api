SPIKE Prime Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/primehub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.PrimeHub
    :no-members:

    This class is identical to the
    :class:`InventorHub <pybricks.hubs.InventorHub>` class, except
    for the name.

    .. rubric:: Using the hub status light

    .. figure:: ../../api/images/primehub_light_label.png
        :width: 22 em

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Turning the light on and off**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/light_off.py

        **Example 2: Changing brightness and using custom colors**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/light_hsv.py

        **Example 3: Making the light blink**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/light_blink.py

        **Example 4: Creating light animations**

        .. literalinclude::
           ../../../examples/pup/hub_primehub/light_animate.py

    .. automethod:: pybricks.hubs::PrimeHub.light.on

    .. automethod:: pybricks.hubs::PrimeHub.light.off

    .. automethod:: pybricks.hubs::PrimeHub.light.blink

    .. automethod:: pybricks.hubs::PrimeHub.light.animate

    .. rubric:: Using the light matrix display

    .. figure:: ../../api/images/primehub_display_label.png
        :width: 22 em

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Displaying images**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/display_image.py

        **Example 2: Displaying numbers**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/display_number.py

        **Example 3: Displaying text**

        .. literalinclude::
           ../../../examples/pup/hub_primehub/display_text.py

        **Example 4: Displaying individual pixels**

        .. literalinclude::
           ../../../examples/pup/hub_primehub/display_pixel.py

        **Example 5: Changing the display orientation**

        .. literalinclude::
           ../../../examples/pup/hub_primehub/display_orientation.py

        **Example 6: Making your own images**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/display_matrix.py

        **Example 7: Combining images to make expressions**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/display_expression.py

        **Example 8: Displaying animations**

        .. literalinclude::
           ../../../examples/pup/hub_primehub/display_animate.py

    .. automethod:: pybricks.hubs::PrimeHub.display.orientation

    .. automethod:: pybricks.hubs::PrimeHub.display.off

    .. automethod:: pybricks.hubs::PrimeHub.display.pixel

    .. automethod:: pybricks.hubs::PrimeHub.display.image

    .. automethod:: pybricks.hubs::PrimeHub.display.animate

    .. automethod:: pybricks.hubs::PrimeHub.display.number

    .. automethod:: pybricks.hubs::PrimeHub.display.char

    .. automethod:: pybricks.hubs::PrimeHub.display.text

    .. rubric:: Using the buttons

    .. figure:: ../../api/images/primehub_buttons_label.png
        :width: 22 em

    .. toggle-header::
        :header: **Show/hide examples**

        **Example: Detecting button presses**

        .. literalinclude::
            ../../../examples/pup/hub_primehub/button_main.py

    .. automethod:: pybricks.hubs::PrimeHub.buttons.pressed

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::PrimeHub.battery.voltage

    .. automethod:: pybricks.hubs::PrimeHub.battery.current

