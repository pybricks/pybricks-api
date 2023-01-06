#!/usr/bin/env python3
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

# This demo makes your PC talk to an EV3 over Bluetooth.
#
# This is identical to the EV3 server example in ../bluetooth_server
#
# The only difference is that it runs in Python3 on your computer, thanks to
# the Python3 implementation of the messaging module that is included here.
# As far as the EV3 is concerned, it thinks it just talks to an EV3 client.
#
# So, the EV3 client example needs no further modifications. The connection
# procedure is also the same as documented in the messaging module docs:
# https://docs.pybricks.com/en/latest/messaging.html

server = BluetoothMailboxServer()
mbox = TextMailbox("greeting", server)

# The server must be started before the client!
print("waiting for connection...")
server.wait_for_connection()
print("connected!")

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
print(mbox.read())
mbox.send("hello to you!")
