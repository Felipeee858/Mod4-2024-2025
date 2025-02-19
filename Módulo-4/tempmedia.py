import numpy as np
NR_TEMPERATURAS=12
#declaração do array
temperaturas=np.zeros(NR_TEMPERATURAS)
#leitura das temperaturas para o array
for i in range(NR_TEMPERATURAS):
    temperaturas[i]= input(f"Introduza as temperaturas:")

#calcular média
total=0
for i in range(NR_TEMPERATURAS):
    total+=temperaturas[i]
Média=total/NR_TEMPERATURAS
print(f"A temperatura média anual foi de {Média}")
#mostrar meses com temperatura superior a média´
for mes in range(NR_TEMPERATURAS):
    if temperaturas[i]>Média:
        print(f"A temperatura do mês {i+1} foi de {temperaturas[i]} sendo superior à média")

#calcular o Maior e o Menor
Maior=temperaturas[0]
Menor=temperaturas[0]
for i in range (1,NR_TEMPERATURAS):
    if temperaturas[i] > Maior:
        Maior=temperaturas[i]
    elif temperaturas[i]<Menor:
        Menor=temperaturas[i]
print(f"A temperatura mais elevada foi de {Maior} e a menor temperatura foi de {Menor}")

#calcular a moda
moda=temperaturas[0]
nr_vezes_moda=0
for i in range(NR_TEMPERATURAS):
    conta=0
    for m_atual in range(NR_TEMPERATURAS):
        if temperaturas[i]==temperaturas[m_atual]:
            conta=conta+1
    if conta>nr_vezes_moda: # se o conta é superior ao nr_vezes_moda este passa a ser a moda
        nr_vezes_moda=conta #nº de vezes que a temperatura da posição i aparece
        moda=i #a posição da temperatura contada
print(f"A moda é a temperatura {temperaturas[moda]} que ocorreu {nr_vezes_moda} vezes")




print(Média)








