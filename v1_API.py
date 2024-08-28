menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite =  500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
lista_transacoes = []


def deposito():
    global saldo
    novo_deposito = float(input('Qual valor deseja depositar? R$'))
    if novo_deposito <= 0:
        print('=' * 34)
        print('ERRO!\nO valor inserido deve ser positivo')
        print('=' * 34)
    else:
        saldo += novo_deposito
        lista_transacoes.append({'DEPOSITO': novo_deposito})
        print('=' * 33)
        print('Deposito feito com sucesso\nQual operação deseja fazer agora?')
        print('=' * 33)


def saque():
    global saldo
    global numero_saques

    if numero_saques <  LIMITE_SAQUES:
        novo_saque = float(input('Qual valor deseja sacar? R$'))
        if novo_saque > saldo:
            print('=' * 36)
            print('Não será possível efetuar a operação\nseu saldo é insuficiente')
            print('=' * 36)
        elif novo_saque > limite:
            print('=' * 32)
            print('O valor máximo para uma operação\nde Saque é de R$500')
            print('=' * 32)
        else:
            saldo -= novo_saque
            lista_transacoes.append({'SAQUE': novo_saque})
            print('=' * 33)
            print('Saque feito com sucesso\nQual operação deseja fazer agora?')
            print('=' * 33)
            numero_saques += 1
    else:
        print('=' * 27)
        print('Você já realizou os\n3 saques diários permitidos')
        print('=' * 27)


def extrato():
    if len(lista_transacoes) == 0:
        print('=' * 31)
        print('Nenhuma transação foi realizada')
        print('=' * 31)
    else:
        for transacao in lista_transacoes:
            for chave, valor in transacao.items():
                print('{} de R${:.2f}'.format(chave, valor))