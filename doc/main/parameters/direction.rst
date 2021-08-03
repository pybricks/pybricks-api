.. pybricks-requirements::

Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Direction

    Rotational direction for positive speed or angle values.

    .. autoattribute:: pybricks.parameters.Direction.CLOCKWISE
        :annotation:

    .. autoattribute:: pybricks.parameters.Direction.COUNTERCLOCKWISE
        :annotation:

    +--------------------------------+-------------------+-----------------+
    | ``positive_direction =``       | Positive speed:   | Negative speed: |
    +================================+===================+=================+
    | ``Direction.CLOCKWISE``        | clockwise         | counterclockwise|
    +--------------------------------+-------------------+-----------------+
    | ``Direction.COUNTERCLOCKWISE`` | counterclockwise  | clockwise       |
    +--------------------------------+-------------------+-----------------+

    In general, clockwise is defined by **looking at the motor shaft, just
    like looking at a clock**. Some motors have two shafts. If in doubt,
    refer to the diagram in the ``Motor`` class documentation.
