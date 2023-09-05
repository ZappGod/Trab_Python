import random
import os
from time import sleep

def escolher_palavra():
    with open("lista_palavras.txt", "r",encoding = "UTF-8") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

p_secreta = escolher_palavra()
p_descobrindo = ["_"] * len(p_secreta)
l_adivinhadas = []
count = 6

while count > 0:
    os.system('cls')
    print(p_secreta)
    print(p_descobrindo)
    escolha = input("Tente adivinhar escrevendo a letra ou a palavra: ")
    
    if len(escolha) == 1:
        if escolha in l_adivinhadas:
            print("Você ja escreveu essa letra antes!")
            sleep(2)
            continue
        if escolha in p_secreta:
            for i in range(len(p_secreta)):
                if p_secreta[i] == escolha:
                    p_descobrindo[i] = escolha
            l_adivinhadas.append(escolha)
            continue  
        
        if len(p_secreta) == len(l_adivinhadas):
            print(f"Você acertou a palavra!A palavra era {p_secreta}")
            sleep(2)
            break

        else:
            print("Letra errada!")
            sleep(2)
            count -= 1

    else:
        if escolha == p_secreta:
            print(f"Você acertou!a palavra era {p_secreta}")
            sleep(2)
            break
        else:
            print("Você errou a palavra!")
            count -= 1
            sleep(2)
        

    
if count == 0:
    print(f"Número máximo de tentativas atingido! a palavra era {p_secreta}")
    sleep(2)