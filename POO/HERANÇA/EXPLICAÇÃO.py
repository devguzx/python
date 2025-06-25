#Herança: em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai(base).

#Herança Simples e Múltipa;

#Simples-
class ClassePai:
    pass
class ClasseFilha(ClassePai):
    pass

#mútipla-
class A:
    pass
class B:
    pass
class C(A,B):
    pass

#Exemplo:
class Animal:
    def __init__(self,nome):
        self.nome=nome

    def som_animal(self):
        print("Som do animal.")

class Cachorro(Animal):
    def som_animal(self): # sobrescrevendo o método
        print("AuAu")

c=Cachorro("TuTu")
c.som_animal()