from pybricks.hubs import TechnicHub
from pybricks.tools import wait

# Initialize the hub.
hub = TechnicHub()

# Get the acceleration vector.
print(hub.imu.acceleration())

# Get the angular velocity vector.
print(hub.imu.angular_velocity())

# Wait so we can see what we printed
wait(5000)
