from pybricks.geometry import Axis
from pybricks.iodevices import PUPDevice
from pybricks.pupdevices import *
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait, StopWatch
from uerrno import ENODEV, ETIMEDOUT

# 1: Determine the type of hub
# -------------------------------------------------------------------
#   For Hubs with IMU: how is it mounted?
#   https://docs.pybricks.com/en/latest/geometry.html#fig-imuexamples
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
    try: # InventorHub is the same as PrimeHub, so treat the same.
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

    print("Hub:\n  Name:\t", hub.system.name(),":",hub_info['hub_type'])
    print("  Reset reason: ", hub.system.reset_reason())
    print("  voltage: ", hub.battery.voltage(), "mV")
    print("  current: ", hub.battery.current(), "mA")

    # Check for IMU and Matrix dislay:
    try: # to init IMU
        from pybricks.parameters import Side
        hub_info.update(init_position=hub.imu.up())
        print("  facing: ", hub_info['init_position'])
        hub_info.update(has_imu=True)
    except AttributeError:
        hub_info.update(has_imu=False)
        pass
    try: # to init Matrix
        from pybricks.parameters import Icon
        hub.display.icon(Icon.UP / 2)
        hub.display.orientation(up_side)
        print("  with display matrix.")
        hub_info.update(has_matrix=True)
    except ImportError or AttributeError:
        hub_info.update(has_matrix=False)
        pass

    return (hub, hub_info)

# 2: Diagnose connected devices
# -------------------------------------------------------------------
# Dictionary of device identifiers along with their name.
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

def ConnectToDevice(port):
    # Returns a device dict()
    device = {'type':None, 'id':None, 'name':None, 'object':None}

    try: # to get the device, if it is attached.
        pupdev = PUPDevice(port)
    except OSError as ex:
        if ex.args[0] == ENODEV:
            # No device found on this port.
            return device
        else:
            raise
    # Get the device id
    temp_info = pupdev.info()
    device['id'] = temp_info["id"]
    try: # to look up the name.
        device['name'] = device_names[device['id']]
    except KeyError:
        device['name'] = "Unknown"
        #print(port, ":", "Unknown device with ID", xid)
    if len(temp_info) > 1:
        print(temp_info)

    # Initiate object and type
    xid = device['id']
    if xid in (1,2):
        try:
            device['object'] = DCMotor(port)
            device['type'] = "DCMotor"
        except OSError as err:
            print("DCMotor could not be initiated: ", err)
            device['type'] = "Custom"
            pass
    elif xid in (46,47,48,49,75,76):
        try:
            device['object'] = Motor(port, positive_direction=Direction.CLOCKWISE, gears=None)
            device['type'] = "Motor"
        except:
            print("Motor could not be initiated: ", err)
            device['type'] = "Custom"
            pass
    elif xid is 8:
        try:
            device['object'] = Light(port)
            device['object'].on(brightness=50)
            device['type'] = "Light"
        except:
            print("Light could not be initiated: ", err)
            device['type'] = "Custom"
            pass
    elif xid is None: #ToDo
        try:
            device['object'] = ColorLightMatrix(port)
            device['type'] = "Matrix3x3"
        except:
            print("Matrix could not be initiated: ", err)
            device['type'] = "Custom"
            pass
    elif xid in (34,35,37,61,62,63):
        device['type'] = "Sensor"
        if xid is 34:
            try:
                device['object'] = TiltSensor(port)
                device['type'] += "/Tilt"
            except:
                print("TiltSensor could not be initiated: ", err)
                device['type'] += "/Custom"
                pass
        elif xid is 35:
            try:
                device['object'] = InfraredSensor(port)
                device['type'] += "/IR/Distance"
            except:
                print("InfraredSensor could not be initiated: ", err)
                device['type'] += "/Custom"
                pass
        elif xid is 37:
            try:
                device['object'] = ColorDistanceSensor(port)
                device['type'] += "/Distance/Color/Light"
            except:
                print("ColorDistanceSensor could not be initiated: ", err)
                device['type'] += "/Custom"
                pass
        elif xid is 61:
            try:
                device['object'] = ColorSensor(port)
                device['type'] += "/Color/Light"
            except:
                print("ColorSensor could not be initiated: ", err)
                device['type'] += "/Custom"
                pass
        elif xid is 62:
            try:
                device['object'] = UltrasonicSensor(port)
                device['type'] += "/Distance/Light"
            except:
                print("UltrasonicSensor could not be initiated: ", err)
                device['type'] += "/Custom"
                pass
        elif xid is 63:
            try:
                device['object'] = ForceSensor(port)
                device['type'] += "/Force/Distance/Press"
            except:
                print("ForceSensor could not be initiated: ", err)
                device['type'] += "/Custom"
                pass
    else:
        pass

    return device

# end of ConnectToDevice(port)
# -------------------------------------------------------------------
 
# Make a list of known ports.
ports = [Port.A, Port.B]
try: # to add more ports, on hubs that support it.
    ports.append(Port.C)
    ports.append(Port.D)
except AttributeError:
    pass
try: # to add more ports, on hubs that support it.
    ports.append(Port.E)
    ports.append(Port.F)
except AttributeError:
    pass

# 3: Remote buttons check and remote init
# -------------------------------------------------------------------
remote = None
ch1_val = 0 # +/-100%, scale if needed
ch2_val = 0 # +100%, scale if needed

def ConnectRemote():
    global remote
    try:
        remote = Remote(name=None,timeout=10000)
        print("Remote: " + remote.name())
        #remote.name("Remote of <user>")
    except OSError as ex:
        if ex.errno == ETIMEDOUT:
            print("No Remote found.")

def ServiceRemote():
    global remote

    if remote is None:
        return (ch1_val,ch2_val)
    try:
        pressed = remote.buttons.pressed()
    except OSError as ex:
        if not ex.errno == ENODEV:
            raise
        print("Lost remote")
        remote = None # empty handle
        return (ch1_val,ch2_val)
    if len(pressed) is 0:
        return (ch1_val,ch2_val)
    #print(pressed)

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

    return (ch1_val_new,ch2_val_new)


# 4: Main / Monitor changes
# -------------------------------------------------------------------
DIAGNOSTICS_PERIOD = 5000 # 5s
sys_tick = StopWatch()
(hub,hub_info) = HubInit()
print(hub_info)
pressed = ()

# Readings
tilt = None
distance = None
color = None
force = None

# Search through all available ports.
devices = []
for port in ports:
    dev = ConnectToDevice(port)
    if dev['type'] is None:
        print(port, ": ---")
    else:
        print(port,dev['id'],":",dev['name'],":",dev['type'])
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

    if sys_tick.time() % DIAGNOSTICS_PERIOD:
        print("Hub voltage: ", hub.battery.voltage(), "mV")
        print("Hub current: ", hub.battery.current(), "mA")
        for device in devices:
            if "Tilt" in device['type']:
                tilt = device['object'].tilt()
            if "Distance" in device['type']:
                distance = device['object'].distance()
            if "Color" in device['type']:
                color = device['object'].color()
            if "Force" in device['type']:
                force = device['object'].force()
        print("T:",tilt,"D:",distance,"C:",color,"F:",force)		
    
    # do not set values blindly to not interfere with other code:
    (ch1_val_new,ch2_val_new) = ServiceRemote()
    if ch1_val_new is not ch1_val:
        ch1_val = ch1_val_new
        print("Channel 1 changed:",ch1_val)
    if ch2_val_new is not ch2_val:
        ch2_val = ch2_val_new
        print("Channel 2 changed:",ch2_val)