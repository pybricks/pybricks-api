:mod:`ev3brick` -- The EV3 Programmable Brick
=============================================

.. automodule:: ev3brick
    :no-members:


Buttons
-------

.. autofunction:: ev3brick.buttons

    Examples::

        # Do something if the left button is pressed
        if Button.LEFT in brick.buttons():
            print("The left button is pressed.")

    ::

        # Wait until any of the buttons are pressed
        while not any(brick.buttons()):
            wait(10)

        # Wait until all buttons are released
        while any(brick.buttons()):
            wait(10)


Light
-----

.. automethod:: ev3brick.light.color

    Example::

        # Make the light red
        brick.light.color(Color.RED)

        # Wait
        wait(1000)

        # Turn the light off
        brick.light.off()


.. automethod:: ev3brick.light.off

.. automethod:: ev3brick.light.brightness

Sound
-----

.. automethod:: ev3brick.sound.beep

    Example::

        # A simple beep
        brick.sound.beep()

        # A high pitch (1500 Hz) for one second (1000 ms) at 50% volume
        brick.sound.beep(1500, 1000, 50)


.. automethod:: ev3brick.sound.beeps

    Example::

        # Make 5 simple beeps
        brick.sound.beeps(5)

.. automethod:: ev3brick.sound.file

    Example::

        # Play one of the built-in sounds
        brick.sound.file(SoundFile.HELLO)

        # Play a sound file from your project folder
        brick.sound.file('mysound.wav')

Display
-------
::

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


.. automethod:: ev3brick.display.clear

    Example::

        # Clear the display
        brick.display.clear()

.. automethod:: ev3brick.display.text

    Example::

        # Print ``Hello`` near the middle of the screen
        brick.display.text("Hello", (60, 50))

        # Print ``World`` directly underneath it
        brick.display.text("World")

.. automethod:: ev3brick.display.image

    Example::

        # Show a built-in image of two eyes looking upward
        brick.display.image(ImageFile.UP)

        # Display a custom image from your project folder
        brick.display.image('pybricks.png')

        # Display a custom image at the top right of the screen,
        # without clearing the screen first
        brick.display.image('arrow.png', Align.TOP_RIGHT, clear=False)

Battery
-------

.. automethod:: ev3brick.battery.voltage

.. automethod:: ev3brick.battery.current
