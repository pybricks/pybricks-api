.. pybricks-requirements:: primehub

Prime Hub / Inventor Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-spike-inventor.png
    :width: 80%

.. class:: InventorHub

    This class is the same as the ``PrimeHub`` class, shown below. Both classes
    work on both hubs.

    These hubs are completely identical. They use the same Pybricks firmware.

.. autoclass:: pybricks.hubs.PrimeHub
    :no-members:

    .. rubric:: Using the hub status light

    .. figure:: ../../main/diagrams/primehub_light.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.light.on

    .. automethod:: pybricks.hubs::PrimeHub.light.off

    .. automethod:: pybricks.hubs::PrimeHub.light.blink

    .. automethod:: pybricks.hubs::PrimeHub.light.animate

    .. rubric:: Using the light matrix display

    .. figure:: ../../main/diagrams/primehub_display.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.display.orientation

    .. automethod:: pybricks.hubs::PrimeHub.display.off

    .. automethod:: pybricks.hubs::PrimeHub.display.pixel

    .. automethod:: pybricks.hubs::PrimeHub.display.icon

    .. automethod:: pybricks.hubs::PrimeHub.display.animate

    .. automethod:: pybricks.hubs::PrimeHub.display.number

    .. automethod:: pybricks.hubs::PrimeHub.display.char

    .. automethod:: pybricks.hubs::PrimeHub.display.text

    .. rubric:: Using the buttons

    .. figure:: ../../main/diagrams/primehub_buttons.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.buttons.pressed

    .. rubric:: Using the IMU

    .. automethod:: pybricks.hubs::PrimeHub.imu.ready

    .. automethod:: pybricks.hubs::PrimeHub.imu.stationary

    .. automethod:: pybricks.hubs::PrimeHub.imu.up

    .. automethod:: pybricks.hubs::PrimeHub.imu.tilt

    .. automethod:: pybricks.hubs::PrimeHub.imu.acceleration

    .. automethod:: pybricks.hubs::PrimeHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::PrimeHub.imu.heading

    .. automethod:: pybricks.hubs::PrimeHub.imu.reset_heading

    .. automethod:: pybricks.hubs::PrimeHub.imu.rotation

    .. automethod:: pybricks.hubs::PrimeHub.imu.orientation

    .. automethod:: pybricks.hubs::PrimeHub.imu.settings

    .. rubric:: Using the speaker

    .. automethod:: pybricks.hubs::PrimeHub.speaker.volume

    .. automethod:: pybricks.hubs::PrimeHub.speaker.beep

    .. automethod:: pybricks.hubs::PrimeHub.speaker.play_notes

    .. rubric:: Using the battery

    .. automethod:: pybricks.hubs::PrimeHub.battery.voltage

    .. automethod:: pybricks.hubs::PrimeHub.battery.current

    .. rubric:: Getting the charger status

    .. automethod:: pybricks.hubs::PrimeHub.charger.connected

    .. automethod:: pybricks.hubs::PrimeHub.charger.current

    .. automethod:: pybricks.hubs::PrimeHub.charger.status

    .. rubric:: System control

    .. automethod:: pybricks.hubs::PrimeHub.system.set_stop_button

    .. automethod:: pybricks.hubs::PrimeHub.system.name

    .. automethod:: pybricks.hubs::PrimeHub.system.storage

        You can store up to 512 bytes of data on this hub.

    .. automethod:: pybricks.hubs::PrimeHub.system.shutdown

    .. automethod:: pybricks.hubs::PrimeHub.system.reset_reason

.. note:: The examples below use the ``PrimeHub`` class. The examples work fine
        on both hubs because they are the identical. If you prefer, you can
        change this to ``InventorHub``.

Status light examples
---------------------

Turning the light on and off
****************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_primehub.py

Changing brightness and using custom colors
*******************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_primehub.py

Making the light blink
**********************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_primehub.py

Creating light animations
*************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_primehub.py

Matrix display examples
-----------------------

Displaying images
*****************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_image.py

Displaying numbers
******************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_number.py

Displaying text
***************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_text.py

Displaying individual pixels
****************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_pixel.py

Changing the display orientation
********************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_orientation.py

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_orientation_imu.py

.. _make_icons:

Making your own images
**********************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_matrix.py

Combining icons to make expressions
************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_expression.py

Displaying animations
*********************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_animate.py

Button examples
---------------

Detecting button presses
************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/button_main.py

IMU examples
---------------

Testing which way is up
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_primehub.py


Reading the tilt value
********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_primehub.py

Using a custom hub orientation
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_primehub.py

Reading acceleration and angular velocity vectors
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_primehub.py

Reading acceleration and angular velocity on one axis
*****************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_primehub.py

System examples
----------------------------------

Changing the stop button combination
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/button_stop.py

Turning the hub off
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_primehub.py

