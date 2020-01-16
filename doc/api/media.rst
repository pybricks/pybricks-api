:mod:`media <pybricks.media>` -- Sounds and Images
==================================================

.. automodule:: pybricks.media
    :no-members:

You can use your own sound and image files by placing them in your project
folder. You can also use any of the images and sounds built into Pybricks.

ev3dev
------

.. automodule:: pybricks.media.ev3dev
    :no-members:

Images
^^^^^^

.. autoclass:: pybricks.media.ev3dev.ImageFile
    :no-members:

Sounds
^^^^^^

.. autoclass:: pybricks.media.ev3dev.SoundFile
    :no-members:


Fonts
^^^^^

.. autoclass:: pybricks.media.ev3dev.Font
    :no-members:

    .. autoattribute:: pybricks.media.ev3dev.Font.DEFAULT
        :annotation: = Font('Lucida', 12)

    .. autoattribute:: pybricks.media.ev3dev.Font.family

    .. autoattribute:: pybricks.media.ev3dev.Font.style

    .. autoattribute:: pybricks.media.ev3dev.Font.width

    .. autoattribute:: pybricks.media.ev3dev.Font.height

    .. automethod:: pybricks.media.ev3dev.Font.text_width

    .. automethod:: pybricks.media.ev3dev.Font.text_height

Making Images
^^^^^^^^^^^^^^^

.. todo::
    Explain what this is for, possibly with a sample.

.. autoclass:: pybricks.media.ev3dev.Image
    :no-members:

    .. rubric:: Drawing text

    There are two ways to draw text on images. :meth:`draw_text` lets text be
    placed precisely on the image or :meth:`print` can be used to automatically
    print text on a new line.

    .. automethod:: pybricks.media.ev3dev.Image.draw_text

    .. automethod:: pybricks.media.ev3dev.Image.print

    .. automethod:: pybricks.media.ev3dev.Image.set_font


    .. rubric:: Drawing images

    A copy of another image can be drawn on an image. Also consider using
    sub-images to copy part of an image.

    .. automethod:: pybricks.media.ev3dev.Image.draw_image


    .. rubric:: Drawing shapes

    These are the methods to draw basic shapes, including points, lines,
    rectangles and circles.

    .. automethod:: pybricks.media.ev3dev.Image.draw_pixel

    .. automethod:: pybricks.media.ev3dev.Image.draw_line

    .. automethod:: pybricks.media.ev3dev.Image.draw_box

    .. automethod:: pybricks.media.ev3dev.Image.draw_circle


    .. rubric:: Image properties

    .. autoattribute:: pybricks.media.ev3dev.Image.width

    .. autoattribute:: pybricks.media.ev3dev.Image.height


    .. rubric:: Replacing the entire image

    .. automethod:: pybricks.media.ev3dev.Image.clear

    .. automethod:: pybricks.media.ev3dev.Image.show_image




