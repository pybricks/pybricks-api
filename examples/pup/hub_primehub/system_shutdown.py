from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
