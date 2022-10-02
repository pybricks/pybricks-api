.. pybricks-requirements:: stm32-float

:mod:`geometry <pybricks.geometry>` -- Geometry and algebra
============================================================

.. module:: pybricks.geometry

.. autoclass:: pybricks.geometry.Matrix
    :no-members:

    .. autoattribute:: pybricks.geometry::Matrix.T

    .. autoattribute:: pybricks.geometry::Matrix.shape

.. autofunction:: pybricks.geometry.vector

.. autoclass:: pybricks.geometry.Axis
    :no-members:

.. _robotframe:

Reference frames
-----------------------

The Pybricks module and this documentation use the following conventions:

- X: Positive means forward. Negative means backward.
- Y: Positive means to the left. Negative means to the right.
- Z: Positive means upward. Negative means downward.

To make sure that all hub measurements (such as acceleration) have the correct
value and sign, you can specify how the hub is mounted in your creation. This
adjust the measurements so that it is easy to see how your *robot* is moving,
rather than how the *hub* is moving.

For example, the hub may be mounted upside down in your design. If you
configure the settings as shown in :numref:`fig_imuexamples`, the hub
measurements will be adjusted accordingly. This way, a positive acceleration
value in the X direction means that your *robot* accelerates forward, even
though the *hub* accelerates backward.

.. _fig_imuexamples:

.. figure:: ../main/diagrams/imuexamples.png
   :width: 100 %

   How to configure the ``top_side`` and ``front_side`` settings for three
   different robot designs. The same technique can be applied to other hubs
   and other creations, by noting which way the top and
   front :class:`Side <Side>` of the hub are pointing. The example
   on the left is the default configuration.
