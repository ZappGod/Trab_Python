import random
import os
from time import sleep

#função para definir a palavra aleatoriamente
def escolher_palavra():
    with open("lista_palavras.txt", "r",encoding = "UTF-8") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

p_secreta = escolher_palavra()
p_descobrindo = ["_"] * len(p_secreta)
lista_palavra = []
count_errado = len(p_secreta) + 1

#o programa vai rodar até você ganhar ou passar o nomero de tantativas
while count_errado > 0:
    os.system('cls')
    print(p_secreta)
    
    #mostra a palavra sendo descoberta,contagem de tentativas restantes e as ultimas palavras tentadas
    print(p_descobrindo)
    print(f"{count_errado} tentativas restantes")
    if len(lista_palavra) != 0:
        print(f"Ultimas palavras adivinhadas: {lista_palavra}")

    escolha = input("Tente adivinhar escrevendo a letra ou a palavra: ")
    lista_palavra.append(escolha)
    
    #não deixa a palavra tentada ser de tamanho diferente da palavra secreta
    if len(escolha) != len(p_secreta):
        os.system('cls')
        print("Tamanho da palavra invalido!")
        sleep(2)
        continue
    
    #coloca as letras da tentativa que são iguais e na mesma posição da palavra secreta na palavra sendo descoberta   
    for i in range(min(len(p_secreta), len(escolha))):
        if p_secreta[i] == escolha[i]:
            p_descobrindo[i] = p_secreta[i]
    count_errado -= 1        
    
    #se a palavra for acertada mostra que você acertou e a palavra  
    if p_descobrindo == list(p_secreta):
        os.system('cls')
        print(f"Você acertou!a palavra era {p_secreta}")
        sleep(2)
        break

#se acabar o número de tentativas encerra o programa
if count_errado == 0:
    os.system('cls')
    print(f"Número máximo de tentativas atingido! a palavra era {p_secreta}")
    sleep(2)