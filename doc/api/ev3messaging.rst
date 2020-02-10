:mod:`ev3messaging <pybricks.ev3messaging>` -- EV3 Messaging
============================================================

.. automodule:: pybricks.ev3messaging
    :no-members:

.. currentmodule:: pybricks.ev3messaging


Mailboxes
---------

Mailboxes are used to send data to and from other EV3s.

.. autoclass:: LogicMailbox
    :no-members:

    .. automethod:: read
    .. automethod:: send
    .. automethod:: wait
    .. automethod:: wait_new

.. autoclass:: NumericMailbox
    :no-members:

    .. automethod:: read
    .. automethod:: send
    .. automethod:: wait
    .. automethod:: wait_new

.. autoclass:: TextMailbox
    :no-members:

    .. automethod:: read
    .. automethod:: send
    .. automethod:: wait
    .. automethod:: wait_new

.. autoclass:: Mailbox

.. autoclass:: BluetoothMailboxServer

.. autoclass:: BluetoothMailboxClient
