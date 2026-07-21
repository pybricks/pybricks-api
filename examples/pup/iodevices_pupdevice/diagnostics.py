from pybricks.geometry import Axis
from pybricks.iodevices import PUPDevice
from pybricks.pupdevices import DCMotor, Motor, Light, ColorLightMatrix, Remote, TiltSensor, InfraredSensor, ColorDistanceSensor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Port, Button, Color, Direction  # if needed: Side
from pybricks.tools import wait, StopWatch
from uerrno import ENODEV, ETIMEDOUT
from micropython import const

# 1: Determine the type of hub
# -------------------------------------------------------------------
#  How is hub with IMU mounted: https://docs.pybricks.com/en/latest/geometry.html#fig-imuexamples


def HubInit(mounted_top=Axis.Z, mounted_front=Axis.X):
    # Returns (str hub_object, dict hub_info)
    hub = None
    hub_info = dict()
    try:
        from pybricks.hubs import MoveHub
        hub = MoveHub()
        hub_info.update(hub_type="MoveHub")
    except ImportError:
        pass
    try:
        from pybricks.hubs import CityHub
        hub = CityHub()
        hub_info.update(hub_type="CityHub")
    except ImportError:
        pass
    try:
        from pybricks.hubs import TechnicHub
        hub = TechnicHub(top_side=mounted_top, front_side=mounted_front)
        hub_info.update(hub_type="TechnicHub")
    except ImportError:
        pass
    try:  # InventorHub is the same as PrimeHub, so treat the same.
        from pybricks.hubs import PrimeHub
        hub = PrimeHub(top_side=mounted_top, front_side=mounted_front)
        hub_info.update(hub_type="PrimeHub")
    except ImportError:
        pass
    try:
        from pybricks.hubs import EssentialHub
        hub = EssentialHub(top_side=mounted_top, front_side=mounted_front)
        hub_info.update(hub_type="EssentialHub")
    except ImportError:
        pass

    if hub is None:
        raise Exception("No valid Hub found")

    print("Hub:\n  Name:\t", hub.system.name(), ":", hub_info['hub_type'])
    print("  Reset reason: ", hub.system.reset_reason())
    print("  voltage: ", hub.battery.voltage(), "mV")
    print("  current: ", hub.battery.current(), "mA")

    # Check for IMU and Matrix dislay:
    try:  # to init IMU
        hub_info.update(init_position=hub.imu.up())
        print("  facing: ", hub_info['init_position'])
        hub_info.update(has_imu=True)
    except AttributeError:
        hub_info.update(has_imu=False)
        pass
    try:  # to init Matrix
        from pybricks.parameters import Icon
        hub.display.icon(Icon.UP / 2)
        hub.display.orientation(hub_info['init_position'])
        print("  with display matrix.")
        hub_info.update(has_matrix=True)
    except ImportError or AttributeError:
        hub_info.update(has_matrix=False)
        pass

    return (hub, hub_info)


# 2: Diagnose connected devices
# -------------------------------------------------------------------
# Dictionary of device identifiers along with their name.
# Also check https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#io-device-type-ids
device_names = {
    # pybricks.pupdevices.DCMotor
    1: "Wedo 2.0 Medium Motor",
    2: "Powered Up Train Motor",
    # pybricks.pupdevices.Light
    8: "Powered Up Light",
    # pybricks.pupdevices.Motor
    38: "BOOST Interactive Motor",
    46: "Technic Large Motor",
    47: "Technic Extra Large Motor",
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    65: "SPIKE Small Angular Motor",
    75: "Technic Medium Angular Motor",
    76: "Technic Large Angular Motor",
    # pybricks.pupdevices.TiltSensor
    34: "Wedo 2.0 Tilt Sensor",
    # pybricks.pupdevices.InfraredSensor
    35: "Wedo 2.0 Infrared Motion Sensor",
    # pybricks.pupdevices.ColorDistanceSensor
    37: "BOOST Color Distance Sensor",
    # pybricks.pupdevices.ColorSensor
    61: "SPIKE Color Sensor",
    # pybricks.pupdevices.UltrasonicSensor
    62: "SPIKE Ultrasonic Sensor",
    # pybricks.pupdevices.ForceSensor
    63: "SPIKE Force Sensor",
    # pybricks.pupdevices.ColorLightMatrix
    64: "SPIKE 3x3 Color Light Matrix",
}


def GetPorts():
    ports = [Port.A, Port.B]
    try:  # to add more ports, on hubs that support it.
        ports.append(Port.C)
        ports.append(Port.D)
    except AttributeError:
        pass
    try:  # to add more ports, on hubs that support it.
        ports.append(Port.E)
        ports.append(Port.F)
    except AttributeError:
        pass
    return ports


