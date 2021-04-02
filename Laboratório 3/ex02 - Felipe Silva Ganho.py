import numpy as np

#constantes do problema
a = (90)/1000
b = (70)/1000
c = (120)/1000
permissibilidadeRelativa = 3
permeabilidadeRelativa = 1
modos = []

#velocidade de fase
def velocidadeFase(permissibilidadeRelativa, permeabilidadeRelativa):
    return (3*(10**8))/np.sqrt(permissibilidadeRelativa * permeabilidadeRelativa)

#frequencia de ressonancia
def frequenciaRessonancia(a, b, m, n, p, velocidadeFase):
    return (velocidadeFase/2) * (np.sqrt(((m/a)**2) + ((n/b)**2) + ((p/c)**2)))

#calcula as frequencias de ressonancia 
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            fr = frequenciaRessonancia(a, b, i, j, k, velocidadeFase(permissibilidadeRelativa, permeabilidadeRelativa))
            if(i==0 and j==0 and k==0):
                continue
            else:
                if(i > 0 and j > 0 and k >= 0):
                    modos.append(["ModoTM", i, j, k, fr])

                if((i != 0 or j != 0) and k > 0):
                    modos.append(["ModoTE", i, j, k, fr])

#ordena pela frequencia
modos = sorted(modos, key=lambda modos: modos[4])

#imprime os cinco modos de ordem mais baixa
#verifica casos TE e TM e adiciona mais um
i = 0
range = 5
while(i < range):
    if(modos[i][1] == modos[i+1][1] and modos[i][2] == modos[i+1][2] and modos[i][3] == modos[i+1][3]):
        range = range + 1
    print(modos[i])
    i = i + 1