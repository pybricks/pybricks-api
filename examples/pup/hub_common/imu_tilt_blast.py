# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait
from pybricks.parameters import Axis

# Initialize the hub. In this case, specify that the hub is mounted with the
# top side facing forward and the front side facing to the right.
# For example, this is how the hub is mounted in BLAST in the 51515 set.
hub = ThisHub(top_side=Axis.X, front_side=-Axis.Y)

while True:
    # Read the tilt values. Now, the values are 0 when BLAST stands upright.
    # Leaning forward gives positive pitch. Leaning right gives positive roll.
    pitch, roll = hub.imu.tilt()

    # Print the result.
    print(pitch, roll)
    wait(200)
