from pybricks.hubs import EssentialHub
from pybricks.tools import wait

# Initialize the hub.
hub = EssentialHub()

# Get the acceleration vector in g's.
print(hub.imu.acceleration() / 9810)

# Get the angular velocity vector.
print(hub.imu.angular_velocity())

# Wait so we can see what we printed
wait(5000)
