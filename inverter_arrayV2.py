import numpy as np

NR_ELEMENTOS=5

nomes= np.empty(NR_ELEMENTOS,dtype="U20")
for i in range(NR_ELEMENTOS,dtype="U20"):
    nomes[i]= input(f"Introduza o nome:")
#criar o array para os elementos com posições invertidas
nomes_invertido=np.empty(NR_ELEMENTOS,dtype="U20")

#preencher o array invertendo as posições
k=NR_ELEMENTOS - 1
for i in range(NR_ELEMENTOS):
    nomes_invertido[k] = nomes[i]
    k = k-1
    
#mostrar os dois array
print(nomes,nomes_invertido)