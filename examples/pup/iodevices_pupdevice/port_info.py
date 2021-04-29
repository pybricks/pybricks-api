from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port

# Dictionary of device identifiers along with their name.
device_names = {
    34: "Wedo 2.0 Tilt Sensor",
    35: "Wedo 2.0 Infrared Sensor",
    37: "BOOST Color Distance Sensor",
    38: "BOOST Interactive Motor",
    46: "Technic Large Motor",
    47: "Technic Extra Large Motor",
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    61: "SPIKE Color Sensor",
    62: "SPIKE Ultrasonic Sensor",
    63: "SPIKE Force Sensor",
    75: "Technic Medium Angular Motor",
    76: "Technic Large Angular Motor",
}

# Make a list of known ports.
ports = [Port.A, Port.B]

# On hubs that support it, add more ports.
try:
    ports.append(Port.C)
    ports.append(Port.D)
except AttributeError:
    pass

# On hubs that support it, add more ports.
try:
    ports.append(Port.E)
    ports.append(Port.F)
except AttributeError:
    pass

# Go through all available ports.
for port in ports:

    # Try to get the device, if it is attached.
    try:
        device = PUPDevice(port)
    except OSError:
        # No device found on this port.
        print(port, ": ---")
        continue

    # Get the device id
    id = device.info()['id']

    # Look up the name.
    try:
        print(port, ":", device_names[id])
    except KeyError:
        print(port, ":", "Unknown device with ID", id)
