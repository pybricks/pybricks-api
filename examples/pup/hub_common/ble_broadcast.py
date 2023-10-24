# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the hub.
hub = ThisHub(broadcast_channel=1)

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

while True:
    # Read the motor angles to be sent to the other hub.
    left_angle = left_motor.angle()
    right_angle = right_motor.angle()

    # Set the broadcast data and start broadcasting if not already doing so.
    data = (left_angle, right_angle)
    hub.ble.broadcast(data)

    # Broadcasts are only sent every 100 milliseconds, so there is no reason
    # to call the broadcast() method more often than that.
    wait(100)
