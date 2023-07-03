#Criando a variável 'menu' para armazenar a estrutura textual do menu
menu = f"""{'MENU'.center(16,'=')}
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
{'='*16}"""
#Declarando as variáveis que serão utilizadas nas operações
saldo: float = 2000
limite: float = 500
extrato: str = ''
numero_saques: int = 0
LIMITE_SAQUES: int = 3

#Inicio do sistema, pedindo o nome do cliente e iniciando um loop para exibir o 'menu'
nome: str = input('Informe seu nome: ')
print(f"Bom dia sr.{nome}. Bem vindo ao JonBank!")
while True:
    print(menu)
    op = input('Escolha uma opção: ')#Input da opção do usuário, refêrente ao 'menu'

    if op == 'd':#Opção 'DEPOSITAR'
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


    elif op == 's':#Opção 'SACAR'
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

    elif op == 'e':#Opção 'EXTRATO'
        print("EXTRATO".center(24,'='))
        print("Nenhuma movimentação." if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print("="*24)
        input("Aperte 'Enter' para continuar.")

    elif op == 'q':#Opção 'SAIR'
        break

    else:
        print('Opção inválida!')
