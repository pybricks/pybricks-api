# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Images and Sounds for Pybricks on ev3dev."""

from __future__ import annotations

from typing import Union, Literal, overload, Optional, Any

from ..parameters import Color


class Image:
    """Object representing a graphics image. This can either be an in-memory
    copy of an image or the image displayed on a screen."""

    # Documentation note: This class is also treated as the `screen` object
    # on EV3 so we use |this image| when it would make sense to say "the screen"
    # in that context and it is automatically replaced when the documentation
    # is generated.

    @overload
    def __init__(self, /, source: Union[Image, ImageFile, str]):
        ...

    @overload
    def __init__(
        self, /, source: Image, sub: Literal[False], x1: int, y1: int, x2: int, y2: int
    ):
        ...

    def __init__(self, *args):
        """Image(source, sub=False)


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

                Additional keyword arguments ``x1``, ``y1``, ``x2``, ``y2`` are
                needed when ``sub=True``. These specify the top-left and
                bottom-right coordinates in the ``source`` image that will be
                used as the bounds for the sub-image.
        """

    @property
    def width(self) -> int:
        """Gets the width of |this image| in pixels."""
        return 0

    @property
    def height(self) -> int:
        """Gets the height of |this image| in pixels."""
        return 0

    def clear(self) -> None:
        """clear()

        Clears |this image|. All pixels on |this image| will be set to
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.
        """

    def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        """draw_pixel(x, y, color=Color.BLACK)

        Draws a single pixel on |this image|.

        Arguments:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            color (Color): The color of the pixel.
        """

    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        width: int = 1,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_line(x1, y1, x2, y2, width=1, color=Color.BLACK)

        Draws a line on |this image|.

        Arguments:
            x1 (int): The x coordinate of the starting point of the line.
            y1 (int): The y coordinate of the starting point of the line.
            x2 (int): The x coordinate of the ending point of the line.
            y2 (int): The y coordinate of the ending point of the line.
            width (int): The width of the line in pixels.
            color (Color): The color of the line.
        """

    def draw_box(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        r: int = 0,
        fill: bool = False,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_box(x1, y1, x2, y2, r=0, fill=False, color=Color.BLACK)

        Draws a box on |this image|.

        Arguments:
            x1 (int): The x coordinate of the left side of the box.
            y1 (int): The y coordinate of the top of the box.
            x2 (int): The x coordinate of the right side of the box.
            y2 (int): The y coordinate of the bottom of the box.
            r (int): The radius of the corners of the box.
            fill (bool): If ``True``, the box will be filled with ``color``,
                otherwise only the outline of the box will be drawn.
            color (Color): The color of the box.
        """

    def draw_circle(
        self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK
    ) -> None:
        """draw_circle(x, y, r, fill=False, color=Color.BLACK)

        Draws a circle on |this image|.

        Arguments:
            x (int): The x coordinate of the center of the circle.
            y (int): The y coordinate of the center of the circle.
            r (int): The radius of the circle.
            fill (bool): If ``True``, the circle will be filled with
                ``color``, otherwise only the circumference will be drawn.
            color (Color): The color of the circle.
        """

    def draw_image(
        self,
        x: int,
        y: int,
        source: Union[Image, ImageFile, str],
        transparent: Optional[Color] = None,
    ) -> None:
        """draw_image(x, y, source, transparent=None)

        Draws the ``source`` image on |this image|.

        Arguments:
            x (int):
                The x-axis value where the left side of the image will start.
            y (int):
                The y-axis value where the top of the image will start.
            source (Image or str):
                The source :class:`Image <pybricks.media.ev3dev.Image>`. If
                the argument is a string, then the ``source`` image is loaded
                from file.
            transparent (Color):
                The color of ``image`` to treat as transparent or ``None`` for
                no transparency.
        """

    def load_image(self, source: Union[Image, ImageFile, str]) -> None:
        """load_image(source)

        Clears this image, then draws the ``source`` image centered in
        |this image|.

        Arguments:
            source (Image or str):
                The source :class:`Image <pybricks.media.ev3dev.Image>`. If
                the argument is a string, then the ``source`` image is loaded
                from file.
        """

    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        text_color: Color = Color.BLACK,
        background_color: Optional[Color] = None,
    ) -> None:
        """draw_text(x, y, text, text_color=Color.BLACK, background_color=None)

        Draws text on |this image|.

        The most recent font set using :meth:`.set_font` will be used or
        :data:`Font.DEFAULT <pybricks.media.ev3dev.Font.DEFAULT>` if no font
        has been set yet.

        Arguments:
            x (int):
                The x-axis value where the left side of the text will start.
            y (int):
                The y-axis value where the top of the text will start.
            text (str):
                The text to draw.
            text_color (Color):
                The color used for drawing the text.
            background_color (Color):
                The color used to fill the rectangle behind the text or
                ``None`` for transparent background.
        """

    def print(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        """print(*args, sep=" ", end="\\n")

        Prints a line of text on |this image|.

        This method works like the builtin ``print()`` function, but it writes
        on |this image| instead.

        You can set the font using :meth:`.set_font`. If no font has been set,
        :data:`Font.DEFAULT <pybricks.media.ev3dev.Font.DEFAULT>` will be
        used. The text is always printed used black text with a white
        background.

        Unlike the builtin ``print()``, the text does not wrap if it is too
        wide to fit on |this image|. It just gets cut off. But if the text
        would go off of the bottom of |this image|, the entire image is
        scrolled up and the text is printed in the new blank area at the
        bottom of |this image|.

        Arguments:
            args (Any): Zero or more objects to print.
            sep (str): Separator that will be placed between each object that
                is printed.
            end (str): End of line that will be printed after the last object.
        """

    def set_font(self, font: Font) -> None:
        """set_font(font)

        Sets the font used for writing on |this image|.

        The font is used for both :meth:`.draw_text` and :meth:`.print`.

        Arguments:
            font (Font):
                The font to use.
        """

    @staticmethod
    def empty(width: int = 178, height: int = 128) -> Image:
        """empty(width=178, height=128) -> Image

        Creates a new empty :class:`Image` object.

        Arguments:
            width (int):
                The width of the image in pixels.
            height (int):
                The height of the image in pixels.

        Returns:
            A new image with all pixels set
            to :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.

        Raises:
            TypeError:
                If ``width`` or ``height`` is not a number.
            ValueError:
                If ``width`` or ``height`` is less than 1.
            RuntimeError:
                If there was a problem allocating a new image.
        """

    def save(self, filename: str) -> None:
        """save(filename)

        Saves |this image| as a ``.png`` file.

        Arguments:
            filename (str):
                The path to the file to be saved.

        Raises:
            TypeError:
                ``filename`` is not a string.
            OSError:
                There was a problem saving the file.
        """


class Font:
    """Object that represents a font for writing text."""

    DEFAULT: Font = None  # assigned later since we can't use Font() here
    """The default font."""

    def __init__(
        self,
        family: Optional[str] = None,
        size: int = 12,
        bold: bool = False,
        monospace: bool = False,
        lang: Optional[str] = None,
        script: Optional[str] = None,
    ):
        """Font(family=None, size=12, bold=False, monospace=False, lang=None, script=None)

        The font object will be a font that is the "best" match based on the
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
                A language code, such as ``'en'`` or ``'zh-cn'`` or ``None`` to
                use the default language. [#font_lang]_
            script (str):
                A unicode script identifier such as ``'Runr'`` or ``None``.
        """

    @property
    def family(self) -> str:
        """Gets the family name of the font."""
        return "Lucida"

    @property
    def style(self) -> str:
        """style -> str

        Gets a string describing the font style.

        Can be "Regular" or "Bold".
        """
        return "Regular"

    @property
    def width(self) -> int:
        """Gets the width of the widest character of the font."""
        return 0

    @property
    def height(self) -> int:
        """Gets the height of the font."""
        return 0

    def text_width(self, text: str) -> int:
        """text_width(text)

        Gets the width of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The width in pixels.
        """
        return 0

    def text_height(self, text: str) -> int:
        """text_height(text)

        Gets the height of the text when the text is drawn using this font.

        Arguments:
            text (str):
                The text.

        Returns:
            int:
                The height in pixels.
        """
        return 0


Font.DEFAULT = Font("Lucida", 12)


class SoundFile:
    """Paths to standard EV3 sounds."""

    _BASE_PATH: str = "/usr/share/sounds/ev3dev/"
    SHOUTING: str = _BASE_PATH + "expressions/shouting.wav"
    CHEERING: str = _BASE_PATH + "expressions/cheering.wav"
    CRYING: str = _BASE_PATH + "expressions/crying.wav"
    OUCH: str = _BASE_PATH + "expressions/ouch.wav"
    LAUGHING_2: str = _BASE_PATH + "expressions/laughing_2.wav"
    SNEEZING: str = _BASE_PATH + "expressions/sneezing.wav"
    SMACK: str = _BASE_PATH + "expressions/smack.wav"
    BOING: str = _BASE_PATH + "expressions/boing.wav"
    BOO: str = _BASE_PATH + "expressions/boo.wav"
    UH_OH: str = _BASE_PATH + "expressions/uh-oh.wav"
    SNORING: str = _BASE_PATH + "expressions/snoring.wav"
    KUNG_FU: str = _BASE_PATH + "expressions/kung_fu.wav"
    FANFARE: str = _BASE_PATH + "expressions/fanfare.wav"
    CRUNCHING: str = _BASE_PATH + "expressions/crunching.wav"
    MAGIC_WAND: str = _BASE_PATH + "expressions/magic_wand.wav"
    LAUGHING_1: str = _BASE_PATH + "expressions/laughing_1.wav"
    LEFT: str = _BASE_PATH + "information/left.wav"
    BACKWARDS: str = _BASE_PATH + "information/backwards.wav"
    RIGHT: str = _BASE_PATH + "information/right.wav"
    OBJECT: str = _BASE_PATH + "information/object.wav"
    COLOR: str = _BASE_PATH + "information/color.wav"
    FLASHING: str = _BASE_PATH + "information/flashing.wav"
    ERROR: str = _BASE_PATH + "information/error.wav"
    ERROR_ALARM: str = _BASE_PATH + "information/error_alarm.wav"
    DOWN: str = _BASE_PATH + "information/down.wav"
    FORWARD: str = _BASE_PATH + "information/forward.wav"
    ACTIVATE: str = _BASE_PATH + "information/activate.wav"
    SEARCHING: str = _BASE_PATH + "information/searching.wav"
    TOUCH: str = _BASE_PATH + "information/touch.wav"
    UP: str = _BASE_PATH + "information/up.wav"
    ANALYZE: str = _BASE_PATH + "information/analyze.wav"
    STOP: str = _BASE_PATH + "information/stop.wav"
    DETECTED: str = _BASE_PATH + "information/detected.wav"
    TURN: str = _BASE_PATH + "information/turn.wav"
    START: str = _BASE_PATH + "information/start.wav"
    MORNING: str = _BASE_PATH + "communication/morning.wav"
    EV3: str = _BASE_PATH + "communication/ev3.wav"
    GO: str = _BASE_PATH + "communication/go.wav"
    GOOD_JOB: str = _BASE_PATH + "communication/good_job.wav"
    OKEY_DOKEY: str = _BASE_PATH + "communication/okey-dokey.wav"
    GOOD: str = _BASE_PATH + "communication/good.wav"
    NO: str = _BASE_PATH + "communication/no.wav"
    THANK_YOU: str = _BASE_PATH + "communication/thank_you.wav"
    YES: str = _BASE_PATH + "communication/yes.wav"
    GAME_OVER: str = _BASE_PATH + "communication/game_over.wav"
    OKAY: str = _BASE_PATH + "communication/okay.wav"
    SORRY: str = _BASE_PATH + "communication/sorry.wav"
    BRAVO: str = _BASE_PATH + "communication/bravo.wav"
    GOODBYE: str = _BASE_PATH + "communication/goodbye.wav"
    HI: str = _BASE_PATH + "communication/hi.wav"
    HELLO: str = _BASE_PATH + "communication/hello.wav"
    MINDSTORMS: str = _BASE_PATH + "communication/mindstorms.wav"
    LEGO: str = _BASE_PATH + "communication/lego.wav"
    FANTASTIC: str = _BASE_PATH + "communication/fantastic.wav"
    SPEED_IDLE: str = _BASE_PATH + "movements/speed_idle.wav"
    SPEED_DOWN: str = _BASE_PATH + "movements/speed_down.wav"
    SPEED_UP: str = _BASE_PATH + "movements/speed_up.wav"
    BROWN: str = _BASE_PATH + "colors/brown.wav"
    GREEN: str = _BASE_PATH + "colors/green.wav"
    BLACK: str = _BASE_PATH + "colors/black.wav"
    WHITE: str = _BASE_PATH + "colors/white.wav"
    RED: str = _BASE_PATH + "colors/red.wav"
    BLUE: str = _BASE_PATH + "colors/blue.wav"
    YELLOW: str = _BASE_PATH + "colors/yellow.wav"
    TICK_TACK: str = _BASE_PATH + "mechanical/tick_tack.wav"
    HORN_1: str = _BASE_PATH + "mechanical/horn_1.wav"
    BACKING_ALERT: str = _BASE_PATH + "mechanical/backing_alert.wav"
    MOTOR_IDLE: str = _BASE_PATH + "mechanical/motor_idle.wav"
    AIR_RELEASE: str = _BASE_PATH + "mechanical/air_release.wav"
    AIRBRAKE: str = _BASE_PATH + "mechanical/airbrake.wav"
    RATCHET: str = _BASE_PATH + "mechanical/ratchet.wav"
    MOTOR_STOP: str = _BASE_PATH + "mechanical/motor_stop.wav"
    HORN_2: str = _BASE_PATH + "mechanical/horn_2.wav"
    LASER: str = _BASE_PATH + "mechanical/laser.wav"
    SONAR: str = _BASE_PATH + "mechanical/sonar.wav"
    MOTOR_START: str = _BASE_PATH + "mechanical/motor_start.wav"
    INSECT_BUZZ_2: str = _BASE_PATH + "animals/insect_buzz_2.wav"
    ELEPHANT_CALL: str = _BASE_PATH + "animals/elephant_call.wav"
    SNAKE_HISS: str = _BASE_PATH + "animals/snake_hiss.wav"
    DOG_BARK_2: str = _BASE_PATH + "animals/dog_bark_2.wav"
    DOG_WHINE: str = _BASE_PATH + "animals/dog_whine.wav"
    INSECT_BUZZ_1: str = _BASE_PATH + "animals/insect_buzz_1.wav"
    DOG_SNIFF: str = _BASE_PATH + "animals/dog_sniff.wav"
    T_REX_ROAR: str = _BASE_PATH + "animals/t-rex_roar.wav"
    INSECT_CHIRP: str = _BASE_PATH + "animals/insect_chirp.wav"
    DOG_GROWL: str = _BASE_PATH + "animals/dog_growl.wav"
    SNAKE_RATTLE: str = _BASE_PATH + "animals/snake_rattle.wav"
    DOG_BARK_1: str = _BASE_PATH + "animals/dog_bark_1.wav"
    CAT_PURR: str = _BASE_PATH + "animals/cat_purr.wav"
    EIGHT: str = _BASE_PATH + "numbers/eight.wav"
    SEVEN: str = _BASE_PATH + "numbers/seven.wav"
    SIX: str = _BASE_PATH + "numbers/six.wav"
    FOUR: str = _BASE_PATH + "numbers/four.wav"
    TEN: str = _BASE_PATH + "numbers/ten.wav"
    ONE: str = _BASE_PATH + "numbers/one.wav"
    TWO: str = _BASE_PATH + "numbers/two.wav"
    THREE: str = _BASE_PATH + "numbers/three.wav"
    ZERO: str = _BASE_PATH + "numbers/zero.wav"
    FIVE: str = _BASE_PATH + "numbers/five.wav"
    NINE: str = _BASE_PATH + "numbers/nine.wav"
    READY: str = _BASE_PATH + "system/ready.wav"
    CONFIRM: str = _BASE_PATH + "system/confirm.wav"
    GENERAL_ALERT: str = _BASE_PATH + "system/general_alert.wav"
    CLICK: str = _BASE_PATH + "system/click.wav"
    OVERPOWER: str = _BASE_PATH + "system/overpower.wav"


class ImageFile:
    """Paths to standard EV3 images."""

    _BASE_PATH: str = "/usr/share/images/ev3dev/mono/"
    RIGHT: str = _BASE_PATH + "information/right.png"
    FORWARD: str = _BASE_PATH + "information/forward.png"
    ACCEPT: str = _BASE_PATH + "information/accept.png"
    QUESTION_MARK: str = _BASE_PATH + "information/question_mark.png"
    STOP_1: str = _BASE_PATH + "information/stop_1.png"
    LEFT: str = _BASE_PATH + "information/left.png"
    DECLINE: str = _BASE_PATH + "information/decline.png"
    THUMBS_DOWN: str = _BASE_PATH + "information/thumbs_down.png"
    BACKWARD: str = _BASE_PATH + "information/backward.png"
    NO_GO: str = _BASE_PATH + "information/no_go.png"
    WARNING: str = _BASE_PATH + "information/warning.png"
    STOP_2: str = _BASE_PATH + "information/stop_2.png"
    THUMBS_UP: str = _BASE_PATH + "information/thumbs_up.png"
    EV3: str = _BASE_PATH + "lego/ev3.png"
    EV3_ICON: str = _BASE_PATH + "lego/ev3_icon.png"
    TARGET: str = _BASE_PATH + "objects/target.png"
    BOTTOM_RIGHT: str = _BASE_PATH + "eyes/bottom_right.png"
    BOTTOM_LEFT: str = _BASE_PATH + "eyes/bottom_left.png"
    EVIL: str = _BASE_PATH + "eyes/evil.png"
    CRAZY_2: str = _BASE_PATH + "eyes/crazy_2.png"
    KNOCKED_OUT: str = _BASE_PATH + "eyes/knocked_out.png"
    PINCHED_RIGHT: str = _BASE_PATH + "eyes/pinched_right.png"
    WINKING: str = _BASE_PATH + "eyes/winking.png"
    DIZZY: str = _BASE_PATH + "eyes/dizzy.png"
    DOWN: str = _BASE_PATH + "eyes/down.png"
    TIRED_MIDDLE: str = _BASE_PATH + "eyes/tired_middle.png"
    MIDDLE_RIGHT: str = _BASE_PATH + "eyes/middle_right.png"
    SLEEPING: str = _BASE_PATH + "eyes/sleeping.png"
    MIDDLE_LEFT: str = _BASE_PATH + "eyes/middle_left.png"
    TIRED_RIGHT: str = _BASE_PATH + "eyes/tired_right.png"
    PINCHED_LEFT: str = _BASE_PATH + "eyes/pinched_left.png"
    PINCHED_MIDDLE: str = _BASE_PATH + "eyes/pinched_middle.png"
    CRAZY_1: str = _BASE_PATH + "eyes/crazy_1.png"
    NEUTRAL: str = _BASE_PATH + "eyes/neutral.png"
    AWAKE: str = _BASE_PATH + "eyes/awake.png"
    UP: str = _BASE_PATH + "eyes/up.png"
    TIRED_LEFT: str = _BASE_PATH + "eyes/tired_left.png"
    ANGRY: str = _BASE_PATH + "eyes/angry.png"
