from pybricks.hubs import MoveHub
from pybricks.tools import wait

# Initialize the hub.
hub = MoveHub()

# Get the acceleration tuple.
print(hub.imu.acceleration())

while True:
    # Get individual acceleration values.
    x, y, z = hub.imu.acceleration()
    print(x, y, z)

    # Wait so we can see what we printed.
    wait(100)
