import numpy as np

#constantes do problema
a = (50)/1000
b = (45)/1000
f = (3*(10**9))
permissibilidadeRelativa = 9
permeabilidadeRelativa = 1
modosTE = []
modosTM = []

#velocidade de fase
def velocidadeFase(permissibilidadeRelativa, permeabilidadeRelativa):
    return (3*(10**8))/np.sqrt(permissibilidadeRelativa * permeabilidadeRelativa)

#frequencia de corte
def frequenciaCorte(a, b, m, n, velocidadeFase):
    return (velocidadeFase/2) * (np.sqrt(((m/a)**2) + ((n/b)**2)))

#procura os modos abaixo da frequencia f determinada
for i in range(0, 10):
    for j in range(0, 10):
        fc = frequenciaCorte(a, b, i, j, velocidadeFase(permissibilidadeRelativa, permeabilidadeRelativa))
        if(fc <= f):
            if(i==0 and j==0):
                continue
            else:
                if(i==0 or j==0):
                    modosTE.append([i, j, fc])

                else:
                    modosTE.append([i, j, fc])
                    modosTM.append([i, j, fc])

print("Quantidade de modos TE:", len(modosTE))
print("Modos TE:", modosTE)
print("\n")
print("Quantidade de modos TM:", len(modosTM))
print("Modos TM:", modosTM)
