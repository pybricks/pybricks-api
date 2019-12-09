.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: Motor and Sensor Ports

    +-----------------+-----------------+-----------------+-----------------+
    |.. data:: Port.A |.. data:: Port.B |.. data:: Port.C |.. data:: Port.D |
    +-----------------+-----------------+-----------------+-----------------+

    .. rubric:: Using the hub status light

    .. automethod:: pybricks._instances.light.on

    .. automethod:: pybricks._instances.light.off

        Example::

            # Initialize MoveHub at the top of your script
            hub = MoveHub()

            # Make the light red
            hub.light.on(Color.RED)

            # Wait
            wait(1000)

            # Turn the light off
            hub.light.off()

    .. rubric:: Using the battery

    .. automethod:: pybricks._instances.battery.voltage

    .. automethod:: pybricks._instances.battery.current
