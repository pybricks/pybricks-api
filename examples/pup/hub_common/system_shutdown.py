# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# Initialize the hub.
hub = ThisHub()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
