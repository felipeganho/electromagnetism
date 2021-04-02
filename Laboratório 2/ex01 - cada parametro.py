#Felipe Silva Ganho

import numpy as np
from numpy import pi

#funcoes para R, L, G e C da LINHA COAXIAL
def resistenciaCoaxial(profundidaPelicular, condutividade, raioA, raioB):
    return (1/(2 * pi * profundidaPelicular * condutividade)) * ((1/raioA) + (1/raioB))

def indutanciaCoaxial(permeabilidade, raioA, raioB):
    return ((permeabilidade/(2 * pi)) * (np.log(raioA/raioB)))

def condutanciaCoaxial(condutividade, raioA, raioB):
    return ((2 * pi * condutividade) / (np.log(raioB/raioA)))

def capacitanciaCoaxial(permissibilidade, raioA, raioB):
    return ((2 * pi * permissibilidade) / (np.log(raioB/raioA)))

#funcoes para R, L, G e C da LINHA BIFILAR
def resistenciaBifilar(raioA, profundidaPelicular, condutividade):
    return (1/(pi * raioA * profundidaPelicular * condutividade))

def indutanciaBifilar(permeabilidade, distancia, raioA):
    return ((permeabilidade/pi) * (np.arccosh((distancia/(2 * raioA)))))

def condutanciaBifilar(condutividade, distancia, raioA):
    return ((pi * condutividade) / (np.arccosh((distancia/(2 * raioA)))))

def capacitanciaBifilar(permissibilidade, distancia, raioA):
    return ((pi * permissibilidade) / (np.arccosh((distancia/(2 * raioA)))))

#funcoes para R, L, G e C da LINHA PLANAR
def resistenciaPlanar(largura, profundidaPelicular, condutividade):
    return (2/(largura * profundidaPelicular * condutividade))

def indutanciaPlanar(permeabilidade, distancia, largura):
    return ((permeabilidade * distancia) / largura)

def condutanciaPlanar(condutividade, largura, distancia):
    return ((condutividade * largura) / distancia)

def capacitanciaPlanar(permissibilidade, largura, distancia):
    return ((permissibilidade * largura) / distancia)