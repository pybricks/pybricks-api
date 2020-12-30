MINDSTORMS Inventor Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../api/images/inventorhub.png
    :height: 15 em

.. autoclass:: pybricks.hubs.InventorHub
    :no-members:

    This class is identical to the
    :class:`PrimeHub <pybricks.hubs.PrimeHub>` class, except
    for the name.

    .. rubric:: Using the hub status light

    .. figure:: ../../api/images/primehub_light_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::InventorHub.light.on

    .. automethod:: pybricks.hubs::InventorHub.light.off

    .. automethod:: pybricks.hubs::InventorHub.light.blink

    .. automethod:: pybricks.hubs::InventorHub.light.animate

    .. rubric:: Using the light matrix display

    .. figure:: ../../api/images/primehub_display_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::InventorHub.display.orientation

    .. automethod:: pybricks.hubs::InventorHub.display.off

    .. automethod:: pybricks.hubs::InventorHub.display.pixel

    .. automethod:: pybricks.hubs::InventorHub.display.image

    .. automethod:: pybricks.hubs::InventorHub.display.animate

    .. automethod:: pybricks.hubs::InventorHub.display.number

    .. automethod:: pybricks.hubs::InventorHub.display.char

    .. automethod:: pybricks.hubs::InventorHub.display.text

    .. rubric:: Using the buttons

    .. figure:: ../../api/images/primehub_buttons_label.png
        :width: 22 em

    .. automethod:: pybricks.hubs::InventorHub.buttons.pressed

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::InventorHub.imu.acceleration

    .. automethod:: pybricks.hubs::InventorHub.imu.gyro

    .. rubric:: Using the speaker

    .. automethod:: pybricks.hubs::InventorHub.speaker.beep

    .. automethod:: pybricks.hubs::InventorHub.speaker.play_notes

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::InventorHub.battery.voltage

    .. automethod:: pybricks.hubs::InventorHub.battery.current

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/light_off.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/light_hsv.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/light_blink.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/light_animate.py

Matrix display examples
-----------------------

Displaying images
*****************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_image.py

Displaying numbers
******************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_number.py

Displaying text
***************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_text.py

Displaying individual pixels
****************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_pixel.py

Changing the display orientation
********************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_orientation.py

Making your own images
**********************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_matrix.py

Combining images to make expressions
************************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_expression.py

Displaying animations
*********************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/display_animate.py

Button examples
---------------

Detecting button presses
************************

.. literalinclude::
    ../../../examples/pup/hub_inventorhub/button_main.py
