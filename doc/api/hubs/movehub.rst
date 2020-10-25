BOOST Move Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_movehub:

.. figure:: ../../api/images/movehub_label.png
    :height: 15 em

.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: Using the hub status light

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Turning the light on and off**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_movehub/light_off.py

        **Example 2: Changing brightness and using custom colors**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_movehub/light_hsv.py

        **Example 3: Making the light blink**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_movehub/light_blink.py

        **Example 4: Creating light animations**

        .. literalinclude::
            ../../../pybricks-projects/snippets/pup/hub_movehub/light_animate.py

    .. automethod:: pybricks.hubs::MoveHub.light.on

    .. automethod:: pybricks.hubs::MoveHub.light.off

    .. automethod:: pybricks.hubs::MoveHub.light.blink

    .. automethod:: pybricks.hubs::MoveHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::MoveHub.battery.voltage

    .. automethod:: pybricks.hubs::MoveHub.battery.current
