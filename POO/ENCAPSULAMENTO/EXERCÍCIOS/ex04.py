#Conta bancária com segurança

class Conta:
    def __init__(self, titular, saldo = 0):
        if saldo >=0:
            self.__titular = titular #Atributo privado
            self.__saldo = saldo #Atributo privado
        else:
            raise ValueError("Saldo inválido!")
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    def __mostrar_saldo(self): #Método privado
        print(f"Saldo = R${self.__saldo:.2f}")

    def depositar(self,valor): #Método público
        if valor > 0:
            self.__saldo+=valor
            print("Deposito concluído.")
            self.__mostrar_saldo()
        else:
            print("Deposito inválido.")

    def sacar(self,valor): #Método público
        if (valor<=self.__saldo) and valor > 0: 
            self.__saldo-=valor
            print("Saque Realizado.")
            self.__mostrar_saldo()
        else:
            print("Saque inválido")

conta1= Conta("Guthy",200)
print(conta1.saldo)
conta1.depositar(2000)
conta1.depositar(300)

conta1.sacar(1000)
print(conta1.saldo)
