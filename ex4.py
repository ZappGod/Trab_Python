"""
“Banco de dados” de dicionários:Primeiramente o usuário tem que entrar com os campos que ele quer que tenha no banco de dados,após isso mostra o menu que ele decide se quer cadastras,
imprimir ou encerrar,na primeira opção ele pega os campos que escolheu e joga para a função que cadastra os dados e depois pede para ele escrever a informação a cada respectivo campo que ele 
escolheu e armazena no banco de dados,assim voltando novamente para o menu.Na segunda opção,vai ser redirecionado para a função de imprimir esses dados,e la ira perguntar como ele deseja 
imprimir,se for todos os dados ele apenas imprime tudo e mostra ao usuário,se for por nomes,ele mostra na tela os dados dos nomes que o usuário colocou,se for por campos,
mostra os dados de quem tiver os campos desejados,e se for por nomes e campos,ele filtra os dados dos nomes,dados e os valores dos dados que o usuário escolher.E por fim a ultima 
opção do menu é para encerrar o programa
"""
#armazenamento dos usuarios
banco_user = []

#armazena os campos para armazenar os usuarios
def cadastro(camp_obrig):
    user = {}
    for campo in camp_obrig:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        user[campo] = valor
    banco_user.append(user)

#imprime os usuarios com base no que foi escolhido
def imprimi(*args, **kwargs):
    opcao = input("1 - imprimir todos\n2 - filtrar por nomes\n3 - filtrar por campos\n4 - filtrar por nomes e campos\n")
    
    if opcao == '1':
        for user in banco_user:
            print(user)
    elif opcao == '2':
        nomes = input("Digite os nomes separados por vírgula: ").split(',')
        for user in banco_user:
            if user['nome'] in nomes:
                print(user)
    elif opcao == '3':
        campo = input("Digite o campo de busca: ")
        valor = input(f"Digite o valor para o campo '{campo}': ")
        for user in banco_user:
            if campo in user and user[campo] == valor:
                print(user)
    elif opcao == '4':
        nomes = input("Digite os nomes separados por vírgula: ").split(',')
        campo = input("Digite o campo de busca: ")
        valor = input(f"Digite o valor para o campo '{campo}': ")
        for user in banco_user:
            if user['nome'] in nomes and campo in user and user[campo] == valor:
                print(user)
    else:
        print("Opção inválida")

camp_obrig = input("Digite os campos obrigatórios separados por vírgula: ").split(',')

#o programa vai rodar até você decidir parar
while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Imprimir usuários")
    print("0 - Encerrar")
        
    opcao = input("Digite a opção desejada: ")
        
    if opcao == '1':
        cadastro(camp_obrig)
        print("Usuário cadastrado com sucesso!")
    elif opcao == '2':
        imprimi()
    elif opcao == '0':
        break
    else:
        print("Opção inválida")
