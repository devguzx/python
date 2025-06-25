#@property é um decorador que transforma um método de uma classe em um atributo de leitura.

#Com ele, você acessa o valor retornando como se fosse um atributo comum, mas na verdade está chamando uma função por trás dos panos.

#Setter: modificação controlada

#Exemplo: 
class Pessoa:
    def __init__(self, nome):
        self.__nome=nome

    @property
    def nome(self):
        print(self.__nome)

    @nome.setter
    def nome(self, novo_nome):
        if (novo_nome!=self.__nome) and len(novo_nome)>0:
            self.__nome=novo_nome
        else:
            print("Nome inválido")

pessoa1 = Pessoa("Guthy")
pessoa1.nome

pessoa1.nome = "Elis" #modificação válida, pois no código existe o setter.
pessoa1.nome
