:mod:`parameters <pybricks.parameters>` -- Parameters and Constants
===================================================================

.. automodule:: pybricks.parameters
    :no-members:

.. autoclass:: pybricks.parameters.Port
    :no-members:

    Motor ports:

    .. data:: A
    .. data:: B
    .. data:: C
    .. data:: D

    Sensor ports:

    .. data:: S1
    .. data:: S2
    .. data:: S3
    .. data:: S4

.. autoclass:: pybricks.parameters.Direction
    :no-members:

    In general, clockwise is defined by **looking at the motor shaft, just
    like looking at a clock**.

    Some motors have two shafts. If in doubt, refer to the following diagrams:

        - Clockwise direction for :ref:`EV3/NXT motors <fig_ev3motors>`

.. autoclass:: pybricks.parameters.Stop
    :no-members:

    The following table show how each stop type adds an extra level of
    resistance to motion. In these examples, ``m`` is a
    :class:`Motor <pybricks.ev3devices.Motor>` and
    and ``d`` is a :class:`DriveBase <pybricks.robotics.DriveBase>`. The
    examples also show how running at zero speed compares to these stop types.

    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    | | Type | | Friction | | Back | | Speed     |  | Angle kept | | Examples                              |
    |        |            | | EMF  | | kept at 0 |  | at target  |                                         |
    +========+============+========+=============+===============+=========================================+
    | Coast  | +          |        |             |               | | ``m.stop()``                          |
    |        |            |        |             |               | | ``m.run_target(500, 90, Stop.COAST)`` |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    | Brake  | +          | +      |             |               | | ``m.brake()``                         |
    |        |            |        |             |               | | ``m.run_target(500, 90, Stop.BRAKE)`` |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    |        | +          | +      | +           |               | | ``m.run(0)``                          |
    |        |            |        |             |               | | ``d.drive(0, 0)``                     |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    | Hold   | +          | +      | +           | +             | | ``m.hold()``                          |
    |        |            |        |             |               | | ``m.run_target(500, 90, Stop.HOLD)``  |
    |        |            |        |             |               | | ``d.straight(0)``                     |
    |        |            |        |             |               | | ``d.straight(100)``                   |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+

.. autoclass:: pybricks.parameters.Color
    :no-members:

.. autoclass:: pybricks.parameters.Button
    :no-members:
