from pybricks.parameters import Port
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import wait

# Initialize the sensor.
sensor = UltrasonicSensor(Port.A)

# Turn on the upper lights.
sensor.lights.on([50, 50, 0, 0])


def main():
    while True:
        print("Main program is running.")
        wait(500)


# Wrap the main code in try/finally so that the cleanup code always runs
# when the program ends, even if an exception was raised.
try:
    main()
finally:
    # The cleanup code goes here.
    print("Cleaning up.")
    sensor.lights.off()
