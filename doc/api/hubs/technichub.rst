Technic Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/technichub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.TechnicHub
    :no-members:

    .. rubric:: Using the hub status light

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Turning the light on and off**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_technichub/light_off.py

        **Example 2: Changing brightness and using custom colors**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_technichub/light_hsv.py

        **Example 3: Making the light blink**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_technichub/light_blink.py

        **Example 4: Creating light animations**

        .. literalinclude::
           ../../../pybricks-projects/snippets/pup/hub_technichub/light_animate.py

    .. automethod:: pybricks.hubs::TechnicHub.light.on

    .. automethod:: pybricks.hubs::TechnicHub.light.off

    .. automethod:: pybricks.hubs::TechnicHub.light.blink

    .. automethod:: pybricks.hubs::TechnicHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::TechnicHub.battery.voltage

    .. automethod:: pybricks.hubs::TechnicHub.battery.current

