class Pessoa:
    def __init__(self, nome):
        self.__nome = nome #Atributo privado

    def mostrar_nome(self): #Método público
        print(self.__nome)

pessoa1=Pessoa("guthy")

pessoa1.mostrar_nome()