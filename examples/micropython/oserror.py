from pybricks.pupdevices import Motor
from pybricks.parameters import Port

from uerrno import ENODEV

try:
    # Try to initialize a motor.
    my_motor = Motor(Port.A)

    # If all goes well, you'll see this message.
    print("Detected a motor.")
except OSError as ex:
    # If an OSError was raised, we can check what
    # kind of error this was, like ENODEV.
    if ex.errno == ENODEV:
        # ENODEV is short for "Error, no device."
        print("There is no motor this port.")
    else:
        print("Another error occurred.")
