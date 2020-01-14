:mod:`resources <pybricks.resources>` -- Resources
==================================================

.. automodule:: pybricks.resources
    :no-members:

Graphical Images
^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.resources.Image
    :no-members:

    .. rubric:: Drawing Text

    There are two ways to draw text on images. :meth:`draw_text` lets text be
    placed precisely on the image or :meth:`print` can be used to automatically
    print text on a new line.

    .. automethod:: pybricks.resources.Image.draw_text

    .. automethod:: pybricks.resources.Image.print

    .. automethod:: pybricks.resources.Image.set_font


    .. rubric:: Drawing Images

    A copy of another image can be drawn on an image. Also consider using
    sub-images to copy part of an image.

    .. automethod:: pybricks.resources.Image.draw_image


    .. rubric:: Drawing Shapes

    These are the methods to draw basic shapes, including points, lines,
    rectangles and circles.

    .. automethod:: pybricks.resources.Image.draw_pixel

    .. automethod:: pybricks.resources.Image.draw_line

    .. automethod:: pybricks.resources.Image.draw_box

    .. automethod:: pybricks.resources.Image.draw_circle


    .. rubric:: Image properties

    .. autoattribute:: pybricks.resources.Image.width

    .. autoattribute:: pybricks.resources.Image.height


    .. rubric:: Replacing the Entire Image

    .. automethod:: pybricks.resources.Image.clear

    .. automethod:: pybricks.resources.Image.show_image


Fonts
^^^^^

.. autoclass:: pybricks.resources.Font
    :no-members:

    .. autoattribute:: pybricks.resources.Font.DEFAULT
        :annotation: = Font('Lucida', 12)

    .. autoattribute:: pybricks.resources.Font.family

    .. autoattribute:: pybricks.resources.Font.style

    .. autoattribute:: pybricks.resources.Font.width

    .. autoattribute:: pybricks.resources.Font.height

    .. automethod:: pybricks.resources.Font.text_width

    .. automethod:: pybricks.resources.Font.text_height
