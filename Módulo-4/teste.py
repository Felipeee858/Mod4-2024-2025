import numpy as np
dados=np.array([10,3,-5,11,-10])
#nºs aray
print(len(dados))
#contar >= 0 and <0
contar_maior=0
contar_menor=0
for i in dados:
    if i >=0:
        contar_maior+=1
    else:
        contar_menor+=1
print(contar_maior)
print(contar_menor)

#inverter
invertido=np.zeros(len(dados))
for i in range(len(dados)):
    invertido[i]=dados[len(dados)-1-i]
print(invertido)


#capicua
#if frase == frase[::-1]