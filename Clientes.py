import FunctionsData

#comentário
#comentário 2

def initializer():
    answerNewClient = int(input('Digite [1] - Para logar com um perfil existente e [2] - Para criar um novo:  '))
    try:
        if answerNewClient == 2:
            user = input('Digite um nome de usuário: ')
            key = input('Agora digite uma senha: ')
            FunctionsData.saveNewClient(user, key)
        elif answerNewClient == 1:
            print('Faça login com usuário e senha! ')

            user = input('Digite seu usuario: ')
            key = input('Digite sua senha: ')
            cursor = FunctionsData.clientByUsername(user)

            if not cursor:
                username = ''
                password = ''
            else:
                for row in cursor:
                    username = row[0]
                    password = row[1]

            if user == username:
                if key == password:
                    print(f'Bem-vindo {username}')
                    dashboard(username)
                else:
                    input('Senha inválida, tente novamente!')
            else:
                input('Usuário não existe!')
        else:
            input('Essa não é uma opção válida, tente novamente... ')
    except:
        input('Algo deu errado! ', )


def dashboard(username):
    exit = False

    while not exit:
        print(''' 
            [1] - Fazer requisição de um produto
            [2] - Ver requisições em andamento
            [3] - Ver produtos disponíveis
            [4] - Alterar senha
            [] - Logout
            
            
        ''')
        choose = int(input('Digite sua escolha: '))

        if choose == 1:
            products = input('Digite o produto: ')
            nameClient = input('Nome do cliente:')
            FunctionsData.createRequisitions(nameClient, products)
        elif choose == 2:
            nameClient = input('Digite seu usuário: ')
            FunctionsData.getRequisitionsClient(nameClient)
        elif choose == 3:
            FunctionsData.getAllProducts()
            input('Enter para continuar... ')
        elif choose == 4:
            password = input('Digite a nova senha: ')
            passwordKey = input('Digite a novamente a senha: ')
            if password == passwordKey:
                exit = FunctionsData.updatePasswordClient(username, password)
            else:
                input('As senhas não são iguais')
        elif choose == 5:
            exit = True
        else:
            input('Opção inválida, tente novamente!!! ')
