# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# Initialize the hub.
hub = ThisHub()

while True:
    # Read the tilt values.
    pitch, roll = hub.imu.tilt()

    # Print the result.
    print(pitch, roll)
    wait(200)
