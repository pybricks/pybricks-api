"""Resources module for the Pybricks API."""

from .parameters import Color


class Image:
    """Object representing a graphics image. This can either be an in-memory
    copy of an image or the image displayed on a screen."""

    def __init__(self, source, sub=False):
        """
        Arguments:
            source (str or Image):
                The source of the image.

                If ``source`` is a string, then the image will be loaded from
                the file path given by the string. Only ``.png`` files are
                supported. As a special case, if the string is ``_screen_``,
                the image will be configured to draw directly on the screen.

                If an :class:`Image` is given, the new object will contain a
                copy of the ``source`` image object.

            sub (bool):
                If ``sub`` is ``True``, then the image object will act as a
                sub-image of the ``source`` image (this only works if the type
                of ``source`` is :class:`Image` and not when it is a ``str``).

                Additional keyword arguments ``x1``, ``y1`, ``x2``, ``y2`` are
                needed when ``sub=True``. These specify the top-left and
                bottom-right coordinates in the ``source`` image that will be
                used as the bounds for the sub-image.
        """
        pass

    @property
    def width(self):
        """Gets the width of the image in pixels."""
        return 0

    @property
    def height(self):
        """Gets the height of the image in pixels."""
        return 0

    def clear(self):
        """Clears the image. All pixels in the image will be set to
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.
        """
        pass

    def draw_pixel(self, x, y, color=Color.BLACK):
        """Draws a single pixel on the image.

        Arguments:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            color (Color): The color of the pixel.
        """
        pass

    def draw_line(self, x1, y1, x2, y2, color=Color.BLACK):
        """Draws a line on the image.

        Arguments:
            x1 (int): The x coordinate of the starting point of the line.
            y1 (int): The y coordinate of the starting point of the line.
            x2 (int): The x coordinate of the ending point of the line.
            y2 (int): The y coordinate of the ending point of the line.
            color (Color): The color of the line.
        """
        pass

    def draw_box(self, x1, y1, x2, y2, r=0, filled=False, color=Color.BLACK):
        """Draws a box on the image.

        Arguments:
            x1 (int): The x coordinate of the left side of the box.
            y1 (int): The y coordinate of the top of the box.
            x2 (int): The x coordinate of the right side of the box.
            y2 (int): The y coordinate of the bottom of the box.
            r (int): The radius of the corners of the box.
            filled (bool): If ``True``, the box will be filled with ``color``,
                otherwise only the outline of the box will be drawn.
            color (Color): The color of the box.
        """
        pass

    def draw_circle(self, x, y, r=0, filled=False, color=Color.BLACK):
        """Draws a circle on the image.

        Arguments:
            x (int): The x coordinate of the center of the circle.
            y (int): The y coordinate of the center of the circle.
            r (int): The radius of the circle.
            filled (bool): If ``True``, the circle will be filled with
                ``color``, otherwise only the circumference will be drawn.
            color (Color): The color of the circle.
        """
        pass

    def draw_image(self, x, y, image, color=None):
        """Draws a copy of another image on this image.

        Arguments:
            x (int):
                The x-axis value where the left side of the image will start.
            y (int):
                The y-axis value where the top of the image will start.
            image (Image):
                The image to copy.
            color (Color):
                The color of ``image`` to treat as transparent or ``None`` for
                no transparency.
        """

    def draw_text(self, x, y, text, color=Color.BLACK):
        """Draws text on the image.

        The most recent font set using :meth:`set_font` will be used or
        :data:`Font.DEFAULT` if no font has been set yet.

        Arguments:
            x (int):
                The x-axis value where the left side of the text will start.
            y (int):
                The y-axis value where the top of the text will start.
            text (str):
                The text to display.
            color (Color):
                The color used for drawing the text.
        """
        pass

    def print(self, *args, sep=' ', end='\n'):
        """Prints a line of text on the image.

        This method works like the built-in ``print()`` function except that
        it writes the text on the image instead.

        The most recent font set using :meth:`set_font` will be used or
        :data:`Font.DEFAULT` if no font has been set yet.

        Lines are not wrapped if they are too long to fit on the image
        horizontally. On the other hand, If the text would be printed off of
        the image vertically, the entire image is scrolled up so that the text
        will be visible in the image.

        Arguments:
            * (object):
                Zero or more objects to print.
            sep (str):
                Separator that will be placed between each object that is
                printed.
            end (str):
                End of line that will be printed after the last object.
        """
        pass

    def set_font(self, font):
        """Sets the font used for writing on this image.

        The font is used for both :meth:`draw_text` and :meth:`print`.

        Arguments:
            font (:class:`Font`):
                The font to use.
        """
        pass


class Font:
    """Object that represents a font for writing text."""

    DEFAULT = None  # assigned later since we can't use Font() here
    """The default font."""

    def __init__(self, family=None, size=12, bold=False, monospace=False,
                 lang=None, scrip=None):
        """The font object will be a font that is the "best" match based on the
        parameters given and available fonts installed.

        Arguments:
            family (str):
                The preferred font family or ``None`` to use the default value.
            size (int):
                The preferred font size. Most fonts have sizes between 6 and 24.
                This is the "point" size and not the same as :attr:`height`.
            bold (bool):
                When ``True``, prefer bold fonts.
            monospace (bool):
                When ``True`` prefer monospaced fonts. This is useful for
                aligning multiple rows of text.
            lang (str):
                A language code, such as "en-us" or "zh-cn" or ``None`` to use
                the default language.
            script (str):
                A unicode script identifier such as "Runr" or ``None``.
        """

    @property
    def family(self):
        """Gets the family name of the font."""
        return 'Lucida'

    @property
    def style(self):
        """Gets a string describing the font style.

        Can be "Regular" or "Bold".
        """
        return 'Regular'

    @property
    def width(self):
        """Gets the width of the widest character of the font."""
        return 0

    @property
    def height(self):
        """Gets the height of the font."""
        return 0

    def text_width(self, text):
        """Gets the width of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The width in pixels.
        """
        return 0

    def text_height(self, text):
        """Gets the height of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The height in pixels.
        """
        return 0


Font.DEFAULT = Font('Lucida', 12)
