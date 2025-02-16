def Contar(nomes,nome):
    contar_Repetidos=0
    for v in nomes:
        if v == nome:
            contar_Repetidos=contar_Repetidos+1
    return contar_Repetidos

def ContarV2(nomes,nome):
    contar_repetido=0
    for p in range(len(nomes)):
        if nomes[p]==nome:
            contar_repetido = contar_repetido + 1
    return contar_repetido

