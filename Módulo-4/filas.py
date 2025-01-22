"""O Sr.Joaquim tem restaurante muito popular é precisa de ajuda a gerir a fila de espera dos clientes.
Pretende-se criar um programa para registrar os nomes dos clientes em espera e de cada vez retirar o primeiro a chegar
á fila (FIFO)
Menu: 1.Entrada 2.Saída 3.Consultar Fila 4.Terminar"""
import numpy as np

NR_MAX=10

def Entrada(fila,nr_total):
    """Adicionar um nome ao final da fila de espera"""
    #procurar ultimo lugar da fila
    encontrou=False
    for posiçao in range(NR_MAX):
        if fila[posiçao] =="":
            encontrou=True
            break
    #avisar se a fila ta cheia
    if encontrou==False:
        print("Fila Cheia. Volte mais tarde.")
        return
    #ler nome
    nome=input("Indique o nome para a fila de espera: ")
    #inserir no final
    fila[posiçao]=nome
    print(f"A sua posição na fila de espera é {posiçao+1}")
def Saída(fila):
    """Retirar o primeiro nome da fila de espera"""
    fila_procurar=input("Introduza ")
    for k in range(fila):
        fila[k]=fila[k-1]

    
def Consultar(fila):
    """Listar os nomes na fila de espera"""
    pass


def main():
    fila=np.empty(NR_MAX,dtype="U20")
    nr_total=0
    #limpar array
    for i in range (NR_MAX):
        fila[i]=""
    op = 0
    while op != 4:
        op=input("1.Entrada\n2.Saída\n3.Consultar\n4.Terminar")
        if op =="1":
            Entrada(fila,nr_total)
        elif op =="2":
            Saída(fila)
        elif op =="3":
            Consultar(fila)
        elif op =="4":
            break
        else:
            print("Opção inválida")


if __name__=="__main__":
    main()