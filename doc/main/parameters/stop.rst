.. pybricks-requirements::

Stop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Stop

    Action after the motor stops.

    .. autoattribute:: pybricks.parameters.Stop.COAST
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.COAST_SMART
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.BRAKE
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.HOLD
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.NONE
        :annotation:

    The following table shows how each of the basic stop types add an extra
    level of resistance to motion. In these examples, ``m`` is a
    :class:`Motor <pybricks.pupdevices.Motor>` and
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