def ConnectToDevice(port):
    # Returns a device dict()
    device = {'type': None, 'id': None, 'name': None, 'object': None}

    try:  # to get the device, if it is attached.
        pupdev = PUPDevice(port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # No device found on this port.
            return device
        raise

    # Get the device id
    temp_info = pupdev.info()
    device['id'] = temp_info["id"]
    try:  # to look up the name.
        device['name'] = device_names[device['id']]
    except KeyError:
        device['name'] = "Unknown"
    if len(temp_info) > 1:
        print(temp_info)

    # Initiate object and type
    xid = device['id']
    device['type'] = ""  # Make it work with += "/Custom" in except
    try:
        if xid in (1, 2):
            dev_class = "DCMotor"
            device['object'] = DCMotor(port)
            device['type'] = "DCMotor"
        elif xid in (38, 46, 47, 48, 49, 65, 75, 76):
            dev_class = "Motor"
            device['object'] = Motor(port, positive_direction=Direction.CLOCKWISE, gears=None)
            device['type'] = "Motor"
        elif xid == 8:
            dev_class = "Light"
            device['object'] = Light(port)
            device['object'].on(brightness=50)
            device['type'] = "Light"
        elif xid == 64:
            dev_class = "ColorLightMatrix"
            device['object'] = ColorLightMatrix(port)
            device['object'].on([Color.RED, Color.GREEN, Color.BLUE])
            device['type'] = "Matrix3x3"
        elif xid in (34, 35, 37, 61, 62, 63):
            device['type'] = "Sensor"
            if xid == 34:
                dev_class = "TiltSensor"
                device['object'] = TiltSensor(port)
                device['type'] += "/Tilt"
            elif xid == 35:
                dev_class = "InfraredSensor"
                device['object'] = InfraredSensor(port)
                device['type'] += "/IR/Distance"
            elif xid == 37:
                dev_class = "ColorDistanceSensor"
                device['object'] = ColorDistanceSensor(port)
                device['type'] += "/Distance/Color/Light"
            elif xid == 61:
                dev_class = "ColorSensor"
                device['object'] = ColorSensor(port)
                device['type'] += "/Color/Light"
            elif xid == 62:
                dev_class = "UltrasonicSensor"
                device['object'] = UltrasonicSensor(port)
                device['type'] += "/Distance/Light"
            elif xid == 63:
                dev_class = "ForceSensor"
                device['object'] = ForceSensor(port)
                device['type'] += "/Force/Distance/Press"
            else:
                print("Not able to translate id:", xid, "to a class!")
    except OSError as err:
        print("class", dev_class, "could not be initiated: ", err)
        device['type'] += "/Custom"
        pass

    return device
# end of ConnectToDevice(port)
# -------------------------------------------------------------------


# 3: Remote buttons check and remote init
# -------------------------------------------------------------------
remote = None
ch1_val = 0  # +/-100%, scale if needed
ch2_val = 0  # +100%, scale if needed


def ConnectRemote():
    global remote
    try:
        remote = Remote(name=None, timeout=10000)
        print("Remote: " + remote.name())
        # remote.name("Remote of <user>")
    except OSError as ex:
        if ex.errno == ETIMEDOUT:
            print("No Remote found.")


def ServiceRemote():
    global remote

    if remote is None:
        return (ch1_val, ch2_val)
    try:
        pressed = remote.buttons.pressed()
    except OSError as ex:
        if not ex.errno == ENODEV:
            raise
        print("Lost remote")
        remote = None  # empty handle
        return (ch1_val, ch2_val)
    if len(pressed) == 0:
        return (ch1_val, ch2_val)
    # print(pressed)

    ch1_val_new = ch1_val
    ch2_val_new = ch2_val

    # Remote channel 1:
    if Button.LEFT_PLUS in pressed:
        ch1_val_new += 10
        if ch1_val_new > 100:
            ch1_val_new = 100
    if Button.LEFT_MINUS in pressed:
        ch1_val_new -= 10
        if ch1_val_new < -100:
            ch1_val_new = -100
    if Button.LEFT in pressed:
        ch1_val_new = 0
    # Remote channel 2:
    if Button.RIGHT_PLUS in pressed:
        ch2_val_new += 10
        if ch2_val_new > 100:
            ch2_val_new = 100
    if Button.RIGHT_MINUS in pressed:
        ch2_val_new -= 10
        if ch2_val_new < 0:
            ch2_val_new = 0
    if Button.RIGHT in pressed:
        ch2_val_new = 0

    return (ch1_val_new, ch2_val_new)


# 4: Main loop: Monitor changes
# -------------------------------------------------------------------
DIAGNOSTICS_PERIOD = const(2000)  # 5s
sys_tick = StopWatch()
last_diag = sys_tick.time()
(hub, hub_info) = HubInit()
print(hub_info)
pressed = ()

# Readings
tilt = None
distance = None
color = None
force = None
imu_tilt = None

# Search through all available ports.
ports = GetPorts()
devices = []
for port in ports:
    dev = ConnectToDevice(port)
    if dev['type'] is None:
        print(port, ": ---")
    else:
        print(port, dev['id'], ":", dev['name'], ":", dev['type'])
        devices.append(dev)

ConnectRemote()

while True:
    wait(100)
    try:
        pressed = hub.buttons.pressed()
    except AttributeError:
        pass
    try:
        pressed = hub.button.pressed()
    except AttributeError:
        pass
    if len(pressed) != 0:
        print("Hub button(s) pressed:", pressed)
    if (sys_tick.time() - last_diag) > DIAGNOSTICS_PERIOD:
        last_diag = sys_tick.time()
        print("Hub voltage: ", hub.battery.voltage(), "mV")
        print("Hub current: ", hub.battery.current(), "mA")
        if hub_info['has_imu'] is True:
            imu_tilt = hub.imu.tilt()
        for device in devices:
            if "Motor" in device['type']:  # also catches DCMotor
                device['object'].dc(ch1_val)
            if "Tilt" in device['type']:
                tilt = device['object'].tilt()
            if "Distance" in device['type']:
                distance = device['object'].distance()
            if "Color" in device['type']:
                color = device['object'].color()
            if "Force" in device['type']:
                force = device['object'].force()
        print("D:", distance, "C:", color, "F:", force, "T:", tilt, "IMU.T:", imu_tilt)

    # do not set values blindly to not interfere with other code:
    (ch1_val_new, ch2_val_new) = ServiceRemote()
    if ch1_val_new is not ch1_val:
        ch1_val = ch1_val_new
        print("Channel 1 changed:", ch1_val)
    if ch2_val_new is not ch2_val:
        ch2_val = ch2_val_new
        print("Channel 2 changed:", ch2_val)
