import os
from time import sleep

def verifica_vitória(tab,player):
    
    #verificar vitória na linha
    for linha in tab:
        if all([i == player for i in linha]):
            return True
    
    #verificar vitória na coluna
    for coluna in range(len(tab)):
        if all([tab[i][coluna] == player for i in range(len(tab))]):
            return True
    
    #verifica a vitória nas diagonais
    if all([tab[i][i] == player for i in range(len(tab))]) or all([tab[i][len(tab) - i - 1] == player for i in range(len(tab))]):
        return True
    
    return False

def imprimir_tab(tab):
    #limpar a tela
    os.system('cls')
    #Imprime o tabuleiro
    for i in tab:
        print(i)

def tamanho_tab(tam):
    return[["_" for _ in range(tam)] for _ in range(tam)]

#verifica o tamanho dado e impede que seja menor que 2    
while True:
    os.system('cls')
    tam = int(input("Entre com o tamanho que deseja para o jogo: "))
    
    if tam < 2:
        print("Tamanho minimo de 2")
        sleep(2)
    else:
        break

tab = tamanho_tab(tam)
player = "X"
cont = 0

while True:
    imprimir_tab(tab)
    #mostra o jogador atual e pega a linha e a coluna da jogada dele
    print(f"jogador atual: {player}")
    linha = int(input("Informe a linha para a jogada: ")) - 1
    coluna = int(input("Informe a coluna para a jogada: ")) - 1
    
    #Verifica se o tamanho esta dentro do limite ou se ja colocaram uma jogada no local
    if linha < 0 or linha >= tam or coluna < 0 or coluna >= tam or tab[linha][coluna] != "_":
        print("Jogada inválida")
        sleep(2)
        continue
    
    #atualiza a tabela e o contador
    tab[linha][coluna] = player
    cont += 1
    
    #verifica quem ganhou e mostra na tela
    if verifica_vitória(tab,player):
        imprimir_tab(tab)
        print(f"Parabéns!O jogador {player} vendeu!!")
        break
    
    #verifica se ainda tem espaço na tabela
    if cont == tam * tam:
        imprimir_tab(tab)
        print("Deu velha!")
        break
    #atualiza o player pra proxima jogada
    player = "O" if player == "X" else "X"
    
    