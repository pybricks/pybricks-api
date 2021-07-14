from micropython import const

# This value can be used here. Other files can import it too.
APPLES = const(123)

# These values can only be used within this file.
_ORANGES = const(1 << 8)
_BANANAS = const(789 + _ORANGES)

# You can read the constants as normal values. The compiler
# will just insert the numeric values for you.
fruit = APPLES + _ORANGES + _BANANAS
print(fruit)
