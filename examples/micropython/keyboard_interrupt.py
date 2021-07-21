from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the motor.
test_motor = Motor(Port.A)

# Start moving at 500 deg/s.
test_motor.run(500)

# If you click on the terminal window and press CTRL+C,
# you can continue debugging in this terminal.
wait(5000)

# You can also do this to exit the script and enter the
# terminal. Variables in the global scope are still available.
raise KeyboardInterrupt

# For example, you can copy the following line to the terminal
# to get the angle, because test_motor is still available.
test_motor.angle()
