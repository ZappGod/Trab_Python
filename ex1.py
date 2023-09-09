"""
Jogo da velha 4x4: Primeiramente,imprime a tabela do jogo atravez de uma função que usa o for pra imprimir cada linha uma em baixo da outra corretamente,depois pega a linha e a coluna que o jogador decidir,
diminuindo por -1,assim ele pode escolher sem problemas a linha e a coluna normalmente,verificando se a posição que ele colocou existe na tabela ou se ja não foi colocado uma jogada la,
após isso armazena na tabela a jogada dele e soma +1 em um contador,pegando a tabela e o jogador atuais em uma função que verifica linha,coluna e verticais para saber se há ganhador,
verifica se o contador esta em 16,pois se estiver significa que não tem ganhadores e a mensagem "deu velha" aparece,após isso o player é atualizado para o proximo,isso tudo dentro de uma função 
while True até alguem ganhar ou der empate.
"""
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

tab = [["_","_","_","_"],
       ["_","_","_","_"],
       ["_","_","_","_"],
       ["_","_","_","_"]]
player = "X"
cont = 0

while True:
    imprimir_tab(tab)
    #mostra o jogador atual e pega a linha e a coluna da jogada dele
    print(f"jogador atual: {player}")
    linha = int(input("Informe a linha para a jogada: ")) - 1
    coluna = int(input("Informe a coluna para a jogada: ")) - 1
    
    #Verifica se o tamanho esta dentro do limite ou se ja colocaram uma jogada
    if linha < 0 or linha > 3 or coluna < 0 or coluna > 3 or tab[linha][coluna] != "_":
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
    if cont == 16:
        imprimir_tab(tab)
        print("Deu velha!")
        break
    #atualiza o player pra proxima jogada
    player = "O" if player == "X" else "X"
    
    
