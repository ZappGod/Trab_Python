"""
Jogo Termo:Pegando as palavras do arquivo "lista_palavras.txt" ele escolhe uma palavra aleatoria para ser a escolhida,após isso o jogador tem que identificar essa palavra,é mostrado na tela o 
tamanho dessa palavra,que é uma lista do tamanho da palavra que o jogador tem que adivinhar como uma lista tambem das letras certas,o contador de tentativas que é do tamanho da palavra a ser 
adivinhada somando com mais 1,e depois da primeira tentativa é mostrado as palavras que ele tentou anteriormente,após ele escrever a tentativa,é verificado se a palavra tem o mesmo tamanho da palavra a ser 
adivinhada,se não tiver ele tem que colocar outra,se estiver do tamanho certo ele armazena ela na lista de tentativas e verifica cada letra pra ver se ela esta igual a palavra a ser adivinhada,
se tiver algumas letras certas elas seram mostradas na tela e na posição certa,elas seram mostradas na tela para ajudar o jogador a adivinhar,e um contador de tentativas vai adicionar -1,quando esse 
contador chegar a zero e o jogador não tiver acertado o jogo se encerra e mostra a palavra certa,porem se a lista de letras certas estiver cheia,assim indicando que o jogador acertou,mostra que ele 
acertou a palavra e a mostra na tela.
"""
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
