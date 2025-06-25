#O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, tornando-o mais modular e extensível.

#Classes e Objetos: Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. já os objetos podemos usá-los e eles possuem as características e comportamentos que foram de finidos nas classes.

#Classes- Define como os objetos vão ser.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#Objetos- É uma instância da classe.
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

#Atributos- São as variáveis do objeto, como (nome) e (idade) no exemplo acima.

#Métodos- são as funções dentro da classe
class Pessoa:
    def __init__(self, nome, idade): #construtor
        self.nome=nome #atributo
        self.idade=idade #atributo

    def dizer_ola(self): #método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def __del__(self):
        print(f"{self.nome} foi destruída.")

#Criando objetos
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

p1.dizer_ola()
p2.dizer_ola()