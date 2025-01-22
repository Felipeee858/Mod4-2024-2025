"""
Programa para gerir uma agenda de de contactos. Cada contacto deve ter um nome, email e telefone
A agenda deve permitir:
1. Adicionar
2. Listar
3. Procurar
4. Apagar
5. Terminar
Utilize arrays para implementar as estruturas de dados.
"""
import numpy as np
#Estrutura de Dados
MAX_ITEMS = 100
def menu():
    nomes = np.empty(MAX_ITEMS,dtype="U50")
    emails = np.empty(MAX_ITEMS,dtype="U50")
    telefones= np.empty(MAX_ITEMS,dtype="U9")
    nr_contactos=0
    print("1. Adicionar\n2. Listar Todos\n3. Procurar\n4. Apagar\n5. Editar\n6. Terminar")
    op=0
    while op != 6:
        op=int(input("Introduza a sua opção: "))
        if op ==1:
            nr_contactos=Adicionar(nomes,emails,telefones,nr_contactos)
        elif op ==2:
            Listar(nomes,emails,telefones,nr_contactos)
        elif op ==3:
            Procurar(nomes,emails,telefones,nr_contactos)
        elif op ==4:
            nr_contactos=Apagar(nomes,emails,telefones,nr_contactos)
        elif op == 5:
            Editar(nomes,emails,telefones,nr_contactos)
        elif op == 6:
            break
        else:
            print("Opção Não Existe")

def Adicionar(nomes,emails,telefones,nr_contactos):
    """Função que adiciona um contacto a agenda"""
    if nr_contactos>=MAX_ITEMS:
        print("Erro excedeu o limite")
    else:
        nomes[nr_contactos]=input("Nome: ")
        emails[nr_contactos]=input("Email: ")
        telefones[nr_contactos]=input("Telefone: ")
        nr_contactos=nr_contactos+1
    return nr_contactos




def Listar(nomes,emails,telefones,nr_contactos):
    """Função para listar todos os nomes,emails e telefones"""
    for i in range(nr_contactos):
        print("Nome:",nomes[i], "Email:",emails[i],"Telefone:",telefones[i])


def Procurar(nomes,emails,telefones,nr_contactos):
    """Função para permitir procurar os nomes"""
    nome_procurar=input("Introduza o nome: ")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"{nomes[i]} \t {emails[i]} \t {telefones[i]} \t")
    


def Apagar(nomes,emails,telefones,nr_contactos):
    """Função para apagar algum contacto"""
    nome_procurar=input("Introduza o nome: ")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"{nomes[i]} \t {emails[i]} \t {telefones[i]} \t")
            op=input("Tem a certeza que pretende apagar este contacto? (s/n)")
            if op in "sS":
                for k in range(i,nr_contactos):
                    if k == MAX_ITEMS-1: #evita erro de ultrapassar o limite do array
                        break
                    nomes[k]= nomes[k+1]
                    emails[k] = emails[k+1]
                    telefones[k]= telefones[k+1]
                nr_contactos=nr_contactos-1
    return nr_contactos

def Editar(nomes,emails,telefones,nr_contactos):
    """Função pesquisa um contacto pelo nome e permite alterar os dados"""
    #pedir nome ao utilizador
    nome=input("Qual o nome do contacto a editar: ")
    #percorrer o array dos nomes
    for i in range(nr_contactos):
    #encontra o nome permite alterar os dados
        if nome in nomes[i]:
            print(f"Dados do contacto: {nomes[i]} - {emails[i]} - {telefones[i]}")
            op=input("Pretende editar estes dados? (S/N)")
            if op.lower()!="s":
                continue
            #editar os dados
            novo_nome=input("Introduza o novo nome ou deixa em branco para não alterar: ")
            novo_email=input("Introduza o novo email ou deixa em branco para não alterar: ")
            novo_telefone=input("Introduza o novo telefone ou deixa em branco para não alterar: ")
            if novo_nome.strip()!="":
                nomes[i]=novo_nome.strip()
            if novo_email.strip()!="":
                emails[i]=novo_email.strip()

            if novo_telefone.strip()!="":
                telefones[i]=novo_telefone.strip()
                


menu()
