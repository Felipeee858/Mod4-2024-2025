"""
Um programa para registar os nomes dos clientes que entraram numa loja num determinado dia e o valor
das compras de cada.
O programa deve mostrar o nome do cliente que fez a compra mais cara"""

import numpy as np

MAX_CLIENTES=int(input("Quantos clientes entraram na loja?"))

nomes=np.empty(MAX_CLIENTES,dtype="U20")
compras=np.empty(MAX_CLIENTES,dtype="f")

def LerDados(nomes_clientes,compras_clientes):
    for i in range(MAX_CLIENTES):
        #ler nome
        nomes_clientes[i]= input("Nome: ")
        #ler valor compras
        compras_clientes[i]= input("Valor das compras: ")

def CompraCara(nomes_clientes,compras_clientes):
    #aior_compra=compras_clientes[0]
    posiçao=0
    #percorrer o array
    for i in range(MAX_CLIENTES):
        if compras_clientes [posiçao] < compras_clientes[i]:
            #guardar o maior valor e a posição   
            #maior_compra = compras_clientes[i]
            posiçao=i
    print(f"O melhor cliente foi {nomes_clientes[posiçao]} que gastou {compras_clientes[posiçao]}")

LerDados(nomes,compras)
CompraCara(nomes,compras)