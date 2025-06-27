#Classes abstratas: É uma classe que não pode ser instânciada diretamente. Define uma estrutura que suas subclasses devem seguir.

#Não é possível instanciar uma classe abstrata diretamente.

#Subclasses devem implementar todos os métodos abstratos para poderem ser nstanciadas

#Abstract Base Classe
from abc import ABC, abstractmethod

#Exemplo
class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"