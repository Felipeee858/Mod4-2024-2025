import numpy as np
carros=np.array(["Tesla","Volvo","Bmw","Peugeot","Tesla","Mercedes","Ford"])
marcas=np.zeros(len(carros),dtype="U20")

n=0
for carro in carros:
    if carro in marcas:
        continue
    marcas[n]=carro
    n=n+1
    contar=0
    for carro2 in carros:
        if carro==carro2:
            contar=contar+1
    print(f"A {carro} tem {contar} carro(s)")