.. pybricks-requirements::

Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.parameters.Color
    :no-members:

    .. rubric:: Saturated colors

    These colors have maximum saturation and brightness value.
    They differ only in hue.

    .. autoattribute:: RED

        .. pybricks-color:: RED

    .. autoattribute:: ORANGE

        .. pybricks-color:: ORANGE

    .. autoattribute:: YELLOW

        .. pybricks-color:: YELLOW

    .. autoattribute:: GREEN

        .. pybricks-color:: GREEN

    .. autoattribute:: CYAN

        .. pybricks-color:: CYAN

    .. autoattribute:: BLUE

        .. pybricks-color:: BLUE

    .. autoattribute:: VIOLET

        .. pybricks-color:: VIOLET

    .. autoattribute:: MAGENTA

        .. pybricks-color:: MAGENTA

    .. rubric:: Unsaturated colors

    These colors have zero hue and saturation. They differ only in brightness
    value.

    When detecting these colors using sensors, their values depend a lot
    on the distance to the object. If the distance between the sensor and the
    object is not constant in your robot, it is better to use only one of these
    colors in your programs.

    .. autoattribute:: WHITE

        .. pybricks-color:: WHITE

    .. autoattribute:: GRAY

        .. pybricks-color:: GRAY

    .. autoattribute:: BLACK

        This represents dark objects that still reflect
        a very small amount of light.

        .. pybricks-color:: BLACK

    .. autoattribute:: NONE

        This is total darkness, with no reflection or light at all.

        .. pybricks-color:: NONE

.. rubric:: Making your own colors

This example shows the basics of color properties, and how to define new colors.

.. literalinclude::
    ../../../examples/pup/parameters/color_basics.py

This example shows more advanced use cases of the ``Color`` class.

.. literalinclude::
    ../../../examples/pup/parameters/color_advanced.py
