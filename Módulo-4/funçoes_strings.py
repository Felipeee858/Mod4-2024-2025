texto="ola mundo"

tamanho=len(texto)
print(tamanho)

texto=texto.upper() #devolve a string em maiusculas
print(texto)
texto=texto.lower() #devolve a string em minusculas
print(texto)
texto=texto.capitalize() #devolve a string com a primeira em M
print(texto)
texto=texto.strip() #devolve a string sem espaços em branco no inicio e no final
print(texto)
texto=texto.replace(" ","-") #devolve a string substituindo o primeiro parametro pelo segundo (" " por "-")
print(texto)
print(texto.isdigit()) #devolve verdadeiro se todos as letras sem digitos(numeros)
frase="Olá mundo, o computador é uma torradeira"
palavras = frase.split(" ") #devolve uma lista com as partes da string sepadaras por carater indicado " "
print(palavras[4])
print(len(palavras))
print(palavras[0])
posicao= frase.index("") #devolve a posiçao da string mas se não existir da erro
print(posicao)
posicao = frase.find("m") #devolve a posição da string se na encontar devolve -1
if posicao==-1:
    print("Não encontrei")
else:
    print("Encontrei na posição"+str(posicao)) 

#codigo ascii de uma letra
codigo= ord("a")
print(codigo)
#devolve a letra correspondente ao codigo ASCII
letra=chr(97)