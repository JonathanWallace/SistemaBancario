menu = f"""{' Menu '.center(16,'#')}
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
{'#'*16}"""

saldo: float = 2000
limite: float = 500
extrato: str = ''
numero_saques: int = 0
LIMITE_SAQUES: int = 3

nome: str = input('Informe seu nome: ')
print(f"Bom dia sr.{nome}. Bem vindo ao JonBank!")
while True:
    print(menu)
    op = input('Escolha uma opção: ')

    if op == 'd':
        while True:
            try:
                valor = float(input('Digite o valor a ser depositádo: '))
                if valor > 0:
                    saldo += valor
                    print(f"O valor de R${valor:.2f} foi depositado na conta com sucesso!")
                    extrato += f'Depósito: \033[0;32mR${valor:.2f}\033[0;0m\n'
                    break
                else:
                    print('O valor precisa ser positivo.')
            except:
                print('Valor inválido.')


    elif op == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários alcançado, volte amanhã.")
        else:
            while True:
                try:
                    saque = float(input("Digite o valor a ser retirado: "))
                    if saque <= saldo and saque <= limite and saque > 0:
                        saldo -= saque
                        print(f'Valor de R${saque:.2f} retirado com sucesso!')
                        extrato += f'Saque: \033[1;31mR$-{saque:.2f}\033[0;0m\n'
                        numero_saques += 1
                        break
                    else:
                        print("Valor fora do limite de saque ou saldo em conta.")
                except:
                    print("Valor inválido.")

    elif op == 'e':
        print("Extrato".center(20,'#'))
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print("#"*20)
        input("Aperte 'Enter' para continuar.")

    elif op == 'q':
        break

    else:
        print('Opção inválida!')
