.. pybricks-requirements:: playstation-controller

PlayStation Controller
^^^^^^^^^^^^^^^^^^^^^^^^^

.. blockimg:: pybricks_variables_set_xbox_controller

.. autoclass:: pybricks.iodevices.PlayStationController
  :no-members:

  .. automethod:: pybricks.iodevices::PlayStationController.name

  .. blockimg:: pybricks_blockButtonIsPressed_XboxController

  .. automethod:: pybricks.iodevices::PlayStationController.buttons.pressed

    Buttons include:

      * ``Button.A`` (cross), ``Button.B`` (circle), ``Button.X`` (square),
        and ``Button.Y`` (triangle).
      * ``Button.UP``, ``Button.DOWN``, ``Button.LEFT``, ``Button.RIGHT``
        (direction pad). At most two of these can be pressed at the same time.
      * ``Button.LB`` and ``Button.RB`` (L1 and R1).
      * ``Button.LJ`` and ``Button.RJ`` (L3 and R3, pressing the joysticks).
      * ``Button.VIEW`` (share or create), ``Button.MENU`` (options),
        ``Button.GUIDE`` (the PlayStation logo), and ``Button.UPLOAD``
        (pressing the touchpad).

    .. note:: The buttons are currently reported using the names of the
       equivalent buttons on the Xbox controller, as listed above. This will
       change in a future version.

  .. blockimg:: pybricks_blockJoystickValue_xbox_lj_x

  .. blockimg:: pybricks_blockJoystickValue_xbox_lj_y

  .. automethod:: pybricks.iodevices::PlayStationController.joystick_left

  .. blockimg:: pybricks_blockJoystickValue_xbox_rj_x

  .. blockimg:: pybricks_blockJoystickValue_xbox_rj_y

  .. automethod:: pybricks.iodevices::PlayStationController.joystick_right

  .. blockimg:: pybricks_blockJoystickValue_xbox_lt

  .. blockimg:: pybricks_blockJoystickValue_xbox_rt

  .. automethod:: pybricks.iodevices::PlayStationController.triggers

  .. blockimg:: pybricks_blockJoystickValue_xbox_dpad

  .. automethod:: pybricks.iodevices::PlayStationController.dpad

.. _playstation-controller-pairing:

PlayStation Controller Pairing Instructions
===========================================

The first time you use a controller with a hub, you will need to pair them
using the hub menu:

1. On the hub, go to the settings tab and choose ``Add new gamepad``.
2. Put the controller in pairing mode: press and hold the share (or create)
   button and the PlayStation button at the same time until the light starts
   flashing rapidly.
3. Select the controller on the hub when it appears in the list.

When the connection is successful, the light on the controller stops flashing.
You can now start your program. Only one controller can be connected at a
time.

Repeat Connections
------------------

If you keep using the same controller with the same hub, you can simply
press the PlayStation button on the controller the next time and it will
connect to the hub automatically.

If you connect the controller to your console or to another device in the
meantime, you will need to pair it with the hub again as described above.
