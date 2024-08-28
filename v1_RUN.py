from v1_API import deposito, saque, extrato, menu


while True:

    opcao = input(menu).lower().strip()[0]

    if opcao == 'd':
        deposito()

    elif opcao == 's':
        saque()

    elif opcao == 'e':
        extrato()

    elif opcao == 'q':
        break
    
    else:
        print('=' * 33)
        print('Operação inválida, tente novamente')
        print('=' * 33)


