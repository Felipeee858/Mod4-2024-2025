"""Programa para ver se dois nomes completos e indicar se são famíliares. 2 nomes são familiares se o ultimo nome for igual
Versao hacker: Dois nomes são de familiares se um dos dois ultimos nomes forem iguais por qualquer ordem (ultimo=penultimo,ultimo=ultimo,penultimo=penultimo)"""

def Familiares(A,B) ->bool:
    """Função que devolve true se os nomes são familiares"""
    nomesA=A.split(" ") #lista com os nomes
    nomesB=B.split(" ") #lista com os nomes
    #verificar se os ultimos nomes são iguais
    if nomesA[len(nomesA)-1]: #saber a localização
        return True
    #verificar se um dos dois ultimos nomes são iguais

    for i in nomesA[1:]:
        for k in nomesB[1:]:
            if i ==k:
                return True
    return False

nomeA=input("Introduza um nome completo: ")
nomeB=input("Introduza um nome completo: ")
print(Familiares(nomeA,nomeB))