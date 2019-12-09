.. autoclass:: pybricks.hubs.EV3Brick
    :no-members:

    .. rubric:: Motor and Sensor Ports

    +-----------------+-----------------+-----------------+-----------------+
    |.. data:: Port.A |.. data:: Port.B |.. data:: Port.C |.. data:: Port.D |
    +-----------------+-----------------+-----------------+-----------------+
    |.. data:: Port.S1|.. data:: Port.S2|.. data:: Port.S3|.. data:: Port.S4|
    +-----------------+-----------------+-----------------+-----------------+

    .. rubric:: Using the buttons

    .. automethod:: pybricks._instances.buttons.pressed

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # Wait until any of the buttons are pressed
            while not any(brick.buttons.pressed()):
                wait(10)

            # Do something if the left button is pressed
            if Button.LEFT in brick.buttons.pressed():
                print("The left button is pressed.")

            # Wait until all buttons are released
            while any(brick.buttons.pressed()):
                wait(10)


    .. rubric:: Using the brick status light

    .. automethod:: pybricks._instances.light.on

    .. automethod:: pybricks._instances.light.off

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # Make the light red
            brick.light.on(Color.RED)

            # Wait
            wait(1000)

            # Turn the light off
            brick.light.off()

    .. rubric:: Using the speaker

    .. automethod:: pybricks._instances.speaker.beep

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # A simple beep
            brick.speaker.beep()

            # A high pitch (1500 Hz) for one second (1000 ms) at 50% volume
            brick.speaker.beep(1500, 1000, 50)


    .. automethod:: pybricks._instances.speaker.beeps

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # Make 5 simple beeps
            brick.speaker.beeps(5)

    .. automethod:: pybricks._instances.speaker.file

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # Play one of the built-in sounds
            brick.speaker.file(SoundFile.HELLO)

            # Play a sound file from your project folder
            brick.speaker.file('mysound.wav')

    .. rubric:: Using the display

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

    .. automethod:: pybricks._instances.display.clear

    .. automethod:: pybricks._instances.display.text

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # Clear the display
            brick.display.clear()

            # Print ``Hello`` near the middle of the screen
            brick.display.text("Hello", (60, 50))

            # Print ``World`` directly underneath it
            brick.display.text("World")

    .. automethod:: pybricks._instances.display.image

        Example::

            # Initialize EV3 at the top of your script
            brick = EV3Brick()

            # Show a built-in image of two eyes looking upward
            brick.display.image(ImageFile.UP)

            # Display a custom image from your project folder
            brick.display.image('pybricks.png')

            # Display a custom image at the top right of the screen,
            # without clearing the screen first
            brick.display.image('arrow.png', Align.TOP_RIGHT, clear=False)

    .. rubric:: Using the battery

    .. automethod:: pybricks._instances.battery.voltage

    .. automethod:: pybricks._instances.battery.current
