# ExampleHub = TechnicHub PrimeHub
from pybricks.hubs import ExampleHub
from pybricks.tools import wait
from pybricks.geometry import Axis

# Initialize the hub.
hub = ExampleHub()

# Get the acceleration or angular_velocity along a single axis.
# If you need only one value, this is more memory efficient.
while True:

    # Read the forward acceleration.
    forward_acceleration = hub.imu.acceleration(Axis.X)

    # Read the yaw rate.
    yaw_rate = hub.imu.angular_velocity(Axis.Z)

    # Print the yaw rate.
    print(yaw_rate)
    wait(100)
