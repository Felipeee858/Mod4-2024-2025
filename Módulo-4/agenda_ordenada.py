"""Criar uma agenda que regista os nomes por ordem alfabética.
Guardar o nome e data de nascimento das pessoas ordenadas por ordem crescente do nome."""
import numpy as np
NR_MAX=10

def Adicionar(contactos,nome):
    """Recebe um array e o nome do contacto a inserir por ordem alfabética"""
    #verificar está vazio o array
    if contactos[0]=="":
        contactos[0]=nome
        return
    #verificar se está cheio
    if contactos[NR_MAX-1]!="":
        print("Agenda de contactos está cheia")
        return
    #procurar a posição do novo contacto
    for posicao in range(NR_MAX):
        if nome < contactos[posicao] or contactos [posicao]=="":
            break
    #avançar uma posição os restantes contactos
    for i in range(NR_MAX-1,posicao,-1):
        contactos[i]=contactos[i-1]
    #inserir contacto
    contactos[posicao]=nome

def Listar(contactos):
    """Lista os nomes e datas de nascimento de todos os contactos"""
    for nome in contactos:
        partes = nome.split("-")
        print(f"nome: {partes[0]} Data Nascimento: {partes[1]}")
def Pesquisar(contactos,nome):
    """Recebe o array e o nome a pesquisar"""
    pass








def main():
    contactos=np.zeros(NR_MAX,dtype="U30")
    op = 0
    while op != 4:
        op=input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Terminar\n")
        if op =="1":
            nome=input("Nome do contacto a adicionar")
            data=input("Data de nascimento")
            Adicionar(contactos,nome + "-" + data)
        elif op =="2":
            Listar(contactos)
        elif op =="3":
            nome=input("Nome do contacto a adicionar")
            Pesquisar(contactos,nome)
        elif op =="4":
            break
        else:
            print("Opção inválida")


if __name__=="__main__":
    main()