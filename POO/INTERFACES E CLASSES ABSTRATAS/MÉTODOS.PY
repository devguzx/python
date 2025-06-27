#Método de instância:

class Pessoa:
    def __init__(self,nome):
        self.nome=nome

    def saudacao(self): #Método de instância
        return f"Olá, meu nome é {self.nome}"

#Método de classe: Pode acessar atributos e métodos da própria classe, e criar objetos da classe.
class Pessoa:
    ano_atual = 2025  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #Decorador
    def criar_com_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)  # cria e retorna uma instância da classe
    
p = Pessoa.criar_com_ano_nascimento("Guthierry", 2007)
print(p.nome, p.idade)

#Método estático: Usado para funções utilitárias, que fazem parte da lógica da classe, mas não dependem do estado dela.

class Calculadora:
    @staticmethod #decorador
    def somar(a, b):
        return a + b
resultado = Calculadora.somar(10,10)
print(resultado)


#Exemplo Geral: Sistema de cadastro de Alunos

class Aluno:
    ano_atual=2025

    def __init__(self, nome, idade, nota):
        self.__nome=nome
        self.__idade=idade
        if self.validadar_nota(nota):
            self.nota = nota 
        else:
            raise ValueError("Nota inválida")

    
    def mostrar_dados(self):
        print(f"Nome:{self.__nome} - Idade: {self.__idade} - Nota: {self.__nota}")
    
    @classmethod
    def criar_com_ano_de_nascimento(cls, nome, ano_nasc, nota):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade, nota)
    
    @staticmethod
    def validadar_nota(nota):
        return 0<=nota<=10

aluno1 = Aluno("Guthierry", 18, 9.5)
aluno1.mostrar_dados()

aluno2 = Aluno.criar_com_ano_de_nascimento("Elis", 2007, 10.0)
aluno2.mostrar_dados()

print(Aluno.validadar_nota(15))
print(Aluno.validadar_nota(10))