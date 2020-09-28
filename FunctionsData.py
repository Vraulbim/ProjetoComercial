import sqlite3

banco = sqlite3.connect('banco/banco.db')
sql = banco.cursor()


def listClients():
    sql.execute("SELECT * FROM clientes")
    for row in sql.fetchall():
        print('Nome: ', row[0])
        print('-----------------------')
        print()

    input('Enter para continuar...')


def functionaryByUsername(username):
    sql.execute(f"SELECT * FROM usuarios WHERE username = '{username}'")
    cursor = sql.fetchall()
    return cursor


def clientByUsername(username):
    sql.execute(f"SELECT * FROM clientes WHERE clientName = '{username}'")
    cursor = sql.fetchall()
    return cursor


def getRequicoesProducts():
    sql.execute('SELECT * FROM requisicoes')
    for row in sql.fetchall():
        print('Nome do Cliente: ', row[1])
        print('Produto(s) requisitado: ', row[2])


def getRequisitionsClient(client):
    sql.execute(f"SELECT id, produtos FROM requisicoes WHERE nomeCliente= '{client}'")
    for row in sql.fetchall():
        print("ID da requisição: ", row[0])
        print("Produtos requisitados: ", row[1])

def getprivileges(user):
    sql.execute(f"SElECT privilegesUsers FROM usuarios WHERE username = '{user}'")
    for row in sql.fetchall():
        cursor = row[0]

    return cursor

def getAllProducts():
    sql.execute("SELECT nome, valor FROM produtos")
    for row in sql.fetchall():
        print('Nome: ', row[0])
        print('Valor: R$', row[1])
        print('---------------#####---------------')


def ordersBy(situation):
    sql.execute(f"SELECT * FROM ordens WHERE situacao = '{situation}'")
    for row in sql.fetchall():
        print('Numero de ordem: ', row[1])
        print('Funcionário: ', row[2])
        print('Cliente: ', row[3])
        print('Descrição do serviço: ', row[4])
        print('Valor : R$', row[6])
        print('------------------------------------------')

    input('Enter para continuar...')


def createOrderService(order, functionary, client, description, value):
    sql.execute(f"INSERT INTO ordens(ordem, funcionario, cliente, descricao, situacao, valor) "
                f"VALUES('{order}', '{functionary}', '{client}', '{description}', 'aberta', '{value}')")
    banco.commit()
    input('Cadastrado com sucesso! ')


def createNewUser(username, password):
    sql.execute(f"INSERT INTO usuarios(username, password) "
                f"VALUES ('{username}', '{password}')")
    banco.commit()
    input('Cadastrado com sucesso!! ')


def createRequisitions(nameClient, products):
    sql.execute(f"INSERT INTO requisicoes(nomeCliente, produtos) "
                f"VALUES ('{nameClient}', '{products}')")
    banco.commit()
    input('Cadastrado com sucesso!')


def updateAOrder():
    sql.execute("SELECT id, funcionario, descricao FROM ordens")
    for row in sql.fetchall():
        print('ID: ', row[0])
        print('Funcionário: ', row[1])
        print('Ordem: ', row[2])
        print('---------------------------------')

    id = int(input('Digite o id para atualizar: '))
    sql.execute(f"UPDATE ordens SET situacao = 'fechada' WHERE id = {id}")
    banco.commit()

    input('Atualizado com sucesso!')


def updatePasswordClient(clientName, password):
    sql.execute(f"UPDATE clientes SET clientPassword = '{password}' WHERE clientName = '{clientName}' ")
    banco.commit()
    input('Senha atualizada com sucesso...')

    return True

def saveNewClient(user, key):
    sql.execute(f"INSERT INTO clientes(clientName, clientPassword) VALUES('{user}', '{key}') ")
    banco.commit()
    input('Cliente cadastrado com sucesso!! ')


def saveNewProduct(name, value, desc):
    sql.execute(f"INSERT INTO produtos(nome, valor, descricao) VALUES('{name}', '{value}', '{desc}') ")
    banco.commit()
    print('Cadastrado com sucesso!')


def checkIfProductExists(product):
    sql.execute(f"SELECT nome FROM produtos where nome ='{product}' ")
    varName = sql.fetchone()

    if not varName:
        return False
    else:
        return True


