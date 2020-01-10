.. autoclass:: pybricks.hubs.EV3Brick
    :no-members:

    .. rubric:: Using the buttons

    .. automethod:: pybricks._instances.buttons.pressed

    .. rubric:: Using the brick status light

    .. automethod:: pybricks._instances.light.on

        .. toggle-header::
            :header: **Show/hide example**

            **Example: Turn the light on and change the color.**

            .. literalinclude:: ../../pybricks-projects/snippets/ev3/light_color/main.py

    .. automethod:: pybricks._instances.light.off

    .. rubric:: Using the speaker

    .. automethod:: pybricks._instances.speaker.volume

    .. automethod:: pybricks._instances.speaker.beep

    .. automethod:: pybricks._instances.speaker.play

    .. todo:: The following functionality is not yet implemented

    .. automethod:: pybricks._instances.speaker.say

    .. todo:: The following functionality is not yet implemented

    .. automethod:: pybricks._instances.speaker.set_voice_settings

.. todo:: This functionality is not yet implemented

.. rubric:: Using the screen

.. todo:: This functionality is not yet implemented

..  ::

                        x
                -------------->
        (0, 0)  __________________
                |                  |
            |   |                  |
         y  |   |      Hello       |
            |   |      World       |
            v   |                  |
                |__________________|
                                    (177, 127)

..    .. automethod:: pybricks._instances.display.clear

..    .. automethod:: pybricks._instances.display.text

..    .. automethod:: pybricks._instances.display.image

    .. rubric:: Using the battery

    .. automethod:: pybricks._instances.battery.voltage

    .. automethod:: pybricks._instances.battery.current
