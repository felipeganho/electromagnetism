#Felipe Silva Ganho

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

#parametros da linha telefonica
R = 30/1000
L = (100/1000) * (10**(-3))
G = 0
C = (20/1000) * (10**(-6))

#frequencia
f = np.arange(500*(10**3), 1001*(10**3), 1*(10**3))

#impedancia caracteristica
Z0 = np.array([])
for i in f:
    Z0 = np.append(Z0, np.sqrt((complex(R, 2 * pi * i * L)) / (complex(G, 2 * pi * i * C))))

#modulo
moduloZ0 = np.sqrt(Z0.real**2 + Z0.imag**2)
#angulo
anguloZ0 = np.rad2deg(np.arctan2(Z0.imag, Z0.real))

#constante de propagacao
#parte real - constante de atenuacao
#parte imaginaria - constante de fase
constPropagacao = np.array([])
for i in f:
    constPropagacao = np.append(constPropagacao, np.sqrt((complex(R, 2 * pi * i * L))*(complex(G, 2 * pi * i * C))))

#velocidade de fase
velFase = np.array([])
j = 0
for i in f:
    velFase = np.append(velFase, (2 * pi * i)/(constPropagacao[j].imag))
    j += 1

#criando os graficos
fig, ax1 = plt.subplots(1, 1)
fig2, ax2 = plt.subplots(1, 1)
fig3, ax3 = plt.subplots(1, 1)
fig4, ax4 = plt.subplots(1, 1)
fig5, ax5 = plt.subplots(1, 1)

ax1.plot(f, moduloZ0, 'r-', linewidth=2)
ax1.set_xlabel("Frequência")
ax1.set_ylabel("|Z0|")
ax1.grid(True)
ax1.set_title('f x |Z0|')

ax2.plot(f, anguloZ0, 'r-', linewidth=2)
ax2.set_xlabel("Frequência")
ax2.set_ylabel("Ângulo Z0")
ax2.grid(True)
ax2.set_title('f x Ângulo Z0')

ax3.plot(f, constPropagacao.real, 'r-', linewidth=2)
ax3.set_xlabel("Frequência")
ax3.set_ylabel("Constante de Atenuação")
ax3.grid(True)
ax3.set_title('f x α')

ax4.plot(f, constPropagacao.imag, 'r-', linewidth=2)
ax4.set_xlabel("Frequência")
ax4.set_ylabel("Constante de fase")
ax4.grid(True)
ax4.set_title('f x β')

ax5.plot(f, velFase, 'r-', linewidth=2)
ax5.set_xlabel("Frequência")
ax5.set_ylabel("Velocidade de fase")
ax5.grid(True)
ax5.set_title('f x u')

fig.tight_layout()
fig2.tight_layout()
fig3.tight_layout()
fig4.tight_layout()
fig5.tight_layout()

plt.show()

