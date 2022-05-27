from pybricks.pupdevices import Remote
from pybricks.tools import wait

# Connect to a remote called truck2.
truck_remote = Remote("truck2", timeout=None)

print("Connected!")

wait(2000)
