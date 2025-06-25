class Pessoa:
    def __init__(self, nome):
        self.__nome = nome #Atributo privado

    @property
    def nome(self):
        return self.__nome
    
pessoa1=Pessoa("guthy")

print(pessoa1.nome)