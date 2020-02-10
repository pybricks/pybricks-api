EV3 Mailboxes
=============

TODO: introduction... messages are sent immediately, received messages are held
in mailbox for getting later.

.. rubric:: Pairing

Before two EV3s can communicate with each other via Bluetooth, they must be
paired.

TODO: screenshots of pairing with brickman, don't press the connect button!


.. rubric:: Client and server

Programs can be written using either an EV3 mailbox *client* object or an EV3
mailbox *server* object.

The only difference between the *client* and the *server* is which one
initiates the connection at the beginning of the program. After that, sending
and receiving messages is bidirectional and works the same from either point of
view.

The *server* waits for an incoming connection while the *client* initiates the
connection. Therefore, the server program must always be started first. If not,
both programs will wait forever for a connection.


Here is a basic example where two EV3s are connected and send greetings to
each other.

.. rubric:: Client program

.. literalinclude::
    ../../pybricks-projects/snippets/ev3/bluetooth_client/client.py

.. rubric:: Server program

.. literalinclude::
    ../../pybricks-projects/snippets/ev3/bluetooth_server/server.py


.. rubric:: EV3-G compatibility

TODO: screenshots of EV3-G programs, difference between client and server
program is that client program has connect block. Server is always running.

TODO: show equivalent blocks

- :class:`pybricks.ev3messaging.LogicMailbox`
- :class:`pybricks.ev3messaging.NumericMailbox`
- :class:`pybricks.ev3messaging.TextMailbox`


.. rubric:: More than two bricks

A single client EV3 can connect to multiple server EV3s or a single server EV3
can accept connections from multiple clients.

TODO: the actual implementation needs to be updated to match this example.

Example::

    client = EV3MailboxClient()

    # connect to 4 different servers
    client.connect(SERVER1)
    client.connect(SERVER2)
    client.connect(SERVER3)
    client.connect(SERVER4)


Example::

    server = EV3MailboxServer()

    # wait for 4 clients to connect
    server.wait_for_connection(4)
