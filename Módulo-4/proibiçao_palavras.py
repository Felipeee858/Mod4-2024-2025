import numpy as np
proibidas=np.array(["Mal","Pobre","Infeliz","Péssimo"])
Alternativas=np.array(["Bom","Rico","Feliz","Otimo"])

frase=input("Introduza a frase: ")

for i in range(len(proibidas)):
    if proibidas[i] in frase:
        frase=frase.replace(proibidas[i],Alternativas[i])

print(frase)


