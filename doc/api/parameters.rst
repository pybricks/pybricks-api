:mod:`parameters <pybricks.parameters>` -- Parameters and Constants
===================================================================

.. automodule:: pybricks.parameters
    :no-members:

.. autoclass:: pybricks.parameters.Port
    :no-members:

    .. content-tabs::

        .. tab-container:: ev3brick
            :title: EV3 Brick

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

        .. tab-container:: movehub
            :title: Move Hub

            Input/Output ports:

                .. data:: A
                .. data:: B
                .. data:: C
                .. data:: D

        .. tab-container:: cityhub
            :title: City Hub

            Input/Output ports:

                .. data:: A
                .. data:: B

.. autoclass:: pybricks.parameters.Direction
    :no-members:

    In general, clockwise is defined by **looking at the motor shaft, just
    like looking at a clock**.

    Some motors have two shafts. If in doubt, refer to the following diagrams:

        - Clockwise direction for :ref:`EV3/NXT motors <fig_ev3motors>`
        - Clockwise direction for :ref:`Powered Up Motors <fig_pupmotors>`
        - Clockwise direction for :ref:`Move Hub Motors <fig_movehub>`

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

    .. rubric:: Saturated colors

    .. autoattribute:: RED

        .. pybricks-color:: RED

    .. autoattribute:: ORANGE

        .. pybricks-color:: ORANGE

    .. autoattribute:: YELLOW

        .. pybricks-color:: YELLOW

    .. autoattribute:: GREEN

        .. pybricks-color:: GREEN

    .. autoattribute:: CYAN

        .. pybricks-color:: CYAN

    .. autoattribute:: BLUE

        .. pybricks-color:: BLUE

    .. autoattribute:: VIOLET

        .. pybricks-color:: VIOLET

    .. autoattribute:: MAGENTA

        .. pybricks-color:: MAGENTA

    .. rubric:: Unsaturated colors

    .. autoattribute:: BLACK

        .. pybricks-color:: BLACK

    .. autoattribute:: GRAY

        .. pybricks-color:: GRAY

    .. autoattribute:: WHITE

        .. pybricks-color:: WHITE

.. autoclass:: pybricks.parameters.Button
    :no-members:

.. .. autoclass:: pybricks.parameters.Axis
..     :no-members:

.. autoclass:: pybricks.parameters.Side
    :no-members:

    Screens or light matrices have only four sides. For those,
    ``TOP`` is treated the same as ``FRONT``, and ``BOTTOM`` is treated the
    same as ``BACK``.

    Click a tab below to see the sides for relevant devices.

    .. content-tabs::

        .. tab-container:: primehub
            :title: Prime Hub

            .. figure:: ../api/images/orientation_primehub_label.png
                :height: 20 em

        .. tab-container:: inventorhub
            :title: Inventor Hub

            .. figure:: ../api/images/orientation_inventorhub_label.png
                :height: 20 em

        .. tab-container:: movehub
            :title: Move Hub

            .. figure:: ../api/images/orientation_movehub_label.png
                :height: 20 em

        .. tab-container:: technichub
            :title: Technic Hub

            .. figure:: ../api/images/orientation_technichub_label.png
                :height: 20 em

        .. tab-container:: tiltsensor
            :title: Tilt Sensor

            .. figure:: ../api/images/orientation_tiltsensor_label.png
                :height: 20 em
