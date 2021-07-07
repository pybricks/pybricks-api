from pybricks.hubs import MoveHub
from pybricks.tools import wait

# Initialize the hub.
hub = MoveHub()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
