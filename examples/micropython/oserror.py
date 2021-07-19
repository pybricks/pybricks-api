from pybricks.pupdevices import Motor
from pybricks.parameters import Port

from uerrno import ENODEV

try:
    my_motor = Motor(Port.A)
    print("Detected a motor.")
except OSError as ex:
    if ex.errno == ENODEV:
        print("There is no motor this port.")
