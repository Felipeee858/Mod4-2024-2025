"""Programa para preencher um array com 10 elementos em que cada
elemento é o dobro do valor do indice da sua posição"""
import numpy as np

NR_ELEMENTOS=10
numeros=np.empty(NR_ELEMENTOS,dtype="U20")
for i in range(NR_ELEMENTOS):
    numeros[i]=i*2

print(numeros)


    