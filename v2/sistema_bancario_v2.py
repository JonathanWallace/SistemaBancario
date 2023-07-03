#Declarando as variáveis que serão utilizadas nas operações
saldo: float = 2000
limite: float = 500
extrato: list = []
numero_saques: int = 0
LIMITE_SAQUES: int = 3

#Criando a função 'menu' para imprimir a estrutura textual do menu
def menu():
    print(f"""{'MENU'.center(16,'=')}
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
{'='*16}""")

#Declarando as funções das operações
def depositar():#Realiza o depósito do valor informado pelo usuário. Agora a 'Extrato' é uma lista que receberá tuplas ('movimentação','valor') a cada movimentação.
    global numero_saques
    global LIMITE_SAQUES
    global limite
    global extrato
    global saldo
    
    while True:
            try:
                valor = float(input('Digite o valor a ser depositádo: '))
                if valor > 0:
                    saldo += valor
                    print(f"O valor de R${valor:.2f} foi depositado na conta com sucesso!")
                    extrato.append(('DEPÓSITO',valor))
                    break
                else:
                    print('O valor precisa ser positivo.')
            except:
                print('Valor inválido.')

def sacar():#Realiza o saque do valor informado pelo usuário. Agora a 'Extrato' é uma lista que receberá tuplas ('movimentação','valor') a cada movimentação.
    global numero_saques
    global LIMITE_SAQUES
    global limite
    global extrato
    global saldo

    if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários alcançado, volte amanhã.")
    else:
        while True:
            try:
                saque = float(input("Digite o valor a ser retirado: "))
                if saque <= saldo and saque <= limite and saque > 0:
                    saldo -= saque
                    print(f'Valor de R${saque:.2f} retirado com sucesso!')
                    extrato.append(('SAQUE',saque))
                    numero_saques += 1
                    break
                else:
                    print("Valor fora do limite de saque ou saldo em conta.")
            except:
                print("Valor inválido.")

def tirar_extrato():#Imprimi o extrato ta conta, com base na lista de tuplas em 'extrato'
    global extrato
    print("EXTRATO".center(24,'='))
    if extrato:
        for mov, val in extrato:
            print(("\033[1;31m" if mov == 'SAQUE' else "\033[0;32m") + f'{mov:}:'.ljust(9) + f'R$ {val:.2f}'.rjust(15) + "\033[0;0m")
    else:
        print('Nenhuma movimentação.')
    print(f"Saldo atual: R${saldo:.2f}".rjust(24))
    print("="*24)
    input("Aperte 'Enter' para continuar.")



#Inicio do sistema, pedindo o nome do cliente e iniciando um loop para exibir o 'menu'
nome: str = input('Informe seu nome: ')
print(f"Bom dia sr.{nome}. Bem vindo ao JonBank!")
while True:
    menu()
    op = input('Escolha uma opção: ')#Input da opção do usuário, refêrente ao 'menu'

    if op == '1':#Opção 'DEPOSITAR'
        depositar()

    elif op == '2':#Opção 'SACAR'
        sacar()

    elif op == '3':#Opção 'EXTRATO'
       tirar_extrato()
    elif op == '0':#Opção 'SAIR'
        break

    else:
        print('Opção inválida!')
