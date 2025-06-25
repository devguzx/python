class Pessoa:
    def __init__(self, nome):
        if len(nome)>0 and isinstance(nome, str):      
          self.__nome = nome #Atributo privado
        else:
            raise ValueError("Nome inválido")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        if len(novo_nome)>0 and isinstance(novo_nome, str):
            self.__nome=novo_nome
        else:
            print("nome inválido")

    
pessoa1=Pessoa("guthy")
print(pessoa1.nome)

pessoa1.nome="" #Nome inválido
pessoa1.nome="Elis" #Válido

print(pessoa1.nome )
