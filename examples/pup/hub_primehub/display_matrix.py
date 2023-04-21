from pybricks.hubs import PrimeHub
from pybricks.tools import wait, Matrix

# Initialize the hub.
hub = PrimeHub()

# Make a square that is bright on the outside and faint in the middle.
SQUARE = Matrix(
    [
        [100, 100, 100, 100, 100],
        [100, 50, 50, 50, 100],
        [100, 50, 0, 50, 100],
        [100, 50, 50, 50, 100],
        [100, 100, 100, 100, 100],
    ]
)

# Display the square.
hub.display.icon(SQUARE)
wait(3000)

# Make an image using a Python list comprehension. In this image, the
# brightness of each pixel is the sum of the row and column index. So the
# light is faint in the top left and bright in the bottom right.
GRADIENT = Matrix([[(r + c) for c in range(5)] for r in range(5)]) * 12.5

# Display the generated gradient.
hub.display.icon(GRADIENT)
wait(3000)
