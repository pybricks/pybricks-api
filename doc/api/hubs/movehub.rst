Move Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_movehub:

.. figure:: ../../api/images/movehub_label.png
    :height: 15 em

.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: Using the hub status light

    .. automethod:: pybricks.hubs::MoveHub.light.on

    .. automethod:: pybricks.hubs::MoveHub.light.off

    .. automethod:: pybricks.hubs::MoveHub.light.blink

    .. automethod:: pybricks.hubs::MoveHub.light.animate

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::MoveHub.battery.voltage

    .. automethod:: pybricks.hubs::MoveHub.battery.current

Status light examples
---------------------

Turning the light on and off
******************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/light_off.py

Making the light blink
******************************

.. literalinclude::
    ../../../examples/pup/hub_movehub/light_blink.py

