from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorSensor, UltrasonicSensor

# Initialize the hub
hub = PrimeHub()

# Initialize the sensors
ultrasonic_sensor = UltrasonicSensor(Port.E)
color_sensor = ColorSensor(Port.F)

# Turn on upper halves
ultrasonic_sensor.lights.on([50, 50, 0, 0])


# Your robot's code goes here
def main():
    while True:
        color = color_sensor.color()
        if color == Color.RED:
            hub.display.text("R")
        else:
            hub.display.text("?")


# Wrap the code in try-finally to ensure the cleanup code is always executed
# no matter if the program gets stopped gracefully by the user or by an error
try:
    main()
finally:
    # The cleanup code goes here
    color_sensor.lights.off()
    ultrasonic_sensor.lights.off()
