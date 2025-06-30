# Projeto 01: Sistema Bancário Simples 

#Iterador para listar contas
class ContaIterador:
    def __init__(self,lista):
        self.atual=0
        self.lista=lista

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual<len(self.lista):
            dados_conta=self.lista[self.atual]
            self.atual+=1
            return dados_conta
        else:
            raise StopIteration

#Decorador de logs
import datetime 
def log_transacoes(funcao):
    def wrapper(*args, **kwargs):
        agora=datetime.datetime.now()
        agora_formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
        resultado=funcao(*args, **kwargs)
        print(f"""    
        =============== Log Transações ===============
        Data e hora: {agora_formatado}
        Tipo de Transação: {funcao.__name__.title()}  
        ============================================== 
              """)
        return resultado
    return wrapper

# Variáveis principais
saldo = 0
depositos = []
saques = []
usuarios= []
contas=[]
num_conta=0


LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
limite_saque_diario = 0



@log_transacoes
def criar_conta_corrente():
    global num_conta, contas

    num_conta+=1

    agencia="0001"

    usuario_conta=input("Digite o CPF que esta vinculado ao seu cadastro: ").strip().replace(".","").replace("-","")

    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == usuario_conta), None)

    if usuario:
        conta={
            "agencia":agencia,
            "numero_conta":num_conta,
            "usuario":usuario 
        }
        
        contas.append(conta)
        print(f"""
Conta criada com sucesso!
Agência: {agencia}
Número da conta: {num_conta}
Titular: {usuario['nome']}
CPF: {usuario_conta}
""")
    else:
        print("Usuario não cadastrado! Se cadastre primeiro antes de fazer sua conta.")
        return


def listar_contas():
    if not contas:
        print("\nNenhuma conta criada no momento!")
        return
    else:
        for conta in ContaIterador(contas):
            print(f"""
    =============== CONTAS ===============
        Agência: {conta["agencia"]}
        Número da conta: {conta["numero_conta"]}
        Usuário: {conta["usuario"]["nome"]}
        CPF: {conta["usuario"]["cpf"]}
    ======================================
    """)

@log_transacoes
def cadastrar_usuario():
    global usuarios
    nome=str(input("Digite seu nome: ")).strip().title()

    data_nascimento=input("Digite sua data de nascimento(ex:04/01/2007): ")

    cpf=input("Digite seu cpf: ").strip().replace(".","").replace("-","")
    cpf_existe = any(usuario['cpf'] == cpf for usuario in usuarios)

    if cpf_existe:
        print("CPF já cadastrado no sistema!")
        return
    
    endereco = input("Digite seu endereço (Rua - Bairro - Cidade/Estado(sigla)): ").strip().replace(","," - ")


    usuario = {
    "nome": nome,
    "data_nascimento": data_nascimento,
    "cpf": cpf,
    "endereco": endereco,
}
    usuarios.append(usuario)
    print("Usuário cadastrado!")

def listar_usuarios():
    if not usuarios:
        print("Sem usúarios cadastrados.")
        return
    else:
        for usuario in usuarios:
            print(f"""
    =============== USUÁRIOS ===============
        Nome: {usuario["nome"]}
        Data de Nascimento: {usuario["data_nascimento"]}
        CPF: {usuario["cpf"]}
        Endereço: {usuario["endereco"]}
    ===============================================
    """ )

def menu():
    print("""
=============== SISTEMA BANCÁRIO ===============
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar Usuário
    [5] - Listar Usuários
    [6] - Criar conta corrente  
    [7] - Listar Contas   
    [8] - Sair
===============================================
""")

@log_transacoes
def depositar():
    global saldo, depositos
    deposito = float(input("Qual valor deseja depositar? "))

    if deposito <= 0:
        print("Valor inválido!")
    else:
        saldo += deposito
        depositos.append(deposito)
        print(f"Depósito de {deposito} reais realizado com sucesso!")
        print(f"Seu saldo: {saldo}")

@log_transacoes
def sacar():
    global saldo, saques, limite_saque_diario
    saque = float(input("Qual valor deseja sacar? "))

    if saque <= 0:
        print("Valor de saque inválido!")
    elif saque > saldo:
        print("Não é possível realizar o saque. Saldo insuficiente!")
    elif saque > LIMITE_SAQUE:
        print("Não é possível realizar o saque. O valor excede o limite de R$500 por saque!")
    elif limite_saque_diario >= LIMITE_DIARIO:
        print("Limite de saques diários atingido.")
    else:
        saldo -= saque
        saques.append(saque)
        limite_saque_diario += 1
        print(f"Saque de {saque} reais realizado com sucesso!")
        print(f"Seu saldo: {saldo}")

def extrato():
    print("====== EXTRATO ======")
    if not depositos:
        print("Nenhum depósito realizado.")
    else:
        for d in depositos:
            print(f"Depósito: R$ {d:.2f}")

    if not saques:
        print("Nenhum saque realizado.")
    else:
        for s in saques:
            print(f"Saque: R$ {s:.2f}")

    print(f"Saldo atual: R$ {saldo:.2f}")
    print("======================\n")

sistema_ativo=True
while sistema_ativo:
    try:
        menu()

        operacao = int(input("Digite o número da operação: "))

        if operacao == 1:
            depositar()

        elif operacao == 2:
            sacar()

        elif operacao == 3:
            extrato()

        elif operacao == 4:
            cadastrar_usuario()

        elif operacao == 5:
            listar_usuarios()

        elif operacao == 6:
            criar_conta_corrente()

        elif operacao == 7:
            listar_contas()

        elif operacao == 8:
            print("Até mais, volte logo.")
            sistema_ativo = False
        else:
            print("Operação inválida, por favor escolha uma operação válida.")
    except ValueError:
        print("Entrada Inválida")
