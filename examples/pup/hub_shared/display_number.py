from pybricks.hubs import ExampleHub
from pybricks.tools import wait

# Initialize the hub.
hub = ExampleHub()

# Count from 0 to 99.
for i in range(100):
    hub.display.number(i)
    wait(200)
