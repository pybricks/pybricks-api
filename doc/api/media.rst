:mod:`media <pybricks.media>` -- Sounds and Images
==================================================

.. module:: pybricks.media

This module describes media such as sound and images that you can use in your
projects. Media are divided into submodules that indicate on which platform
they are available.

:mod:`media.ev3dev <pybricks.media.ev3dev>` -- Sounds and Images
---------------------------------------------------------------------

.. module:: pybricks.media.ev3dev

EV3 MicroPython is built on top of ev3dev, which comes with a variety of image
and sound files. You can access them using the classes below.

You can also use your own sound and image files by placing them in your project
folder.

Image Files
^^^^^^^^^^^

.. autoclass:: pybricks.media.ev3dev.ImageFile
    :no-members:

    .. toggle-header::
        :header: **Information**

        .. data:: ACCEPT

            .. image:: ../../media/ev3dev-media/images/mono/information/accept.png
                :width: 15 %

        .. data:: BACKWARD

            .. image:: ../../media/ev3dev-media/images/mono/information/backward.png
                :width: 15 %

        .. data:: DECLINE

            .. image:: ../../media/ev3dev-media/images/mono/information/decline.png
                :width: 15 %

        .. data:: FORWARD

            .. image:: ../../media/ev3dev-media/images/mono/information/forward.png
                :width: 15 %

        .. data:: LEFT

            .. image:: ../../media/ev3dev-media/images/mono/information/left.png
                :width: 15 %

        .. data:: NO_GO

            .. image:: ../../media/ev3dev-media/images/mono/information/no_go.png
                :width: 15 %

        .. data:: QUESTION_MARK

            .. image:: ../../media/ev3dev-media/images/mono/information/question_mark.png
                :width: 15 %

        .. data:: RIGHT

            .. image:: ../../media/ev3dev-media/images/mono/information/right.png
                :width: 15 %

        .. data:: STOP_1

            .. image:: ../../media/ev3dev-media/images/mono/information/stop_1.png
                :width: 15 %

        .. data:: STOP_2

            .. image:: ../../media/ev3dev-media/images/mono/information/stop_2.png
                :width: 15 %

        .. data:: THUMBS_DOWN

            .. image:: ../../media/ev3dev-media/images/mono/information/thumbs_down.png
                :width: 15 %

        .. data:: THUMBS_UP

            .. image:: ../../media/ev3dev-media/images/mono/information/thumbs_up.png
                :width: 15 %

        .. data:: WARNING

            .. image:: ../../media/ev3dev-media/images/mono/information/warning.png
                :width: 15 %

    .. toggle-header::
        :header: **LEGO**

        .. data:: EV3

            .. image:: ../../media/ev3dev-media/images/mono/lego/ev3.png
                :width: 15 %

        .. data:: EV3_ICON

            .. image:: ../../media/ev3dev-media/images/mono/lego/ev3_icon.png
                :width: 15 %

    .. toggle-header::
        :header: **Objects**

        .. data:: TARGET

            .. image:: ../../media/ev3dev-media/images/mono/objects/target.png
                :width: 15 %

    .. toggle-header::
        :header: **Eyes**

        .. data:: ANGRY

            .. image:: ../../media/ev3dev-media/images/mono/eyes/angry.png
                :width: 15 %

        .. data:: AWAKE

            .. image:: ../../media/ev3dev-media/images/mono/eyes/awake.png
                :width: 15 %

        .. data:: BOTTOM_LEFT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/bottom_left.png
                :width: 15 %


        .. data:: BOTTOM_RIGHT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/bottom_right.png
                :width: 15 %

        .. data:: CRAZY_1

            .. image:: ../../media/ev3dev-media/images/mono/eyes/crazy_1.png
                :width: 15 %

        .. data:: CRAZY_2

            .. image:: ../../media/ev3dev-media/images/mono/eyes/crazy_2.png
                :width: 15 %

        .. data:: DIZZY

            .. image:: ../../media/ev3dev-media/images/mono/eyes/dizzy.png
                :width: 15 %

        .. data:: DOWN

            .. image:: ../../media/ev3dev-media/images/mono/eyes/down.png
                :width: 15 %

        .. data:: EVIL

            .. image:: ../../media/ev3dev-media/images/mono/eyes/evil.png
                :width: 15 %

        .. data:: KNOCKED_OUT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/knocked_out.png
                :width: 15 %

        .. data:: MIDDLE_LEFT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/middle_left.png
                :width: 15 %

        .. data:: MIDDLE_RIGHT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/middle_right.png
                :width: 15 %

        .. data:: NEUTRAL

            .. image:: ../../media/ev3dev-media/images/mono/eyes/neutral.png
                :width: 15 %

        .. data:: PINCHED_LEFT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/pinched_left.png
                :width: 15 %

        .. data:: PINCHED_MIDDLE

            .. image:: ../../media/ev3dev-media/images/mono/eyes/pinched_middle.png
                :width: 15 %

        .. data:: PINCHED_RIGHT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/pinched_right.png
                :width: 15 %

        .. data:: SLEEPING

            .. image:: ../../media/ev3dev-media/images/mono/eyes/sleeping.png
                :width: 15 %

        .. data:: TIRED_LEFT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/tired_left.png
                :width: 15 %

        .. data:: TIRED_MIDDLE

            .. image:: ../../media/ev3dev-media/images/mono/eyes/tired_middle.png
                :width: 15 %

        .. data:: TIRED_RIGHT

            .. image:: ../../media/ev3dev-media/images/mono/eyes/tired_right.png
                :width: 15 %

        .. data:: UP

            .. image:: ../../media/ev3dev-media/images/mono/eyes/up.png
                :width: 15 %

        .. data:: WINKING

            .. image:: ../../media/ev3dev-media/images/mono/eyes/winking.png
                :width: 15 %

