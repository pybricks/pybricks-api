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

Image Files
^^^^^^^^^^^

.. autoclass:: pybricks.media.ev3dev.ImageFile
    :no-members:

    .. toggle-header::
        :header: **Information**

        .. data:: ACCEPT
        .. data:: BACKWARD
        .. data:: DECLINE
        .. data:: FORWARD
        .. data:: LEFT
        .. data:: NO_GO
        .. data:: QUESTION_MARK
        .. data:: RIGHT
        .. data:: STOP_1
        .. data:: STOP_2
        .. data:: THUMBS_DOWN
        .. data:: THUMBS_UP
        .. data:: WARNING

    .. toggle-header::
        :header: **LEGO**

        .. data:: EV3
        .. data:: EV3_ICON

    .. toggle-header::
        :header: **Objects**

        .. data:: TARGET

    .. toggle-header::
        :header: **Eyes**

        .. data:: ANGRY
        .. data:: AWAKE
        .. data:: BOTTOM_LEFT
        .. data:: BOTTOM_RIGHT
        .. data:: CRAZY_1
        .. data:: CRAZY_2
        .. data:: DIZZY
        .. data:: DOWN
        .. data:: EVIL
        .. data:: KNOCKED_OUT
        .. data:: MIDDLE_LEFT
        .. data:: MIDDLE_RIGHT
        .. data:: NEUTRAL
        .. data:: PINCHED_LEFT
        .. data:: PINCHED_MIDDLE
        .. data:: PINCHED_RIGHT
        .. data:: SLEEPING
        .. data:: TIRED_LEFT
        .. data:: TIRED_MIDDLE
        .. data:: TIRED_RIGHT
        .. data:: UP
        .. data:: WINKING

Sound Files
^^^^^^^^^^^

.. autoclass:: pybricks.media.ev3dev.SoundFile
    :no-members:

    .. toggle-header::
        :header: **Expressions**

        .. data:: BOING
        .. data:: BOO
        .. data:: CHEERING
        .. data:: CRUNCHING
        .. data:: CRYING
        .. data:: FANFARE
        .. data:: KUNG_FU
        .. data:: LAUGHING_1
        .. data:: LAUGHING_2
        .. data:: MAGIC_WAND
        .. data:: OUCH
        .. data:: SHOUTING
        .. data:: SMACK
        .. data:: SNEEZING
        .. data:: SNORING
        .. data:: UH_OH

    .. toggle-header::
        :header: **Information**

        .. data:: ACTIVATE
        .. data:: ANALYZE
        .. data:: BACKWARDS
        .. data:: COLOR
        .. data:: DETECTED
        .. data:: DOWN
        .. data:: ERROR
        .. data:: ERROR_ALARM
        .. data:: FLASHING
        .. data:: FORWARD
        .. data:: LEFT
        .. data:: OBJECT
        .. data:: RIGHT
        .. data:: SEARCHING
        .. data:: START
        .. data:: STOP
        .. data:: TOUCH
        .. data:: TURN
        .. data:: UP

    .. toggle-header::
        :header: **Communication**

        .. data:: BRAVO
        .. data:: EV3
        .. data:: FANTASTIC
        .. data:: GAME_OVER
        .. data:: GO
        .. data:: GOOD
        .. data:: GOOD_JOB
        .. data:: GOODBYE
        .. data:: HELLO
        .. data:: HI
        .. data:: LEGO
        .. data:: MINDSTORMS
        .. data:: MORNING
        .. data:: NO
        .. data:: OKAY
        .. data:: OKEY_DOKEY
        .. data:: SORRY
        .. data:: THANK_YOU
        .. data:: YES

    .. toggle-header::
        :header: **Movement sounds**

        .. data:: SPEED_DOWN
        .. data:: SPEED_IDLE
        .. data:: SPEED_UP

    .. toggle-header::
        :header: **Colors**

        .. data:: BLACK
        .. data:: BLUE
        .. data:: BROWN
        .. data:: GREEN
        .. data:: RED
        .. data:: WHITE
        .. data:: YELLOW

    .. toggle-header::
        :header: **Mechanical**

        .. data:: AIR_RELEASE
        .. data:: AIRBRAKE
        .. data:: BACKING_ALERT
        .. data:: HORN_1
        .. data:: HORN_2
        .. data:: LASER
        .. data:: MOTOR_IDLE
        .. data:: MOTOR_START
        .. data:: MOTOR_STOP
        .. data:: RATCHET
        .. data:: SONAR
        .. data:: TICK_TACK

    .. toggle-header::
        :header: **Animal sounds**

        .. data:: CAT_PURR
        .. data:: DOG_BARK_1
        .. data:: DOG_BARK_2
        .. data:: DOG_GROWL
        .. data:: DOG_SNIFF
        .. data:: DOG_WHINE
        .. data:: ELEPHANT_CALL
        .. data:: INSECT_BUZZ_1
        .. data:: INSECT_BUZZ_2
        .. data:: INSECT_CHIRP
        .. data:: SNAKE_HISS
        .. data:: SNAKE_RATTLE
        .. data:: T_REX_ROAR

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

        .. data:: CLICK
        .. data:: CONFIRM
        .. data:: GENERAL_ALERT
        .. data:: OVERPOWER
        .. data:: READY


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


Image Manipulation
^^^^^^^^^^^^^^^^^^

Instead of drawing directly on the EV3 screen, you can make and interact
with image files using the ``Image`` class given below.

.. |this image| replace:: this image

.. autoclass:: pybricks.media.ev3dev.Image
    :no-members:

    .. automethod:: pybricks.media.ev3dev.Image.empty

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

    .. automethod:: pybricks.media.ev3dev.Image.load_image


    .. rubric:: Saving the image

    .. automethod:: pybricks.media.ev3dev.Image.save
