.. pybricks-requirements::

Side
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Side

    Side of a hub or a sensor. These devices are
    mostly rectangular boxes with six sides:

    .. autoattribute:: pybricks.parameters.Side.TOP
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.BOTTOM
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.FRONT
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.BACK
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.LEFT
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.RIGHT
        :annotation:


    Screens or light matrices have only four sides. For those,
    ``TOP`` is treated the same as ``FRONT``, and ``BOTTOM`` is treated the
    same as ``BACK``. The diagrams below define the sides for relevant devices.

    **Prime Hub**

    .. figure:: ../../main/diagrams/orientation_primehub.png
        :width: 60%

    **Inventor Hub**

    .. figure:: ../../main/diagrams/orientation_inventorhub.png
        :width: 60%

    **Essential Hub**

    .. figure:: ../../main/diagrams/orientation_essentialhub.png
        :width: 60%

    **Move Hub**

    .. figure:: ../../main/diagrams/orientation_movehub.png
        :width: 60%

    **Technic Hub**

    .. figure:: ../../main/diagrams/orientation_technichub.png
        :width: 60%

    .. versionchanged:: 3.2

        Changed which side is the front.

    **Tilt Sensor**

    .. figure:: ../../main/diagrams/orientation_tiltsensor.png
        :width: 50%
