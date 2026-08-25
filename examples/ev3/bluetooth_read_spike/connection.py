from _thread import start_new_thread

from pybricks.bluetooth import AF_BLUETOOTH, BTPROTO_RFCOMM, sockaddr_rc, str2ba
from uctypes import addressof, sizeof, struct
from usocket import SOCK_STREAM, socket

from pybricks.tools import StopWatch, wait


def get_bluetooth_rfcomm_socket(address, channel):
    addr_data = bytearray(sizeof(sockaddr_rc))
    addr = struct(addressof(addr_data), sockaddr_rc)
    addr.rc_family = AF_BLUETOOTH
    str2ba(address, addr.rc_bdaddr)
    addr.rc_channel = channel

    sock = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)
    sock.connect(addr_data)
    return sock


class SpikePrimeStreamReader:
    def __init__(self, address):

        try:
            self.sock = get_bluetooth_rfcomm_socket(address, 1)
        except OSError:
            print("Turn on Bluetooth on the EV3 and on SPIKE.")
            raise

        self._values = None

        start_new_thread(self.reader, ())

        watch = StopWatch()
        while watch.time() < 2000:
            if self.values() is not None:
                return
            wait(100)
        raise OSError("No data received")

    def disconnect(self):
        self.sock.close()

    def reader(self):
        while True:
            try:
                raw = self.sock.recv(1024)
            except OSError:
                break
            try:
                data = eval(raw)
                if data["m"] == 0:
                    self._values = data["p"]
            except (SyntaxError, KeyError):
                pass

    def values(self):
        return self._values

    def device(self, port):
        if "A" <= port <= "F":
            return self.values()[ord(port) - ord("A")][1]
        else:
            raise ValueError

    def acceleration(self):
        return self.values()[6]

    def gyro(self):
        return self.values()[7]

    def orientation(self):
        return self.values()[8]
