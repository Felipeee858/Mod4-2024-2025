import numpy as np
numeros=np.array([10,14,-5,33,120])
for i in range(5):
    print(numeros[i])

#passar os valores do array a zero
for i in range(5):
    numeros[i]=0

array_0dimensões=np.array(40)

#o tipo dados do array(numeros) e (array_0d)
print(type(numeros))
print(type(array_0dimensões))
print(array_0dimensões)

#quantas dimensões tem o array(numeros)
print(numeros.ndim)

for i in range(5):
    print(numeros[i])

for x in numeros:
    print(x)

for x in range(len(numeros)):
    print(numeros[x])

#criar um array vazio
vazio=np.empty(10)
print(vazio)


#criar um array com zeros
zeros=np.zeros(10)
print(zeros)
