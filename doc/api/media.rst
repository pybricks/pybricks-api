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

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/boing.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/boing.wav>`

        .. data:: BOO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/boo.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/boo.wav>`

        .. data:: CHEERING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/cheering.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/cheering.wav>`

        .. data:: CRUNCHING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/crunching.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/crunching.wav>`

        .. data:: CRYING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/crying.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/crying.wav>`

        .. data:: FANFARE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/fanfare.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/fanfare.wav>`

        .. data:: KUNG_FU

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/kung_fu.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/kung_fu.wav>`

        .. data:: LAUGHING_1

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/laughing_1.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/laughing_1.wav>`

        .. data:: LAUGHING_2

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/laughing_2.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/laughing_2.wav>`

        .. data:: MAGIC_WAND

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/magic_wand.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/magic_wand.wav>`

        .. data:: OUCH

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/ouch.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/ouch.wav>`

        .. data:: SHOUTING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/shouting.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/shouting.wav>`

        .. data:: SMACK

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/smack.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/smack.wav>`

        .. data:: SNEEZING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/sneezing.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/sneezing.wav>`

        .. data:: SNORING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/snoring.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/snoring.wav>`

        .. data:: UH_OH

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/uh-oh.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/expressions/uh-oh.wav>`


    .. toggle-header::
        :header: **Information**

        .. data:: ACTIVATE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/activate.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/activate.wav>`

        .. data:: ANALYZE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/analyze.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/analyze.wav>`

        .. data:: BACKWARDS

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/backwards.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/backwards.wav>`

        .. data:: COLOR

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/color.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/color.wav>`

        .. data:: DETECTED

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/detected.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/detected.wav>`

        .. data:: DOWN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/down.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/down.wav>`

        .. data:: ERROR

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/error.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/error.wav>`

        .. data:: ERROR_ALARM

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/error_alarm.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/error_alarm.wav>`


        .. data:: FLASHING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/flashing.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/flashing.wav>`

        .. data:: FORWARD

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/forward.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/forward.wav>`

        .. data:: LEFT

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/left.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/left.wav>`

        .. data:: OBJECT

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/object.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/object.wav>`

        .. data:: RIGHT

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/right.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/right.wav>`

        .. data:: SEARCHING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/searching.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/searching.wav>`

        .. data:: START

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/start.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/start.wav>`

        .. data:: STOP

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/stop.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/stop.wav>`

        .. data:: TOUCH

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/touch.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/touch.wav>`

        .. data:: TURN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/turn.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/turn.wav>`

        .. data:: UP

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/up.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/information/up.wav>`

    .. toggle-header::
        :header: **Communication**

        .. data:: BRAVO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/bravo.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/bravo.wav>`

        .. data:: EV3

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/ev3.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/ev3.wav>`

        .. data:: FANTASTIC

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/fantastic.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/fantastic.wav>`

        .. data:: GAME_OVER

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/game_over.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/game_over.wav>`

        .. data:: GO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/go.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/go.wav>`

        .. data:: GOOD_JOB

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/good_job.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/good_job.wav>`

        .. data:: GOOD

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/good.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/good.wav>`

        .. data:: GOODBYE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/goodbye.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/goodbye.wav>`

        .. data:: HELLO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/hello.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/hello.wav>`

        .. data:: HI

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/hi.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/hi.wav>`

        .. data:: LEGO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/lego.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/lego.wav>`

        .. data:: MINDSTORMS

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/mindstorms.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/mindstorms.wav>`

        .. data:: MORNING

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/morning.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/morning.wav>`

        .. data:: NO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/no.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/no.wav>`

        .. data:: OKAY

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/okay.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/okay.wav>`

        .. data:: OKEY_DOKEY

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/okey-dokey.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/okey-dokey.wav>`

        .. data:: SORRY

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/sorry.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/sorry.wav>`

        .. data:: THANK_YOU

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/thank_you.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/thank_you.wav>`

        .. data:: YES

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/yes.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/communication/yes.wav>`


    .. toggle-header::
        :header: **Movement sounds**

        .. data:: SPEED_DOWN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/speed_down.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/movements/speed_down.wav>`

        .. data:: SPEED_IDLE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/speed_idle.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/movements/speed_idle.wav>`

        .. data:: SPEED_UP

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/speed_up.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/movements/speed_up.wav>`

    .. toggle-header::
        :header: **Colors**

        .. data:: BLACK

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/black.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/black.wav>`

        .. data:: BLUE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/blue.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/blue.wav>`

        .. data:: BROWN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/brown.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/brown.wav>`

        .. data:: GREEN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/green.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/green.wav>`

        .. data:: RED

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/red.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/red.wav>`

        .. data:: WHITE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/white.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/white.wav>`

        .. data:: YELLOW

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/yellow.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/colors/yellow.wav>`


    .. toggle-header::
        :header: **Mechanical**

        .. data:: AIR_RELEASE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/air_release.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/air_release.wav>`

        .. data:: AIRBRAKE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/airbrake.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/airbrake.wav>`

        .. data:: BACKING_ALERT

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/backing_alert.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/backing_alert.wav>`

        .. data:: HORN_1

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/horn_1.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/horn_1.wav>`

        .. data:: HORN_2

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/horn_2.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/horn_2.wav>`

        .. data:: LASER

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/laser.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/laser.wav>`

        .. data:: MOTOR_IDLE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/motor_idle.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/motor_idle.wav>`

        .. data:: MOTOR_START

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/motor_start.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/motor_start.wav>`

        .. data:: MOTOR_STOP

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/motor_stop.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/motor_stop.wav>`

        .. data:: RATCHET

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/ratchet.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/ratchet.wav>`

        .. data:: SONAR

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/sonar.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/sonar.wav>`

        .. data:: TICK_TACK

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/tick_tack.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/mechanical/tick_tack.wav>`


    .. toggle-header::
        :header: **Animal sounds**

        .. data:: CAT_PURR

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/cat_purr.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/cat_purr.wav>`

        .. data:: DOG_BARK_1

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/dog_bark_1.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/dog_bark_1.wav>`

        .. data:: DOG_BARK_2

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/dog_bark_2.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/dog_bark_2.wav>`

        .. data:: DOG_GROWL

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/dog_growl.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/dog_growl.wav>`

        .. data:: DOG_SNIFF

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/dog_sniff.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/dog_sniff.wav>`

        .. data:: DOG_WHINE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/dog_whine.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/dog_whine.wav>`

        .. data:: ELEPHANT_CALL

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/elephant_call.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/elephant_call.wav>`

        .. data:: INSECT_BUZZ_1

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/insect_buzz_1.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/insect_buzz_1.wav>`

        .. data:: INSECT_BUZZ_2

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/insect_buzz_2.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/insect_buzz_2.wav>`

        .. data:: INSECT_CHIRP

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/insect_chirp.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/insect_chirp.wav>`

        .. data:: SNAKE_HISS

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/snake_hiss.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/snake_hiss.wav>`

        .. data:: SNAKE_RATTLE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/snake_rattle.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/snake_rattle.wav>`

        .. data:: T_REX_ROAR

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/t-rex_roar.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/animals/t-rex_roar.wav>`



    .. toggle-header::
        :header: **Numbers**

        .. data:: ZERO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/zero.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/zero.wav>`

        .. data:: ONE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/one.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/one.wav>`

        .. data:: TWO

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/two.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/two.wav>`

        .. data:: THREE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/three.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/three.wav>`

        .. data:: FOUR

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/four.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/four.wav>`

        .. data:: FIVE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/five.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/five.wav>`

        .. data:: SIX

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/six.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/six.wav>`

        .. data:: SEVEN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/seven.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/seven.wav>`

        .. data:: EIGHT

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/eight.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/eight.wav>`

        .. data:: NINE

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/nine.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/nine.wav>`

        .. data:: TEN

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/ten.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/numbers/ten.wav>`


    .. toggle-header::
        :header: **System sounds**

        .. data:: CLICK

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/click.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/system/click.wav>`

        .. data:: CONFIRM

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/confirm.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/system/confirm.wav>`

        .. data:: GENERAL_ALERT

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/general_alert.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/system/general_alert.wav>`

        .. data:: OVERPOWER

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/overpower.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/system/overpower.wav>`

        .. data:: READY

            .. raw:: html

                <audio controls="controls">
                    <source src="_downloads/ready.wav" type="audio/wav">
                    Your browser does not support the <code>audio</code> element.
                </audio>

            :download:`Download <../../media/ev3dev-media/sounds/system/ready.wav>`



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

    **Exploring more fonts**

    Behind the scenes, Pybricks uses Fontconfig_ for fonts. The Fontconfig
    command line tools can be used to explore available fonts in more
    detail. To do so, go to the ev3dev device browser,
    right click on your EV3 brick, and click *Open SSH Terminal*. Then you can
    enter one of these commands::

        # List available font families.
        fc-list :scalable=false family
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

