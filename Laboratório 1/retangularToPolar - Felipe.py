#Felipe Silva Ganho

import numpy as np


def retangularToPolar(a, b):
    c = np.sqrt(a ** 2 + b ** 2)
    o = np.degrees(np.arctan2(b, a))
    if o < 0:
        o += 360
    return c, o


# teste slide
print(retangularToPolar(-2, -2))
print(retangularToPolar(+2, +2))
print(retangularToPolar(-2, +2))
print(retangularToPolar(+2, -2))

print("")

# teste extra
print(retangularToPolar(4, 3))
print(retangularToPolar(-4, +3))
print(retangularToPolar(-4, -3))
print(retangularToPolar(+4, -3))
