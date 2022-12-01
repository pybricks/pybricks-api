.. pybricks-requirements:: stm32-extra

:mod:`uselect` -- Wait for events
=================================

.. automodule:: uselect
    :no-members:

    .. rubric:: Poll instance and class

    .. autofunction:: poll

    .. autoclass:: Poll
        :no-members:

        .. automethod:: register

        .. automethod:: unregister

        .. automethod:: modify

        .. automethod:: poll

        .. automethod:: ipoll

    .. rubric:: Event mask flags

    .. autodata:: POLLIN

    .. autodata:: POLLOUT

    .. autodata:: POLLERR

    .. autodata:: POLLHUP

Examples
---------------

See the `projects website`_ for a demo that uses this module.

.. _projects website: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/