.. rubric:: Available languages for fonts

.. [#font_lang]

    Note: Languages depend on installed fonts. Additional language
    codes are possible and some listed language codes may not have
    a satisfactory font.

    - ``'aa'``: Afar
    - ``'af'``: Afrikaans
    - ``'an'``: Aragonese
    - ``'av'``: Avaric
    - ``'ay'``: Aymara
    - ``'az-az'``: Azerbaijani
    - ``'be'``: Belarusian
    - ``'bg'``: Bulgarian
    - ``'bi'``: Bislama
    - ``'bm'``: Bambara
    - ``'br'``: Breton
    - ``'bs'``: Bosnian
    - ``'bua'``: Buriat
    - ``'ca'``: Catalan
    - ``'ce'``: Chechen
    - ``'ch'``: Chamorro
    - ``'co'``: Corsican
    - ``'crh'``: Crimean
    - ``'cs'``: Czech
    - ``'csb'``: Kashubian
    - ``'cy'``: Welsh
    - ``'da'``: Danish
    - ``'de'``: German
    - ``'ee'``: Ewe
    - ``'el'``: Greek
    - ``'en'``: English
    - ``'eo'``: Esperanto
    - ``'es'``: Spanish
    - ``'et'``: Estonian
    - ``'eu'``: Basque
    - ``'ff'``: Fulah
    - ``'fi'``: Finnish
    - ``'fil'``: Filipino
    - ``'fj'``: Fijian
    - ``'fo'``: Faroese
    - ``'fr'``: French
    - ``'fur'``: Friulian
    - ``'fy'``: Western Frisian
    - ``'ga'``: Irish
    - ``'gd'``: Gaelic
    - ``'gl'``: Galician
    - ``'gv'``: Manx
    - ``'ha'``: Hausa
    - ``'haw'``: Hawaiian
    - ``'he'``: Hebrew
    - ``'ho'``: Hiri Motu
    - ``'hr'``: Croatian
    - ``'hsb'``: Upper Sorbian
    - ``'ht'``: Haitian
    - ``'hu'``: Hungarian
    - ``'ia'``: Interlingua
    - ``'id'``: Indonesian
    - ``'ie'``: Interlingue
    - ``'ik'``: Inupiaq
    - ``'io'``: Ido
    - ``'is'``: Icelandic
    - ``'it'``: Italian
    - ``'ja'``: Japanese
    - ``'jv'``: Javanese
    - ``'ki'``: Kikuyu
    - ``'kj'``: Kuanyama
    - ``'kl'``: Kalaallisut
    - ``'ko'``: Korean
    - ``'ku-tr'``: Kurdish
    - ``'kum'``: Kumyk
    - ``'kw'``: Cornish
    - ``'kwm'``: Kwambi
    - ``'la'``: Latin
    - ``'lb'``: Luxembourgish
    - ``'lez'``: Lezghian
    - ``'lg'``: Ganda
    - ``'li'``: Limburgan
    - ``'ln'``: Lingala
    - ``'lt'``: Lithuanian
    - ``'lv'``: Latvian
    - ``'mg'``: Malagasy
    - ``'mh'``: Marshallese
    - ``'mi'``: Maori
    - ``'mk'``: Macedonian
    - ``'mn-mn'``: Mongolian
    - ``'mo'``: Moldavian
    - ``'ms'``: Malay
    - ``'mt'``: Maltese
    - ``'na'``: Nauru
    - ``'nb'``: Norwegian Bokmål
    - ``'nds'``: Low German
    - ``'ng'``: Ndonga
    - ``'nl'``: Dutch
    - ``'nn'``: Norwegian Nynorsk
    - ``'no'``: Norwegian
    - ``'nr'``: South Ndebele
    - ``'nso'``: Northern Sotho
    - ``'nv'``: Navajo
    - ``'ny'``: Chichewa
    - ``'oc'``: Occitan
    - ``'om'``: Oromo
    - ``'os'``: Ossetian
    - ``'pap-an'``: Papiamento, Netherlands Antilles
    - ``'pap-aw'``: Papiamento, Aruba
    - ``'pl'``: Polish
    - ``'pt'``: Portuguese
    - ``'qu'``: Quechua
    - ``'quz'``: Cusco Quechua
    - ``'rm'``: Romansh
    - ``'rn'``: Rundi
    - ``'ro'``: Romanian
    - ``'ru'``: Russian
    - ``'rw'``: Kinyarwanda
    - ``'sc'``: Sardinian
    - ``'sco'``: Scots
    - ``'se'``: Northern Sami
    - ``'sel'``: Selkup
    - ``'sg'``: Sango
    - ``'sk'``: Slovak
    - ``'sl'``: Slovenian
    - ``'sm'``: Samoan
    - ``'sma'``: Southern Sami
    - ``'smj'``: Lule Sami
    - ``'smn'``: Inari Sami
    - ``'sms'``: Skolt Sami
    - ``'sn'``: Shona
    - ``'so'``: Somali
    - ``'sq'``: Albanian
    - ``'sr'``: Serbian
    - ``'ss'``: Swati
    - ``'st'``: Southern Sotho
    - ``'su'``: Sundanese
    - ``'sv'``: Swedish
    - ``'sw'``: Swahili
    - ``'tk'``: Turkmen
    - ``'tl'``: Tagalog
    - ``'tn'``: Tswana
    - ``'to'``: Tonga
    - ``'tr'``: Turkish
    - ``'ts'``: Tsonga
    - ``'ty'``: Tahitian
    - ``'uk'``: Ukrainian
    - ``'uz'``: Uzbek
    - ``'vo'``: Volapük
    - ``'vot'``: Votic
    - ``'wa'``: Walloon
    - ``'wen'``: Sorbian
    - ``'wo'``: Wolof
    - ``'xh'``: Xhosa
    - ``'yap'``: Yapese
    - ``'yi'``: Yiddish
    - ``'za'``: Zhuang
    - ``'zh-cn'``: Chinese, China
    - ``'zh-sg'``: Chinese, Singapore
    - ``'zh-tw'``: Chinese, Taiwan
    - ``'zu'``: Zulu
