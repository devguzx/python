#Caixa Eletronico

class CaixaEletronico:
    def __init__(self, saldo=0):
        if saldo>=0:
            self.__saldo = saldo
        else:
            raise ValueError("Saldo inválido.")

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor>0:
            self.__saldo=valor
           
        else:
            print("Saldo inválido")

    def ver_saldo(self):
        self.__mostar_saldo()

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

    def __mostar_saldo(self):
        print(f"Saldo = {self.__saldo:.2f}")        

c1 = CaixaEletronico(200)
c1.saldo = -20         
c1.saldo = 100         
c1.ver_saldo()
    