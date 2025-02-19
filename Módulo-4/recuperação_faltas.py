"""6- Dentro do array apresentar o maior e o mais pequeno"""
import numpy as np
array=np.array([60,20,-40])

maior=array[0]
menor=array[0]
for i in array:
    if i > maior:
        maior=i
    elif i < menor:
        menor=i
print(maior)
print(menor)

"""3 - #Crie um programa que lê 10 valores do utilizador e calcula a média."""
NR_MAX=10
array=np.empty(NR_MAX)
média=0
for i in range(len(array)):
    array[i]=int(input("Introduza o número: "))
    média=média+array[i]
média=média/NR_MAX
print(média)