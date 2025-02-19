"""Crie um programa que utiliza um array de 1 dimensão para guardar 10 valores. Os valores
devem ser introduzidos pelo utilizador e, antes de terminar, o programa deve listar todos os
valores do array."""

import numpy as np
NR_MAX=3
"""array=np.empty(NR_MAX,dtype="i")


for i in range(NR_MAX):
    array[i]=int(input("Introduza o número: "))

"""#Altere o programa anterior para listar os valores por ordem inversa."""

"""for i in range(NR_MAX-1,-1,-1):
    print(array[i])"""
    
"""3 - #Crie um programa que lê 10 valores do utilizador e calcula a média."""
"""
array=np.empty(NR_MAX)
média=0
for i in range(len(array)):
    array[i]=int(input("Introduza o número: "))
    média=média+array[i]
média=média/NR_MAX
print(média)"""


"""Cria um array preencher o array com números e somar todos os números"""

"""
array=np.array([10,20,40])
soma=0
for i in array:
    soma=soma+i

print(soma)"""

"""6- Dentro do array apresentar o maior e o mais pequeno"""
"""array=np.array([10,20,40])

maior=array[0]
menor=array[0]
for i in array:
    if i > maior:
        maior=i
    elif i < menor:
        menor=i
print(maior)
print(menor)"""


vogal="aeiou"

frase=input("Introduza a frase: ")
contar=0
for i in frase:
    if i in vogal:
        contar=contar+1
print(contar)
