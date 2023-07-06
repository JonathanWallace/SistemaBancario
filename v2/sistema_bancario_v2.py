#Criando a função 'menu' para imprimir a estrutura textual do menu
def menu():
    print(f"""{'MENU DA CONTA'.center(22,'=')}
[1] Depositar
[2] Sacar
[3] Extrato
                    
[0] Sair
{'='*22}""")
    return  input('Escolha uma opção: ')#Input da opção do usuário, refêrente ao 'menu'

def menu_login():
    print(f"""{'MENU'.center(22,'=')}
[1] Logar
[2] Criar Novo Usuário
                    
[0] Sair
{'='*22}""")
    return  input('Escolha uma opção: ')#Input da opção do usuário, refêrente ao 'menu_login'

def menu_usuario():
    print(f"""{'MENU DO USUÁRIO'.center(22,'=')}
[1] Acessar Conta
[2] Criar Nova Conta
[3] Listar Contas
                    
[0] Sair
{'='*22}""")
    return  input('Escolha uma opção: ')#Input da opção do usuário, refêrente ao 'menu_login'
    
#Declarando as funções de cadastro.
def criar_usuario(users):#Cria um usuário e o adiciona no dicionario com o CPF sendo a chave.
    print('Cadastro de usuário:')
    while True:
        while True:
            try:
                cpf = int(input('Informe seu CPF(somente números): '))
                if str(cpf) not in users:
                    break
                else:
                    print('\033[1;31mEsse CPF já está em uso!\033[0;0m')
                    return users                
            except:
                print('\033[1;31mCPF inválido\033[0;0m')
        nome = input('Informe seu nome: ')
        data_nascimento = input('Data de Nascimento: ')
        logradouro = input('Logradouro: ')
        numero = input('Numero: ')
        bairro = input('Bairro: ')      
        cidade = input('Cidade: ')
        estado = input('Sigla do estado: ')
        endereco = f'{logradouro}, {numero} - {bairro} - {cidade} - {estado}'
        senha = input('Senha: ')
        break
    users[str(cpf)]= {'nome':nome,'nascimento':data_nascimento,'endereco':endereco, 'senha':senha}  
    with open('users.txt', 'w') as file:
                    for cpf, info in users.items():
                        file.write(f"{cpf}#{info['nome']}#{info['nascimento']}#{info['endereco']}#{info['senha']}#\n")  
    print('\033[0;32mUsuário criado com sucesso!\033[0;0m')    
    return users  

def logar(users):
    if users:
        cpf = input('Informe o CPF: ')
        senha = input('Informe a Senha: ')
        if cpf in users:
            if users[cpf]['senha'] == senha:
                print('\033[0;32mLogin realizado com sucesso!\033[0;0m')
                input("Aperte 'Enter' para continuar.")
                return True, cpf            
    else:
        print('\033[1;31mNão existe nenhum usuário cadastrado!\033[0;0m')
        return False, None
    print('\033[1;31mCPF ou Senha, inválidos!\033[0;0m')
    return False, None


    
def criar_conta(agencia, numero_conta, users, contas):#Cria uma conta e a adiciona na lista de contas.
    print('Cadastro de conta:')        
    cpf = input('Informe o CPF do usuário: ')
    if cpf not in users:
        print('\033[1;31mUsuário não existe!\033[0;0m')
        return contas
    else:
        print('\033[0;32mConta criada com sucesso!\033[0;0m')
        input("Aperte 'Enter' para continuar.")
        contas.append({'agencia':agencia, 'conta': numero_conta, 'usuario': users[cpf]})
        with open('contas.txt', 'a') as file:
            file.write(f"{agencia}#{numero_conta}#{cpf}#\n")
        return contas

def acessar_conta(contas):
    listar_contas(contas)
    numero_conta = input('Informe o número da conta que quer acessar:')
    for conta in contas:
        if conta['conta'] == numero_conta and conta:
            print(f"\033[0;32mConta Nº{numero_conta} acessada!\033[0;0m")
            input("Aperte 'Enter' para continuar.")
            return True, numero_conta
    else:
        return False, None


def listar_user(users):#Lista os usuários no sistema
    print('USUÁRIOS'.center(70,'='))
    for user, valor in users.items():
        print(f"Nome: {valor['nome']} - CPF: {user} - Data de Nascimento: {valor['nascimento']}\nEndereço: {valor['endereco']}\nE-mail: {valor['email']}")
        print('-'*70)        
    print('='*70)
    input("Aperte 'Enter' para continuar.")

def listar_contas(contas):#Lista as contas no sistema
    print('CONTAS'.center(70,'='))
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {str(conta['conta']).rjust(2, '0')}, Usuário: {conta['usuario']['nome']}") 
        print('-'*70)     
    print('='*70)

#Declarando as funções das operações
def depositar(saldo, valor, extrato, /):#Realiza o depósito do valor informado pelo usuário. Agora a 'Extrato' é uma lista que receberá tuplas ('movimentação','valor') a cada movimentação.
   
            if valor > 0:
                saldo += valor
                print(f"O valor de R${valor:.2f} foi depositado na conta com sucesso!")
                extrato.append(('DEPOSITO',valor))
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
    #Declarando as constantes que serão utilizadas nas operações
    LIMITE_SAQUES: int = 3
    AGENCIA: str = '0001'

    #Declarando as variaveis de controle de menu
    logado_user = False
    acesso_conta = False
    user_atual = None
    conta_atual = None


    #Declarando as variaveis que serão utilizadas nas operações
    saldo: float = 0
    limite: float = 500
    extrato: list = []

    numero_saques: int = 0    
    users: dict = {}
    contas: list= []

    #carregango lista de usuarios
    try:
        with open('users.txt', 'r') as file:
            for user in file.readlines():
                cpf,nome,nascimento,endereco,senha,_ = user.split('#')
                users[cpf]={'nome':nome,'nascimento':nascimento,'endereco':endereco, 'senha':senha}
    except:
        pass
       

    while True:
        #Se não estiver logado a um usuário ou sem acesso a conta
        if not logado_user and not acesso_conta:
            op = menu_login()
            if op == '1':#Opção Logar
                logado_user, user_atual = logar(users)
                try:
                    with open('contas.txt', 'r') as file:
                        for conta in file.readlines():
                            agencia,conta,cpf,_ = conta.split("#")                                                    
                            if cpf == user_atual:
                                contas.append({'agencia':agencia, 'conta': conta, 'usuario': users[user_atual]})
                except:
                    pass

            elif op == '2':#Opção 'Criar Usuário'
                users = criar_usuario(users)
                
            
            elif op == '0':#Opção 'SAIR'
                break
            else:
                print('Opção inválida!')


        #Se estiver logado a um usuário mas sem acesso uma conta
        elif logado_user and not acesso_conta:
            op = menu_usuario()
            if op == '1':#Acessar conta
                acesso_conta, conta_atual = acessar_conta(contas)                


            elif op == '2':#Opção 'Criar Conta'
                contas = criar_conta(AGENCIA, str(len(contas)+1), users, contas)                               

            elif op == '3':#Opção 'Listar Contas'
                listar_contas(contas)
            
            elif op == '0':#Opção 'SAIR'
                break
            else:
                print('Opção inválida!')
            

            
        #Se estiver logado a um usuário e acessando uma conta
        elif logado_user and acesso_conta:
            op = menu()        
            if op == '1':#Opção 'DEPOSITAR'
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
            
            
            #elif op == '6':#Opção 'Listar Usuários'
                #listar_user(users)
            
            elif op == '0':#Opção 'SAIR'
                break       

            else:
                print('Opção inválida!')
main()