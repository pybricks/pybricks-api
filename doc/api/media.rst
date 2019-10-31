:mod:`media` -- Sounds and Images
=============================================

You can use your own sound and image files by placing them in your project
folder. You can also use any of the images and sounds built into Pybricks.

ev3dev
------

These images and sounds are only available for Pybricks on ev3dev. Example::

    # Imports
    from pybricks.hubs import EV3Brick
    from pybricks.media.ev3dev import SoundFile, ImageFile

    # Initialize the EV3 brick
    brick = EV3Brick()

    # Show an image file
    brick.display.image(ImageFile.AWAKE)

    # Play a sound file
    brick.speaker.file(SoundFile.HELLO)

.. autoclass:: pybricks.media.ev3dev.ImageFile
    :no-members:

.. autoclass:: pybricks.media.ev3dev.SoundFile
    :no-members:
