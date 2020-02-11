:mod:`ev3messaging <pybricks.ev3messaging>` -- EV3 Messaging
============================================================

.. automodule:: pybricks.ev3messaging
    :no-members:

.. currentmodule:: pybricks.ev3messaging

Introductory text. An example network is shown in :numref:`fig_ev3messaging`.

.. _fig_ev3messaging:

.. figure:: images/ev3messaging_label.png
   :width: 90 %
   :alt: ev3messaging
   :align: center

   An example network with one server and two clients.


Connections
------------

.. autoclass:: BluetoothMailboxServer

.. autoclass:: BluetoothMailboxClient

Mailboxes
---------

Mailboxes are used to send data to and from other EV3s.

.. autoclass:: Mailbox

.. autoclass:: LogicMailbox
    :no-members:

.. autoclass:: NumericMailbox
    :no-members:

.. autoclass:: TextMailbox
    :no-members:

