#Felipe Silva Ganho

import math


def polarToRetangular(c, o):
    a = c * math.cos(math.radians(o))
    b = c * math.sin(math.radians(o))
    return a, b


#teste
print(polarToRetangular(2.8284271247461903, 225.0))
print(polarToRetangular(2.8284271247461903, 45.0))
print(polarToRetangular(2.8284271247461903, 135.0))
print(polarToRetangular(2.8284271247461903, 315.0))

print("")

#teste extra
print(polarToRetangular(5, 36.87))
print(polarToRetangular(5, 143.13))
print(polarToRetangular(5, 216.87))
print(polarToRetangular(5, 323.13))


