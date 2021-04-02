#Felipe Silva Ganho

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

beta = 1/3
tam = (50 * pi)**(-1)

x = np.arange((-9) * pi, 9 * pi, tam)
E1 = 50 * np.cos(beta * x)
#E2 = - 50 * np.sin(beta * x)
E2 = 50 * np.cos(pi/2 + beta * x)
#E3 = - 50 * np.cos(beta * x)
E3 = 50 * np.cos(pi + beta * x)

#criando os graficos
fig, ax1 = plt.subplots(3, 1)

ax1[0].plot(x, E1, 'r-', linewidth=2, label="Senoide Continua no tempo")
ax1[0].set_xlabel("Distância")
ax1[0].set_ylabel("Amplitude")
ax1[0].grid(True)
ax1[0].set_title('Ey = 50 cos(Bx)')

ax1[1].plot(x, E2, 'r-', linewidth=2, label="Senoide Continua no tempo")
ax1[1].set_xlabel("Distância")
ax1[1].set_ylabel("Amplitude")
ax1[1].grid(True)
ax1[1].set_title('Ey = - 50 sen(Bx)')

ax1[2].plot(x, E3, 'r-', linewidth=2, label="Senoide Continua no tempo")
ax1[2].set_xlabel("Distância")
ax1[2].set_ylabel("Amplitude")
ax1[2].grid(True)
ax1[2].set_title('Ey = - 50 cos(Bx)')

fig.tight_layout()

plt.show()
