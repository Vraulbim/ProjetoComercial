import Funcionarios
import Clientes

print('--- Sistema de gestões ---')
print()

exit = False

while not exit:
    print('''Escolha a forma de entrada com base em seu perfil: 
        [1] - Para Funcionários e Administradores
        [2] - Para Clientes já cadastrados ou novo cadastro
        [3] - Sair do programa
            ''')

    choose = int(input('Qual a forma de entrada ? '))

    if choose == 1:
        Funcionarios.initializer()
    elif choose == 2:
        Clientes.initializer()
    elif choose == 3:
        input('Obrigado por utilizar nosso software!')
        exit = True
    else:
        input('Digite um comando válido! Enter para continuar...')
