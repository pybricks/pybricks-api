from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the motor.
train_motor = DCMotor(Port.A)

# Choose the "power" level for your train. Negative means reverse.
train_motor.dc(50)

# Keep doing nothing. The train just keeps going.
while True:
    wait(1000)
