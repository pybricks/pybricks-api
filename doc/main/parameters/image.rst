.. pybricks-requirements:: ev3

Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |this image| replace:: this image

.. autoclass:: pybricks.parameters.Image
    :no-members:

    .. automethod:: pybricks.parameters.Image.empty

    .. rubric:: Drawing text

    There are two ways to draw text on images. :meth:`draw_text` lets text be
    placed precisely on the image or :meth:`print` can be used to automatically
    print text on a new line.

    .. automethod:: pybricks.parameters.Image.draw_text

    .. automethod:: pybricks.parameters.Image.print

    .. automethod:: pybricks.parameters.Image.set_font


    .. rubric:: Drawing images

    A copy of another image can be drawn on an image. Also consider using
    sub-images to copy part of an image.

    .. automethod:: pybricks.parameters.Image.draw_image


    .. rubric:: Drawing shapes

    These are the methods to draw basic shapes, including points, lines,
    rectangles and circles.

    .. automethod:: pybricks.parameters.Image.draw_pixel

    .. automethod:: pybricks.parameters.Image.draw_line

    .. automethod:: pybricks.parameters.Image.draw_box

    .. automethod:: pybricks.parameters.Image.draw_circle


    .. rubric:: Image properties

    .. autoattribute:: pybricks.parameters.Image.width

    .. autoattribute:: pybricks.parameters.Image.height


    .. rubric:: Replacing the entire image

    .. automethod:: pybricks.parameters.Image.clear

    .. automethod:: pybricks.parameters.Image.load_image
