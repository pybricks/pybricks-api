from pybricks.tools import wait

print("Started!")

try:

    # Run your script here as you normally would. In this
    # example we just wait forever and do nothing.
    while True:
        wait(1000)

except SystemExit:
    # This code will run when you press the stop button.
    # This can be useful to "clean up", such as to move
    # the motors back to their starting positions.
    print("You pressed the stop button!")
