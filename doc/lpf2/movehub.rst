:mod:`movehub` -- LEGO® Power Functions 2.0 Move Hub
====================================================

.. automodule:: movehub
    :no-members:

Light
-----

.. automethod:: movehub.light.color

    Example::

        # Make the light red
        movehub.light.color(Color.RED)

        # Wait
        wait(1000)

        # Turn the light off
        movehub.light.off()


.. automethod:: movehub.light.off

.. automethod:: movehub.light.brightness

Battery
-------

.. automethod:: movehub.battery.voltage

.. automethod:: movehub.battery.current
