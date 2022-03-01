from pybricks.hubs import EssentialHub
from pybricks.tools import wait

# Initialize the hub.
hub = EssentialHub()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
