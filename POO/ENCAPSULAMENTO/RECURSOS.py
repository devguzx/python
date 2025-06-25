#Recursos públicos e privados:

#Público- Pode ser acessado de fora da classe
#Privado- Só pode ser acessado pela classe.

#Exemplo:
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular #Público - Pode ser acessado diretamente.
        self._saldo=saldo #Protegido - Pode ser acessado, mas não deveria fora da classe. (Por convenção)
        self.__senha="12345" #Privado - Não pode ser acessado diretamente.

    def ver_saldo(self):
        print(f"Saldo = R${self._saldo:.2f}")

    def sacar(self, valor, senha):
        if senha==self.__senha:
            if valor<=self._saldo:
                self._saldo-=valor
                print("Saque realizado")
            else:
                print("Saldo insuficiente.")
        else:
            print("Senha incorreta.")

conta = ContaBancaria("Guthierry", 200)
conta.ver_saldo()
conta.sacar(20, "1234") #Senha errada.

print(conta.__senha) #Não consigo ver a senha e nem modificar, pois esta privado. (Função do encapsulamento)