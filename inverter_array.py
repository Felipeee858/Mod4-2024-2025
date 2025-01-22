"""Programa para inverter um array de nomes com 5 elementos"""
import numpy as np

NR_ELEMENTOS = 5


nomes=np.array(["Ab","Ac","Ad","Ae","Af"])
k=4
temp = ""
for i in range(NR_ELEMENTOS//2):
    temp = nomes[i]
    nomes[i]=nomes[k]
    nomes[k] = temp
    k=k-1


print(nomes)




