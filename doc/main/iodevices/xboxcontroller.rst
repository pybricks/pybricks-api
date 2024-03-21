.. pybricks-requirements:: xbox-controller

Xbox Controller
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams_source/xboxcontroller.png
   :width: 60 %

.. blockimg:: pybricks_variables_set_xbox_controller

.. autoclass:: pybricks.iodevices.XboxController
  :no-members:

  .. blockimg:: pybricks_blockButtonIsPressed_XboxController

  .. automethod:: pybricks.iodevices::XboxController.buttons.pressed

    Buttons include:

      * ``Button.A``, ``Button.B``, ``Button.X``, ``Button.Y``.
      * ``Button.UP``, ``Button.DOWN``, ``Button.LEFT``, ``Button.RIGHT``
        (direction pad). At most two of these can be pressed at the same time.
      * ``Button.LB`` and ``Button.RB`` (bumpers).
      * ``Button.LJ`` and ``Button.RJ`` (pressing the joysticks).
      * ``Button.VIEW``, ``Button.MENU``, ``Button.GUIDE`` (the Xbox logo), and ``Button.UPLOAD``.
      * ``Button.P1``, ``Button.P2``, ``Button.P3``, and ``Button.P4`` (Elite Series 2 only).
        Pressing the paddles may also be detected as other button presses,
        depending on the currently active profile.

  .. blockimg:: pybricks_blockJoystickValue_lj_x

  .. blockimg:: pybricks_blockJoystickValue_lj_y
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.joystick_left

  .. blockimg:: pybricks_blockJoystickValue_rj_x

  .. blockimg:: pybricks_blockJoystickValue_rj_y
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.joystick_right

  .. blockimg:: pybricks_blockJoystickValue_lt

  .. blockimg:: pybricks_blockJoystickValue_rt
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.triggers

  .. blockimg:: pybricks_blockJoystickValue_dpad

  .. automethod:: pybricks.iodevices::XboxController.dpad

  .. blockimg:: pybricks_blockJoystickValue_profile

  .. automethod:: pybricks.iodevices::XboxController.profile

  .. blockimg:: pybricks_blockGamepadRumble_default

  .. blockimg:: pybricks_blockGamepadRumble_default_with_list
      :stack:

  .. blockimg:: pybricks_blockGamepadRumble_with_options
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.rumble

.. _xbox-controller-pairing:

Xbox Controller Pairing Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The first time you use a controller with a hub, you will need to pair
them: Turn the controller on and then press and hold the pairing
button on the back of the controller for a few seconds. When you release
it, the Xbox button starts flashing more rapidly. Then start your program.

When pairing and the connection is succesful, the Xbox button will stop
flashing and stay on for as long as the program is running.

Repeat Connections
==================

If you keep using the same controller with the same hub, you can simply
turn the controller on the next time and the hub will connect to it
automatically when your program with this class runs.

The Xbox controller only accepts this simpler connection with the most
recently connected device. So if you connect to your Xbox console again, or
connect to another hub, you will need to pair them again as described
above.

Compatible Controllers
============================

All Xbox controllers released since 2016 are compatible. This includes the
controller from the One S (``1708`` from 2016), the Elite Series 2 (``1797``
from 2019), and the Series X/S (``1914`` from 2020), which is
the latest model as of this writing.

.. raw:: html

  <p>See also <a href="https://en.wikipedia.org/wiki/Xbox_Wireless_Controller#Summary" target="_blank">
  this overview</a> of model numbers including pictures of each controller.</p>

Updating the Xbox Controller
============================

If you frequently use the Xbox Controller with your console, your controller
is probably already up to date. If you have not used it for a while or if you
bought one recently, you may need to update it.

To update the controller without a console, you can use the Xbox Accessories
app on a Windows computer. You can download it from the Microsoft Store.
Connect the controller via USB to the computer and follow the instructions in
the app to click on "Update now".

Technic Hub Limitations
=======================

Due to limitations of the Technic Hub, the hub will disconnect from the
computer when searching for the Xbox controller. This means you will not be
able to see output from the ``print`` command. Also, you'll have to connect to
the computer again if you want to change your program.
