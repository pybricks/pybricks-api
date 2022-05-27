from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Display the letter A for two seconds.
hub.display.char("A")
wait(2000)

# Display text, one letter at a time.
hub.display.text("Hello, world!")
