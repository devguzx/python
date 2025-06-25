#Encapsulamento: Princípio da POO que trata de proteger os dados internos de um objeto e controlar como esses dados podem ser acessados e modificados.

#Exemplo: Conta no banco (com restrição de acesso ao saldo)
class Conta:
    def __init__(self, titular, idade, saldo=0):
        self.titular = titular
        self.idade = idade
        self.__saldo = saldo #atributo privado

    def depositar(self,valor):
        #...
        self.__saldo += valor 
        self.__ver_saldo()
        

    def sacar(self,valor):
        #...
        self.__saldo -= valor
        self.__ver_saldo()

    def __ver_saldo(self): # método privado
        #...
        print(f"Saldo = R${self.__saldo:.2f}")

    @property
    def saldo_conta(self): # leitura sem alteração
        return self.__saldo

conta1 = Conta("Guthierry", 18)

conta1.depositar(2000)
conta1.sacar(1000)
print(conta1.saldo_conta)




        
