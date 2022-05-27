from pybricks.pupdevices import Remote

# Connect to any remote.
my_remote = Remote()

# Print the current name of the remote.
print(my_remote.name())

# Choose a new name.
my_remote.name("truck2")

print("Done!")
