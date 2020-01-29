:mod:`media <pybricks.media>` -- Sounds and Images
==================================================

.. automodule:: pybricks.media
    :no-members:

You can use your own sound and image files by placing them in your project
folder. You can also use any of the images and sounds built into ev3dev, or
draw your own.

ev3dev
------

.. automodule:: pybricks.media.ev3dev
    :no-members:

Images
^^^^^^

.. autoclass:: pybricks.media.ev3dev.ImageFile
    :no-members:

    .. toggle-header::
        :header: **Information**

        .. data:: RIGHT
        .. data:: FORWARD
        .. data:: ACCEPT
        .. data:: QUESTION_MARK
        .. data:: STOP_1
        .. data:: LEFT
        .. data:: DECLINE
        .. data:: THUMBS_DOWN
        .. data:: BACKWARD
        .. data:: NO_GO
        .. data:: WARNING
        .. data:: STOP_2
        .. data:: THUMBS_UP

    .. toggle-header::
        :header: **LEGO**

        .. data:: EV3
        .. data:: EV3_ICON

    .. toggle-header::
        :header: **Objects**

        .. data:: TARGET

    .. toggle-header::
        :header: **Eyes**

        .. data:: BOTTOM_RIGHT
        .. data:: BOTTOM_LEFT
        .. data:: EVIL
        .. data:: CRAZY_2
        .. data:: KNOCKED_OUT
        .. data:: PINCHED_RIGHT
        .. data:: WINKING
        .. data:: DIZZY
        .. data:: DOWN
        .. data:: TIRED_MIDDLE
        .. data:: MIDDLE_RIGHT
        .. data:: SLEEPING
        .. data:: MIDDLE_LEFT
        .. data:: TIRED_RIGHT
        .. data:: PINCHED_LEFT
        .. data:: PINCHED_MIDDLE
        .. data:: CRAZY_1
        .. data:: NEUTRAL
        .. data:: AWAKE
        .. data:: UP
        .. data:: TIRED_LEFT
        .. data:: ANGRY

Sounds
^^^^^^

.. autoclass:: pybricks.media.ev3dev.SoundFile
    :no-members:

    .. toggle-header::
        :header: **Expressions**

        .. data:: SHOUTING
        .. data:: CHEERING
        .. data:: CRYING
        .. data:: OUCH
        .. data:: LAUGHING_2
        .. data:: SNEEZING
        .. data:: SMACK
        .. data:: BOING
        .. data:: BOO
        .. data:: UH_OH
        .. data:: SNORING
        .. data:: KUNG_FU
        .. data:: FANFARE
        .. data:: CRUNCHING
        .. data:: MAGIC_WAND
        .. data:: LAUGHING_1

    .. toggle-header::
        :header: **Information**

        .. data:: LEFT
        .. data:: BACKWARDS
        .. data:: RIGHT
        .. data:: OBJECT
        .. data:: COLOR
        .. data:: FLASHING
        .. data:: ERROR
        .. data:: ERROR_ALARM
        .. data:: DOWN
        .. data:: FORWARD
        .. data:: ACTIVATE
        .. data:: SEARCHING
        .. data:: TOUCH
        .. data:: UP
        .. data:: ANALYZE
        .. data:: STOP
        .. data:: DETECTED
        .. data:: TURN
        .. data:: START

    .. toggle-header::
        :header: **Communication**

        .. data:: MORNING
        .. data:: EV3
        .. data:: GO
        .. data:: GOOD_JOB
        .. data:: OKEY_DOKEY
        .. data:: GOOD
        .. data:: NO
        .. data:: THANK_YOU
        .. data:: YES
        .. data:: GAME_OVER
        .. data:: OKAY
        .. data:: SORRY
        .. data:: BRAVO
        .. data:: GOODBYE
        .. data:: HI
        .. data:: HELLO
        .. data:: MINDSTORMS
        .. data:: LEGO
        .. data:: FANTASTIC

    .. toggle-header::
        :header: **Movement sounds**

        .. data:: SPEED_IDLE
        .. data:: SPEED_DOWN
        .. data:: SPEED_UP

    .. toggle-header::
        :header: **Colors**

        .. data:: BROWN
        .. data:: GREEN
        .. data:: BLACK
        .. data:: WHITE
        .. data:: RED
        .. data:: BLUE
        .. data:: YELLOW

    .. toggle-header::
        :header: **Mechanical**

        .. data:: TICK_TACK
        .. data:: HORN_1
        .. data:: BACKING_ALERT
        .. data:: MOTOR_IDLE
        .. data:: AIR_RELEASE
        .. data:: AIRBRAKE
        .. data:: RATCHET
        .. data:: MOTOR_STOP
        .. data:: HORN_2
        .. data:: LASER
        .. data:: SONAR
        .. data:: MOTOR_START

    .. toggle-header::
        :header: **Animal sounds**

        .. data:: INSECT_BUZZ_2
        .. data:: ELEPHANT_CALL
        .. data:: SNAKE_HISS
        .. data:: DOG_BARK_2
        .. data:: DOG_WHINE
        .. data:: INSECT_BUZZ_1
        .. data:: DOG_SNIFF
        .. data:: T_REX_ROAR
        .. data:: INSECT_CHIRP
        .. data:: DOG_GROWL
        .. data:: SNAKE_RATTLE
        .. data:: DOG_BARK_1
        .. data:: CAT_PURR

    .. toggle-header::
        :header: **Numbers**

        .. data:: ZERO
        .. data:: ONE
        .. data:: TWO
        .. data:: THREE
        .. data:: FOUR
        .. data:: FIVE
        .. data:: SIX
        .. data:: SEVEN
        .. data:: EIGHT
        .. data:: NINE
        .. data:: TEN

    .. toggle-header::
        :header: **System sounds**

        .. data:: READY
        .. data:: CONFIRM
        .. data:: GENERAL_ALERT
        .. data:: CLICK
        .. data:: OVERPOWER


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

Making Your Own Images
^^^^^^^^^^^^^^^^^^^^^^
Instead of drawing directly on the EV3 screen, you can make and interact
with image files using the ``Image`` class given below.

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




