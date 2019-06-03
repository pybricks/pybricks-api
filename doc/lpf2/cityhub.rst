:mod:`cityhub` -- LEGO® Power Functions 2.0 City Hub
=====================================================

.. automodule:: cityhub
    :no-members:


Light
-----

.. automethod:: cityhub.light.color

    Example::

        # Make the light red
        cityhub.light.color(Color.RED)

        # Wait
        wait(1000)

        # Turn the light off
        cityhub.light.off()


.. automethod:: cityhub.light.off

.. automethod:: cityhub.light.brightness

Battery
-------

.. automethod:: cityhub.battery.voltage

.. automethod:: cityhub.battery.current
