#Exercício 01:

class InstrumentoMusical:
    def __init__(self):
        pass

    def tocar(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class Violao(InstrumentoMusical):
    def tocar(self):
        print("trililili...")

class Piano(InstrumentoMusical):
    def tocar(self):
        print("plin plon plin plon...")

class Bateria(InstrumentoMusical):
    def tocar(self):
        print("Pam pam tack tack pam...")


def executar_teste(obj):
    obj.tocar()

executar_teste(Piano())
executar_teste(Violao())
executar_teste(Bateria())