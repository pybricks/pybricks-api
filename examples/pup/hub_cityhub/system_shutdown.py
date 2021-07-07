from pybricks.hubs import CityHub
from pybricks.tools import wait

# Initialize the hub.
hub = CityHub()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
