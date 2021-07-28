from pybricks.pupdevices import Remote

try:
    # Search for a remote for 5 seconds.
    my_remote = Remote(timeout=5000)

    print("Connected!")

    # Here you can write code that uses the remote.

except OSError:

    print("Could not find the remote.")

    # Here you can make your robot do something
    # without the remote.
