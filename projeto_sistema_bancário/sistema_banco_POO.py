#Modelando o sistema bancário em POO:
from abc import ABC, abstractmethod

class Transacao(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__()
        self.valor=valor

    
    def registrar(self,conta):
       if conta.depositar(self.valor):
           conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self,valor):
        super().__init__()
        self.valor=valor

    
    def registrar(self,conta):
       if conta.sacar(self.valor):
           conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self.__transacoes=[]

    @property
    def transacoes(self):
        return self.__transacoes
    

    def adicionar_transacao(self, transacao):
        self.__transacoes.append(transacao)
        
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf=cpf
        self.nome=nome
        self.data_nascimento=data_nascimento
    
class Conta:
    def __init__(self,saldo, numero,cliente, agencia= "0001"):
        self.__saldo = saldo
        self.__numero = numero
        self.__cliente = cliente
        self.__agencia = agencia
        self.__historico = Historico()

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def agencia(self):
        return self.__agencia
    
    
    @property
    def historico(self):
        return self.__historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(saldo=0,cliente=cliente, numero=numero)
    
    def sacar(self,valor):
        if valor<=self.__saldo:
            print("Saque realizado com sucesso")
            self.__saldo-=valor
            print(f"Saldo = R${self.__saldo:.2f}")
            return True
        else:
            print("Saque inválido")
            return False
        
    def depositar(self,valor):
        if valor<=0:
            print("Deposito inválido")
            return False
        else:
            print("Deposito realizado com sucesso")
            self.__saldo+=valor
            print(f"Saldo = R${self.__saldo:.2f}")
            return True
        
class ContaCorrente(Conta):

    def __init__(self, saldo, numero, cliente, agencia="0001"):
        super().__init__(saldo, numero, cliente, agencia)
        self.__limite=3
        self.__limite_saques=500
        self.__cont_saques=0

    @property
    def limite(self):
        return self.__limite
    
    @property
    def limite_saques(self):
        return self.__limite_saques
    
    @property
    def cont_saques(self):
        return self.__cont_saques
    
    def sacar(self, valor):
        if self.cont_saques>=self.__limite:
            print("Limite de saques diarios atingidos.")
            return False
        
        elif valor>self.limite_saques:
            print(f"Não é possível realizar o saque. O valor excede o limite de R${self.__limite_saques:.2f} por saque!")
            return False
        
        elif not super().sacar(valor):
            return False
        
        else:
            self.__cont_saques+=1
            return True
        
    def __str__(self):
        return f"""
        Agência: {self.__agencia}
        Número: {self.__numero}
        Titular: {self.cliente.nome}
                """ 

        

        
#Teste: 
cliente = PessoaFisica("Rua k", "12345678900", "Guthierry", "04/01/2007") 

conta = ContaCorrente.nova_conta(cliente, numero=1)

cliente.adicionar_conta(conta)

cliente.realizar_transacao(conta, Deposito(1000))
cliente.realizar_transacao(conta, Saque(200))      
cliente.realizar_transacao(conta, Saque(600))

        




    
    
