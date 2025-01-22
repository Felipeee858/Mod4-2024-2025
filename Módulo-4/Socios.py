import numpy as np

Socios_A=np.array(["Joaquim","Maria","João"])
Socios_B=np.array(["Maria","António","Carla"])

#listar os socios que pertence aos dois clubes
contar=0
for nome_A in Socios_A:
    for nome_B in Socios_B:
        if nome_A==nome_B:
            print(f"O sócio com o nome {nome_A} pertence aos dois clubes")

#versão 2
for nome_A in Socios_A:
    if nome_A in Socios_B:
        print(f"O sócio com o nome {nome_A} pertence aos dois clubes")

