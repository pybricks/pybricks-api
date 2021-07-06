# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from typing import Any, Literal, Optional, Union, overload

from ..parameters import Color

class Image:
    @overload
    def __init__(self, /, source: Union[Image, ImageFile, str]): ...
    @overload
    def __init__(
        self, /, source: Image, sub: Literal[True], x1: int, y1: int, x2: int, y2: int
    ): ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    def clear(self) -> None: ...
    def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK) -> None: ...
    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        width: int = 1,
        color: Color = Color.BLACK,
    ) -> None: ...
    def draw_box(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        r: int = 0,
        fill: bool = False,
        color: Color = Color.BLACK,
    ) -> None: ...
    def draw_circle(
        self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK
    ) -> None: ...
    def draw_image(
        self,
        x: int,
        y: int,
        source: Union[Image, ImageFile, str],
        transparent: Optional[Color] = None,
    ) -> None: ...
    def load_image(self, source: Union[Image, ImageFile, str]) -> None: ...
    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        text_color: Color = Color.BLACK,
        background_color: Optional[Color] = None,
    ) -> None: ...
    def print(self, *args: Any, sep: str = " ", end: str = "\n") -> None: ...
    def set_font(self, font: Font) -> None: ...
    @staticmethod
    def empty(width: int = 178, height: int = 128) -> Image: ...
    def save(self, filename: str) -> None: ...

class Font:
    DEFAULT: Font
    def __init__(
        self,
        family: Optional[str] = None,
        size: int = 12,
        bold: bool = False,
        monospace: bool = False,
        lang: Optional[str] = None,
        script: Optional[str] = None,
    ): ...
    @property
    def family(self) -> str: ...
    @property
    def style(self) -> str: ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    def text_width(self, text: str) -> int: ...
    def text_height(self, text: str) -> int: ...

class SoundFile:
    SHOUTING: SoundFile
    CHEERING: SoundFile
    CRYING: SoundFile
    OUCH: SoundFile
    LAUGHING_2: SoundFile
    SNEEZING: SoundFile
    SMACK: SoundFile
    BOING: SoundFile
    BOO: SoundFile
    UH_OH: SoundFile
    SNORING: SoundFile
    KUNG_FU: SoundFile
    FANFARE: SoundFile
    CRUNCHING: SoundFile
    MAGIC_WAND: SoundFile
    LAUGHING_1: SoundFile
    LEFT: SoundFile
    BACKWARDS: SoundFile
    RIGHT: SoundFile
    OBJECT: SoundFile
    COLOR: SoundFile
    FLASHING: SoundFile
    ERROR: SoundFile
    ERROR_ALARM: SoundFile
    DOWN: SoundFile
    FORWARD: SoundFile
    ACTIVATE: SoundFile
    SEARCHING: SoundFile
    TOUCH: SoundFile
    UP: SoundFile
    ANALYZE: SoundFile
    STOP: SoundFile
    DETECTED: SoundFile
    TURN: SoundFile
    START: SoundFile
    MORNING: SoundFile
    EV3: SoundFile
    GO: SoundFile
    GOOD_JOB: SoundFile
    OKEY_DOKEY: SoundFile
    GOOD: SoundFile
    NO: SoundFile
    THANK_YOU: SoundFile
    YES: SoundFile
    GAME_OVER: SoundFile
    OKAY: SoundFile
    SORRY: SoundFile
    BRAVO: SoundFile
    GOODBYE: SoundFile
    HI: SoundFile
    HELLO: SoundFile
    MINDSTORMS: SoundFile
    LEGO: SoundFile
    FANTASTIC: SoundFile
    SPEED_IDLE: SoundFile
    SPEED_DOWN: SoundFile
    SPEED_UP: SoundFile
    BROWN: SoundFile
    GREEN: SoundFile
    BLACK: SoundFile
    WHITE: SoundFile
    RED: SoundFile
    BLUE: SoundFile
    YELLOW: SoundFile
    TICK_TACK: SoundFile
    HORN_1: SoundFile
    BACKING_ALERT: SoundFile
    MOTOR_IDLE: SoundFile
    AIR_RELEASE: SoundFile
    AIRBRAKE: SoundFile
    RATCHET: SoundFile
    MOTOR_STOP: SoundFile
    HORN_2: SoundFile
    LASER: SoundFile
    SONAR: SoundFile
    MOTOR_START: SoundFile
    INSECT_BUZZ_2: SoundFile
    ELEPHANT_CALL: SoundFile
    SNAKE_HISS: SoundFile
    DOG_BARK_2: SoundFile
    DOG_WHINE: SoundFile
    INSECT_BUZZ_1: SoundFile
    DOG_SNIFF: SoundFile
    T_REX_ROAR: SoundFile
    INSECT_CHIRP: SoundFile
    DOG_GROWL: SoundFile
    SNAKE_RATTLE: SoundFile
    DOG_BARK_1: SoundFile
    CAT_PURR: SoundFile
    EIGHT: SoundFile
    SEVEN: SoundFile
    SIX: SoundFile
    FOUR: SoundFile
    TEN: SoundFile
    ONE: SoundFile
    TWO: SoundFile
    THREE: SoundFile
    ZERO: SoundFile
    FIVE: SoundFile
    NINE: SoundFile
    READY: SoundFile
    CONFIRM: SoundFile
    GENERAL_ALERT: SoundFile
    CLICK: SoundFile
    OVERPOWER: SoundFile

class ImageFile:
    RIGHT: ImageFile
    FORWARD: ImageFile
    ACCEPT: ImageFile
    QUESTION_MARK: ImageFile
    STOP_1: ImageFile
    LEFT: ImageFile
    DECLINE: ImageFile
    THUMBS_DOWN: ImageFile
    BACKWARD: ImageFile
    NO_GO: ImageFile
    WARNING: ImageFile
    STOP_2: ImageFile
    THUMBS_UP: ImageFile
    EV3: ImageFile
    EV3_ICON: ImageFile
    TARGET: ImageFile
    BOTTOM_RIGHT: ImageFile
    BOTTOM_LEFT: ImageFile
    EVIL: ImageFile
    CRAZY_2: ImageFile
    KNOCKED_OUT: ImageFile
    PINCHED_RIGHT: ImageFile
    WINKING: ImageFile
    DIZZY: ImageFile
    DOWN: ImageFile
    TIRED_MIDDLE: ImageFile
    MIDDLE_RIGHT: ImageFile
    SLEEPING: ImageFile
    MIDDLE_LEFT: ImageFile
    TIRED_RIGHT: ImageFile
    PINCHED_LEFT: ImageFile
    PINCHED_MIDDLE: ImageFile
    CRAZY_1: ImageFile
    NEUTRAL: ImageFile
    AWAKE: ImageFile
    UP: ImageFile
    TIRED_LEFT: ImageFile
    ANGRY: ImageFile
