#Felipe Silva Ganho

import numpy as np
from numpy import pi

#funcao para LINHA COAXIAL
def ltCoaxial(profundidadePelicular, condutividade, raioA, raioB, permeabilidade, permissibilidade):
    R = (1/(2 * pi * profundidadePelicular * condutividade)) * ((1/raioA) + (1/raioB))
    L = ((permeabilidade/(2 * pi)) * (np.log(raioA/raioB)))
    G = ((2 * pi * condutividade) / (np.log(raioB/raioA)))
    C = ((2 * pi * permissibilidade) / (np.log(raioB/raioA)))
    return R, L, G, C

#funcao para LINHA BIFILAR
def ltBifilar(raioA, profundidadePelicular, condutividade, permeabilidade, distancia, permissibilidade):
    R = (1/(pi * raioA * profundidadePelicular * condutividade))
    L = ((permeabilidade/pi) * (np.arccosh((distancia/(2 * raioA)))))
    G = ((pi * condutividade) / (np.arccosh((distancia/(2 * raioA)))))
    C = ((pi * permissibilidade) / (np.arccosh((distancia/(2 * raioA)))))
    return R, L, G, C

#funcao para LINHA PLANAR
def ltPlanar(largura, profundidadePelicular, condutividade, permeabilidade, distancia, permissibilidade):
    R = (2/(largura * profundidadePelicular * condutividade))
    L = ((permeabilidade * distancia) / largura)
    G = ((condutividade * largura) / distancia)
    C = ((permissibilidade * largura) / distancia)
    return R, L, G, C
