from pybricks.hubs import MoveHub

# Initialize the hub.
hub = MoveHub()

# Initialize "random" seed.
_rand = hub.battery.voltage() + hub.battery.current()


# Return a random integer N such that a <= N <= b.
def randint(a, b):
    global _rand
    _rand = 75 * _rand % 65537  # Lehmer
    return _rand * (b - a + 1) // 65537 + a


# Generate a few example numbers.
for i in range(5):
    print(randint(0, 1000))
