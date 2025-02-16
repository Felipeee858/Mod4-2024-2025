import numpy as np

#definir um array para strings
"""
i - inteiros
f - reais
b - boleanos
s - strings
U - unicode string
M- datetime
"""

nomes=np.empty(4,dtype="U20") #20 é o tamanho máximo no caso do nome
print(nomes)
for i in range(len(nomes)):
    nomes[i] = input("Introduza o nome: ")
print(nomes)