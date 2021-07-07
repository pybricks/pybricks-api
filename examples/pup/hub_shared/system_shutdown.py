# ExampleHub = MoveHub CityHub TechnicHub
from pybricks.hubs import ExampleHub
from pybricks.tools import wait

# Initialize the hub.
hub = ExampleHub()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
