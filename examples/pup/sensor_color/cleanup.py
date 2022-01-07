from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorSensor(Port.A)


def main():
    # Run the main code.
    while True:
        print(sensor.color())
        wait(500)


# Wrap the main code in try/finally so that the cleanup code always runs
# when the program ends, even if an exception was raised.
try:
    main()
finally:
    # The cleanup code goes here.
    print("Cleaning up.")
    sensor.lights.off()
