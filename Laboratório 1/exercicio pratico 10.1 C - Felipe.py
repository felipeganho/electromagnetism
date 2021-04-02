#Felipe Silva Ganho

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

k = 2/3
tam = (50 * pi)**(-1)

x = np.arange((-9) * pi, 9 * pi, tam)
H = 0.1 * np.cos(pi/4 - k * x)

#criando os graficos
fig, ax1 = plt.subplots(1, 1)

ax1.plot(x, H, 'r-', linewidth=2, label="Senoide Continua no tempo")
ax1.set_xlabel("Distância")
ax1.set_ylabel("Amplitude")
ax1.grid(True)
ax1.set_title('H = 0.1 cos(pi/4 - kx)')

fig.tight_layout()

plt.show()