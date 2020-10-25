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

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Turning the light on and off**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_primehub/light_off.py

        **Example 2: Changing brightness and using custom colors**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_primehub/light_hsv.py

        **Example 3: Making the light blink**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_primehub/light_blink.py

        **Example 4: Creating light animations**

        .. literalinclude::
           ../../../pybricks-projects/snippets/pup/hub_primehub/light_animate.py

    .. automethod:: pybricks.hubs::PrimeHub.light.on

    .. automethod:: pybricks.hubs::PrimeHub.light.off

    .. automethod:: pybricks.hubs::PrimeHub.light.blink

    .. automethod:: pybricks.hubs::PrimeHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::PrimeHub.battery.voltage

    .. automethod:: pybricks.hubs::PrimeHub.battery.current