Sound Files
^^^^^^^^^^^

.. autoclass:: pybricks.media.ev3dev.SoundFile
    :no-members:

    .. toggle-header::
        :header: **Expressions**

        .. data:: BOING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/boing.wav>`

        .. data:: BOO

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/boo.wav>`

        .. data:: CHEERING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/cheering.wav>`

        .. data:: CRUNCHING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/crunching.wav>`

        .. data:: CRYING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/crying.wav>`

        .. data:: FANFARE

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/fanfare.wav>`

        .. data:: KUNG_FU

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/kung_fu.wav>`

        .. data:: LAUGHING_1

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/laughing_1.wav>`

        .. data:: LAUGHING_2

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/laughing_2.wav>`

        .. data:: MAGIC_WAND

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/magic_wand.wav>`

        .. data:: OUCH

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/ouch.wav>`

        .. data:: SHOUTING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/shouting.wav>`

        .. data:: SMACK

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/smack.wav>`

        .. data:: SNEEZING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/sneezing.wav>`

        .. data:: SNORING

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/snoring.wav>`

        .. data:: UH_OH

            :download:`Preview <../../media/ev3dev-media/sounds/expressions/uh-oh.wav>`


    .. toggle-header::
        :header: **Information**

        .. data:: ACTIVATE

            :download:`Preview <../../media/ev3dev-media/sounds/information/activate.wav>`

        .. data:: ANALYZE

            :download:`Preview <../../media/ev3dev-media/sounds/information/analyze.wav>`

        .. data:: BACKWARDS

            :download:`Preview <../../media/ev3dev-media/sounds/information/backwards.wav>`

        .. data:: COLOR

            :download:`Preview <../../media/ev3dev-media/sounds/information/color.wav>`

        .. data:: DETECTED

            :download:`Preview <../../media/ev3dev-media/sounds/information/detected.wav>`

        .. data:: DOWN

            :download:`Preview <../../media/ev3dev-media/sounds/information/down.wav>`

        .. data:: ERROR

            :download:`Preview <../../media/ev3dev-media/sounds/information/error.wav>`

        .. data:: ERROR_ALARM

            :download:`Preview <../../media/ev3dev-media/sounds/information/error_alarm.wav>`


        .. data:: FLASHING

            :download:`Preview <../../media/ev3dev-media/sounds/information/flashing.wav>`

        .. data:: FORWARD

            :download:`Preview <../../media/ev3dev-media/sounds/information/forward.wav>`

        .. data:: LEFT

            :download:`Preview <../../media/ev3dev-media/sounds/information/left.wav>`

        .. data:: OBJECT

            :download:`Preview <../../media/ev3dev-media/sounds/information/object.wav>`

        .. data:: RIGHT

            :download:`Preview <../../media/ev3dev-media/sounds/information/right.wav>`

        .. data:: SEARCHING

            :download:`Preview <../../media/ev3dev-media/sounds/information/searching.wav>`

        .. data:: START

            :download:`Preview <../../media/ev3dev-media/sounds/information/start.wav>`

        .. data:: STOP

            :download:`Preview <../../media/ev3dev-media/sounds/information/stop.wav>`

        .. data:: TOUCH

            :download:`Preview <../../media/ev3dev-media/sounds/information/touch.wav>`

        .. data:: TURN

            :download:`Preview <../../media/ev3dev-media/sounds/information/turn.wav>`

        .. data:: UP

            :download:`Preview <../../media/ev3dev-media/sounds/information/up.wav>`

    .. toggle-header::
        :header: **Communication**

        .. data:: BRAVO

            :download:`Preview <../../media/ev3dev-media/sounds/communication/bravo.wav>`

        .. data:: EV3

            :download:`Preview <../../media/ev3dev-media/sounds/communication/ev3.wav>`

        .. data:: FANTASTIC

            :download:`Preview <../../media/ev3dev-media/sounds/communication/fantastic.wav>`

        .. data:: GAME_OVER

            :download:`Preview <../../media/ev3dev-media/sounds/communication/game_over.wav>`

        .. data:: GO

            :download:`Preview <../../media/ev3dev-media/sounds/communication/go.wav>`

        .. data:: GOOD_JOB

            :download:`Preview <../../media/ev3dev-media/sounds/communication/good_job.wav>`

        .. data:: GOOD

            :download:`Preview <../../media/ev3dev-media/sounds/communication/good.wav>`

        .. data:: GOODBYE

            :download:`Preview <../../media/ev3dev-media/sounds/communication/goodbye.wav>`

        .. data:: HELLO

            :download:`Preview <../../media/ev3dev-media/sounds/communication/hello.wav>`

        .. data:: HI

            :download:`Preview <../../media/ev3dev-media/sounds/communication/hi.wav>`

        .. data:: LEGO

            :download:`Preview <../../media/ev3dev-media/sounds/communication/lego.wav>`

        .. data:: MINDSTORMS

            :download:`Preview <../../media/ev3dev-media/sounds/communication/mindstorms.wav>`

        .. data:: MORNING

            :download:`Preview <../../media/ev3dev-media/sounds/communication/morning.wav>`

        .. data:: NO

            :download:`Preview <../../media/ev3dev-media/sounds/communication/no.wav>`

        .. data:: OKAY

            :download:`Preview <../../media/ev3dev-media/sounds/communication/okay.wav>`

        .. data:: OKEY_DOKEY

            :download:`Preview <../../media/ev3dev-media/sounds/communication/okey-dokey.wav>`

        .. data:: SORRY

            :download:`Preview <../../media/ev3dev-media/sounds/communication/sorry.wav>`

        .. data:: THANK_YOU

            :download:`Preview <../../media/ev3dev-media/sounds/communication/thank_you.wav>`

        .. data:: YES

            :download:`Preview <../../media/ev3dev-media/sounds/communication/yes.wav>`


    .. toggle-header::
        :header: **Movement sounds**

        .. data:: SPEED_DOWN

            :download:`Preview <../../media/ev3dev-media/sounds/movements/speed_down.wav>`

        .. data:: SPEED_IDLE

            :download:`Preview <../../media/ev3dev-media/sounds/movements/speed_idle.wav>`

        .. data:: SPEED_UP

            :download:`Preview <../../media/ev3dev-media/sounds/movements/speed_up.wav>`

    .. toggle-header::
        :header: **Colors**

        .. data:: BLACK

            :download:`Preview <../../media/ev3dev-media/sounds/colors/black.wav>`

        .. data:: BLUE

            :download:`Preview <../../media/ev3dev-media/sounds/colors/blue.wav>`

        .. data:: BROWN

            :download:`Preview <../../media/ev3dev-media/sounds/colors/brown.wav>`

        .. data:: GREEN

            :download:`Preview <../../media/ev3dev-media/sounds/colors/green.wav>`

        .. data:: RED

            :download:`Preview <../../media/ev3dev-media/sounds/colors/red.wav>`

        .. data:: WHITE

            :download:`Preview <../../media/ev3dev-media/sounds/colors/white.wav>`

        .. data:: YELLOW

            :download:`Preview <../../media/ev3dev-media/sounds/colors/yellow.wav>`


    .. toggle-header::
        :header: **Mechanical**

        .. data:: AIR_RELEASE

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/air_release.wav>`

        .. data:: AIRBRAKE

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/airbrake.wav>`

        .. data:: BACKING_ALERT

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/backing_alert.wav>`

        .. data:: HORN_1

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/horn_1.wav>`

        .. data:: HORN_2

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/horn_2.wav>`

        .. data:: LASER

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/laser.wav>`

        .. data:: MOTOR_IDLE

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/motor_idle.wav>`

        .. data:: MOTOR_START

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/motor_start.wav>`

        .. data:: MOTOR_STOP

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/motor_stop.wav>`

        .. data:: RATCHET

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/ratchet.wav>`

        .. data:: SONAR

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/sonar.wav>`

        .. data:: TICK_TACK

            :download:`Preview <../../media/ev3dev-media/sounds/mechanical/tick_tack.wav>`


    .. toggle-header::
        :header: **Animal sounds**

        .. data:: CAT_PURR

            :download:`Preview <../../media/ev3dev-media/sounds/animals/cat_purr.wav>`

        .. data:: DOG_BARK_1

            :download:`Preview <../../media/ev3dev-media/sounds/animals/dog_bark_1.wav>`

        .. data:: DOG_BARK_2

            :download:`Preview <../../media/ev3dev-media/sounds/animals/dog_bark_2.wav>`

        .. data:: DOG_GROWL

            :download:`Preview <../../media/ev3dev-media/sounds/animals/dog_growl.wav>`

        .. data:: DOG_SNIFF

            :download:`Preview <../../media/ev3dev-media/sounds/animals/dog_sniff.wav>`

        .. data:: DOG_WHINE

            :download:`Preview <../../media/ev3dev-media/sounds/animals/dog_whine.wav>`

        .. data:: ELEPHANT_CALL

            :download:`Preview <../../media/ev3dev-media/sounds/animals/elephant_call.wav>`

        .. data:: INSECT_BUZZ_1

            :download:`Preview <../../media/ev3dev-media/sounds/animals/insect_buzz_1.wav>`

        .. data:: INSECT_BUZZ_2

            :download:`Preview <../../media/ev3dev-media/sounds/animals/insect_buzz_2.wav>`

        .. data:: INSECT_CHIRP

            :download:`Preview <../../media/ev3dev-media/sounds/animals/insect_chirp.wav>`

        .. data:: SNAKE_HISS

            :download:`Preview <../../media/ev3dev-media/sounds/animals/snake_hiss.wav>`

        .. data:: SNAKE_RATTLE

            :download:`Preview <../../media/ev3dev-media/sounds/animals/snake_rattle.wav>`

        .. data:: T_REX_ROAR

            :download:`Preview <../../media/ev3dev-media/sounds/animals/t-rex_roar.wav>`



    .. toggle-header::
        :header: **Numbers**

        .. data:: ZERO

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/zero.wav>`

        .. data:: ONE

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/one.wav>`

        .. data:: TWO

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/two.wav>`

        .. data:: THREE

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/three.wav>`

        .. data:: FOUR

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/four.wav>`

        .. data:: FIVE

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/five.wav>`

        .. data:: SIX

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/six.wav>`

        .. data:: SEVEN

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/seven.wav>`

        .. data:: EIGHT

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/eight.wav>`

        .. data:: NINE

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/nine.wav>`

        .. data:: TEN

            :download:`Preview <../../media/ev3dev-media/sounds/numbers/ten.wav>`


    .. toggle-header::
        :header: **System sounds**

        .. data:: CLICK

            :download:`Preview <../../media/ev3dev-media/sounds/system/click.wav>`

        .. data:: CONFIRM

            :download:`Preview <../../media/ev3dev-media/sounds/system/confirm.wav>`

        .. data:: GENERAL_ALERT

            :download:`Preview <../../media/ev3dev-media/sounds/system/general_alert.wav>`

        .. data:: OVERPOWER

            :download:`Preview <../../media/ev3dev-media/sounds/system/overpower.wav>`

        .. data:: READY

            :download:`Preview <../../media/ev3dev-media/sounds/system/ready.wav>`



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


.. tip:: Behind the scenes, Pybricks uses Fontconfig_ for fonts. The Fontconfig
         command line tools can be used to explore available fonts in more
         detail.

         Example::

             # List available font families.
             fc-list :scalable=false:dpi=119 family
             # Perform lookup similar to Font.DEFAULT
             fc-match :scalable=false:dpi=119:family=Lucida:size=12
             # Perform lookup similar to Font(size=24,lang=zh-cn)
             fc-match :scalable=false:dpi=119:size=24:lang=zh-cn

         Pybricks only allows the use of bitmap fonts (``scalable=false``)
         and the screen on the EV3 has 119 pixels per inch (``dpi=119``).

.. _FontConfig: https://www.freedesktop.org/wiki/Software/fontconfig/


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
