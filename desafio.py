menu = '''
----------------------------
    MENU DE OPERAÇÕES

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair
----------------------------
'''

saldo = 0
limite = 500
extrado = ''
deposito_list = []
saque_list = []
numero_saques =  0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()

    if opcao == 'D':
        deposito = float(input('Qual valor deseja depositar?\nR$ '))

        if deposito < 0:
            print(f'\nVocê tentou depositar R${deposito:.2f}.\nEsse valor é inválido. Por favor, faça um novo depósito.')
        else:
            saldo += deposito
            deposito_list.append(deposito)
            print(f'\nVocê realizou um depósito de R${deposito:.2f}.\nSeu Saldo atual é de R${saldo:.2f}')

    elif opcao == 'S':
        saque =  float(input('Você pode realizer até 3 saques no valor de R$500.00\nQual o valor que deseja sacar?\nR$ '))

        if saque > 500 or saque < 0:
            print(f'Você tentou sacar R${saque:.2f}. Por favor, faça uma saque no valor permitido')

        elif saque < 500 and numero_saques < LIMITE_SAQUES:
            if saque > saldo:
                print(f'Você tentou realizar um saque maior do que seu valor em conta.')
                print(f'SALDO: R${saldo:.2f}')
            else:
                saldo -= saque
                numero_saques += 1
                saque_list.append(saque)
                print(f'Você realizou um saque de R$ {saque:.2f}.\nSeu saldo atual é R$ {saldo:.2f}')

        else:
            print('Você já realizou todos os saques do dia. ')
            
    elif opcao == 'E':
        extrato = f'Depósitos: {deposito_list}\nSaques: {saque_list}\nSaldo atual: R${saldo:.2f}'
        print('*'*20)
        print('EXTRATO')
        print(extrato)
        print('*'*20)
    elif opcao == 'Q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')