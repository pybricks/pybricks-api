City Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/cityhub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.CityHub
    :no-members:

    .. rubric:: Using the hub status light

    .. toggle-header::
        :header: **Show/hide examples**

        **Example 1: Turning the light on and off**

        .. literalinclude::
            ../../../examples/pup/hub_cityhub/light_off.py

        **Example 2: Changing brightness and using custom colors**

        .. literalinclude::
            ../../../examples/pup/hub_cityhub/light_hsv.py

        **Example 3: Making the light blink**

        .. literalinclude::
            ../../../examples/pup/hub_cityhub/light_blink.py

        **Example 4: Creating light animations**

        .. literalinclude::
            ../../../examples/pup/hub_cityhub/light_animate.py

    .. automethod:: pybricks.hubs::CityHub.light.on

    .. automethod:: pybricks.hubs::CityHub.light.off

    .. automethod:: pybricks.hubs::CityHub.light.blink

    .. automethod:: pybricks.hubs::CityHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::CityHub.battery.voltage

    .. automethod:: pybricks.hubs::CityHub.battery.current

