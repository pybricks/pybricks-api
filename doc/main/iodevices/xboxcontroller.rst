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

      * ``"A"``, ``"B"``, ``"X"``, ``"Y"``.
      * ``"LB"`` and ``"RB"`` (bumpers).
      * ``"LJ"`` and ``"RJ"`` (pressing the joysticks).
      * ``"VIEW"``, ``"MENU"``, ``"GUIDE"`` (the Xbox logo), and ``"UPLOAD"``.
      * ``"P1"``, ``"P2"``, ``"P3"``, and ``"P4"`` (Elite Series 2 only).
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


