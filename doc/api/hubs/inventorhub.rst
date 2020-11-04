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

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::InventorHub.battery.voltage

    .. automethod:: pybricks.hubs::InventorHub.battery.current

