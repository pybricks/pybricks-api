# SPDX-License-Identifier: MIT
# Copyright (C) 2020,2023 The Pybricks Authors

"""
:class:`RFCOMMServer` can be used to communicate with other Bluetooth RFCOMM
devices that don't support the EV3 mailbox protocol.

It is based on the standard library ``socketserver`` module and attempts to
remain a strict subset of that implementation when it comes to low-level
implementation details.
"""

from socket import socket, AF_BLUETOOTH, BTPROTO_RFCOMM, SOCK_STREAM
from socketserver import ThreadingMixIn


class RFCOMMServer:
    """
    Object that simplifies setting up an RFCOMM socket server.

    This is based on the ``socketserver.SocketServer`` class in the Python
    standard library.
    """

    request_queue_size = 1

    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass

        self.socket = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)

        try:
            self.socket.bind(server_address)
            # self.server_address = self.socket.getsockname()
            self.socket.listen(self.request_queue_size)
        except Exception:
            self.server_close()
            raise

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.server_close()

    def handle_request(self):
        try:
            request, addr_data = self.socket.accept()
        except OSError:
            return

        try:
            self.process_request(request, addr_data)
        except Exception:
            request.close()
            raise

    def process_request(self, request, client_address):
        self.finish_request(request, client_address)
        request.close()

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self)

    def server_close(self):
        self.socket.close()


class ThreadingRFCOMMServer(ThreadingMixIn, RFCOMMServer):
    """
    Version of :class:`RFCOMMServer` that handles connections in a new thread.
    """

    daemon_threads = True


class RFCOMMClient:
    def __init__(self, client_address, RequestHandlerClass):
        self.client_address = client_address
        self.RequestHandlerClass = RequestHandlerClass
        self.socket = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)

    def handle_request(self):
        self.socket.connect(self.client_address)
        try:
            self.process_request(self.socket, self.client_address)
        except Exception:
            self.socket.close()
            raise

    def process_request(self, request, client_address):
        self.finish_request(request, client_address)
        request.close()

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self)

    def client_close(self):
        self.socket.close()


class ThreadingRFCOMMClient(ThreadingMixIn, RFCOMMClient):
    """
    Version of :class:`RFCOMMClient` that handles connections in a new thread.
    """

    daemon_threads = True
