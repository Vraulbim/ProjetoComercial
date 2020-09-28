import FunctionsData


def initializer():

    print('Faça login com usuário e senha! ')

    user = input('Digite seu usuario: ')
    key = input('Digite sua senha: ')
    feacth = FunctionsData.functionaryByUsername(user)

    if not feacth:
        username = ''
        password = ''
    else:
        for row in feacth:
            username = row[0]
            password = row[1]

    if user == username:
        if key == password:
            print(f'Bem-vindo {username}')
            logout = False
            while not logout:
                privileges = FunctionsData.getprivileges(username)
                if privileges == 'adm':
                    logout = dashboardAdministrator()
                else:
                    logout = dashboard()

        else:
            input('Senha inválida, tente novamente!')
    else:
        input('Usuário não existe!')


def dashboard():
    print(''' 
        [1]  - Listar clientes associados
        [2]  - Abrir uma ordem de serviço
        [3]  - Ver ordens em aberto
        [4]  - Ver ordens já finalizadas
        [5]  - Finalizar uma ordem
        [6]  - Cadastrar um novo produto
        [7]  - Ver requisição de produtos
        [8]  - fazer logout
        
        
        
    ''')
    check = int(input('Informe a opção da operação: '))

    if check == 1:
        FunctionsData.listClients()
    elif check == 2:
        nOrder = input('Digite o número da ordem: ')
        functionary = input('Nome do funcionário: ')
        client = input('Nome do cliente: ')
        description = input('Ordem: ')
        value = input('Valor: ')
        FunctionsData.createOrderService(nOrder, functionary, client, description, value)
    elif check == 3:
        FunctionsData.ordersBy('aberta')
    elif check == 4:
        FunctionsData.ordersBy('fechada')
    elif check == 5:
        FunctionsData.updateAOrder()
    elif check == 6:
        name = input('Digite o nome do produto: ')
        value = input('Digite o valor: ')
        description = input('Informe uma descricao se necessário: ')
        verify = FunctionsData.checkIfProductExists(name)
        if not verify:
            FunctionsData.saveNewProduct(name, value, description)
        else:
            input('Esse produto já existe')
    elif check == 7:
        FunctionsData.getRequicoesProducts()
    elif check == 8:
        return True

    return False


def dashboardAdministrator():
    print(''' 
        [1]  - Listar clientes associados
        [2]  - Abrir uma ordem de serviço
        [3]  - Ver ordens em aberto
        [4]  - Ver ordens já finalizadas
        [5]  - Finalizar uma ordem
        [6]  - Cadastrar novo funcionário
        [7]  - Cadastrar um novo produto
        [8]  - Ver requisição de produtos
        [9]  - fazer logout
        
        admin

    ''')
    check = int(input('Informe a opção da operação: '))

    if check == 1:
        FunctionsData.listClients()
    elif check == 2:
        nOrder = input('Digite o número da ordem: ')
        functionary = input('Nome do funcionário: ')
        client = input('Nome do cliente: ')
        description = input('Ordem: ')
        value = input('Valor: ')
        FunctionsData.createOrderService(nOrder, functionary, client, description, value)
    elif check == 3:
        FunctionsData.ordersBy('aberta')
    elif check == 4:
        FunctionsData.ordersBy('fechada')
    elif check == 5:
        FunctionsData.updateAOrder()
    elif check == 6:
        user = input('Digite o nome do novo usuário: ')
        key = input('Digite a senha: ')
        FunctionsData.createNewUser(user, key)
    elif check == 7:
        name = input('Digite o nome do produto: ')
        value = input('Digite o valor: ')
        description = input('Informe uma descricao se necessário: ')
        verify = FunctionsData.checkIfProductExists(name)
        if not verify:
            FunctionsData.saveNewProduct(name, value, description)
        else:
            input('Esse produto já existe')
    elif check == 8:
        FunctionsData.getRequicoesProducts()
    elif check == 9:
        return True

    return False





