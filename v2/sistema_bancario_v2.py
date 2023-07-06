#Criando a função 'menu' para imprimir a estrutura textual do menu
def menu():
    print(f"""{'MENU'.center(22,'=')}
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Usuários
[7] Listar Contas
          
[0] Sair
{'='*22}""")
    return  input('Escolha uma opção: ')#Input da opção do usuário, refêrente ao 'menu'
    
#Declarando as funções de cadastro.
def criar_usuario(users):#Cria um usuário e o adiciona no dicionario com o CPF sendo a chave.
    print('Cadastro de usuário:')
    while True:
        while True:
            try:
                cpf = int(input('Informe seu CPF(somente números): '))
                if cpf not in users:
                    break
                else:
                    print('Esse cpf já está em uso!')
                    return users                
            except:
                print('CPF inválido')
        nome = input('Informe seu nome: ')
        data_nascimento = input('Data de Nascimento: ')
        logradouro = input('Logradouro: ')
        numero = input('Numero: ')
        bairro = input('Bairro: ')      
        cidade = input('Cidade: ')
        estado = input('Sigla do estado: ')
        endereco = f'{logradouro}, {numero} - {bairro} - {cidade} - {estado}'
        break
    users[str(cpf)]= {'nome':nome,'nascimento':data_nascimento,'endereco':endereco}    
    print('Usuário criado com sucesso!')
    
    return users            
    
def criar_conta(agencia, numero_conta, users, contas):#Cria uma conta e a adiciona na lista de contas.
    print('Cadastro de conta:')        
    cpf = input('Informe o CPF do usuário: ')
    if cpf not in users:
        print('Usuário não existe!')
        return contas
    else:
        print('Conta criada com sucesso!')
        contas = [{'agencia':agencia, 'conta': numero_conta, 'usuario': users[cpf]}]
        return contas

def listar_user(users):#Lista os usuários no sistema
    print('USUÁRIOS'.center(70,'='))
    for user, valor in users.items():
        print(f"Nome: {valor['nome']} - CPF: {user} - Data de Nascimento: {valor['nascimento']}\nEndereço: {valor['endereco']}")
        print('-'*70)        
    print('='*70)
    input("Aperte 'Enter' para continuar.")

def listar_contas(contas):#Lista as contas no sistema
    print('CONTAS'.center(70,'='))
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {str(conta['conta']).rjust(2, '0')}, Usuário: {conta['usuario']['nome']}") 
        print('-'*70)     
    print('='*70)
    input("Aperte 'Enter' para continuar.")



#Declarando as funções das operações
def depositar(saldo, valor, extrato, /):#Realiza o depósito do valor informado pelo usuário. Agora a 'Extrato' é uma lista que receberá tuplas ('movimentação','valor') a cada movimentação.
   
            if valor > 0:
                saldo += valor
                print(f"O valor de R${valor:.2f} foi depositado na conta com sucesso!")
                extrato.append(('DEPÓSITO',valor))
                return saldo, extrato                
            else:
                print('O valor precisa ser positivo.')
                return saldo, extrato
        

def sacar(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):#Realiza o saque do valor informado pelo usuário. Agora a 'Extrato' é uma lista que receberá tuplas ('movimentação','valor') a cada movimentação.
    
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários alcançado, volte amanhã.")
        return saldo, extrato, numero_saques
    else:        
        if valor <= saldo and valor <= limite and valor > 0:
            saldo -= valor
            print(f'Valor de R${valor:.2f} retirado com sucesso!')
            extrato.append(('SAQUE',valor))
            numero_saques += 1
            return saldo, extrato, numero_saques          
        else:
            print("Valor fora do limite de saque ou saldo em conta.")
            return saldo, extrato, numero_saques
        
    

def tirar_extrato(saldo, /,* ,extrato):#Imprimi o extrato da conta, com base na lista de tuplas em 'extrato'
    print("EXTRATO".center(24,'='))
    if extrato:
        for mov, val in extrato:
            print(("\033[1;31m" if mov == 'SAQUE' else "\033[0;32m") + f'{mov:}:'.ljust(9) + f'R$ {val:.2f}'.rjust(15) + "\033[0;0m")
    else:
        print('Nenhuma movimentação.')
    print(f"Saldo atual: R${saldo:.2f}".rjust(24))
    print("="*24)
    input("Aperte 'Enter' para continuar.")


def main():
    #Declarando as variáveis e constantes que serão utilizadas nas operações
    LIMITE_SAQUES: int = 3
    AGENCIA: str = '0001'

    saldo: float = 0
    limite: float = 500
    extrato: list = []
    numero_saques: int = 0    
    users: dict = {}
    contas: list= []                      

    while True:
        op = menu()
        if op == '1':#Opção 'DEPOSITAR'0
            while True:
                try:
                    valor = float(input('Digite o valor a ser depositádo: '))
                    if valor > 0:
                        saldo, extrato = depositar(saldo, valor, extrato)
                        break
                    else:
                        print('Valor precisa ser positivo!')
                except:
                    print('Valor inválido.')

        elif op == '2':#Opção 'SACAR'
            while True:
                try:
                    valor = float(input("Digite o valor a ser retirado: "))
                    saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
                    break
                except:
                    print("Valor inválido.")

        elif op == '3':#Opção 'EXTRATO'
            tirar_extrato(saldo, extrato=extrato)

        elif op == '4':#Opção 'Criar Usuário'
            users = criar_usuario(users)
        elif op == '5':#Opção 'Criar Conta'
            contas = criar_conta(AGENCIA, len(contas)+1, users, contas)
        elif op == '6':#Opção 'Listar Usuários'
            listar_user(users)
        elif op == '7':#Opção 'Listar Contas'
            listar_contas(contas)
        elif op == '0':#Opção 'SAIR'
            break       

        else:
            print('Opção inválida!')

main()