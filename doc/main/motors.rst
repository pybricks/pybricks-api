More about Motors
===========================================

.. _control:

The Control Class
^^^^^^^^^^^^^^^^^

The ``Motor`` class uses PID control to accurately track your commanded target
angles. Similarly, the ``DriveBase`` class uses two of such controllers:
one to control the heading and one to control the traveled distance.

You can change the control settings through the following attributes, which are
instances of the ``Control`` class given below.:

    - ``Motor.control``
    - ``DriveBase.heading_control``
    - ``DriveBase.distance_control``

You can only change the settings while the controller is stopped. For example,
you can set the settings at the beginning of your program. Alternatively, first
call ``stop()`` to make your ``Motor`` or ``DriveBase`` stop, and then change
the settings.

.. autoclass:: pybricks._common.Control
    :no-members:

    .. rubric:: Status

    .. automethod:: pybricks._common.Control.done

    .. automethod:: pybricks._common.Control.stalled

    .. automethod:: pybricks._common.Control.load

    .. rubric:: Settings

    .. automethod:: pybricks._common.Control.limits

    .. automethod:: pybricks._common.Control.pid

    .. automethod:: pybricks._common.Control.target_tolerances

    .. automethod:: pybricks._common.Control.stall_tolerances
