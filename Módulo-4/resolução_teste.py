#Problema-1
import numpy as np
nomes=input("Nomes: ")
Tempos=input("Tempos: ")
Pilotos=np.array(nomes.split(", "))
Voltas=np.array(Tempos.split(","))
i=0
PM=0
PP=0
while i<5:
    if int(Voltas[i]<0):
        Voltas[i]=int(input("..."))
    else:
        i+=1[PP]-Voltas[PM]


for i in range(5):
    if int(Voltas[i])<int(Voltas[PM]):
        PM=i
    elif Voltas[i]>Voltas[PP]:
        PP=i
Diferenca=Voltas[PP]-Voltas[PM]
print("Primerio",Pilotos[PM])
print("Ultimo",Pilotos[PP])
print("Diferença",Diferenca)
for i in range(5):
    print(Pilotos[i],Voltas[i])

#Problema-2
contar=0
email=input("")
PP=input("")
if len(PP)>=8:
    contar+=1
if PP not in email:
    contar=contar+1
for i in PP:
    if i>="a" and i<="z":
        contar=contar+1
        break
for l in PP:
    if l>="Z":
        contar+=1
        break
for i in PP:
    if i>"0" and i<="9":
        contar+=1
        break


    
