:mod:`hub4` -- LEGO® Power Functions 2.0 Hub 4
=====================================================

.. automodule:: hub4
    :no-members:


Light
-----

.. automethod:: hub4.light.color

    Example::

        # Make the light red
        hub4.light.color(Color.RED)

        # Wait
        wait(1000)

        # Turn the light off
        hub4.light.off()


.. automethod:: hub4.light.off

.. automethod:: hub4.light.brightness

Battery
-------

.. automethod:: hub4.battery.voltage

.. automethod:: hub4.battery.current
