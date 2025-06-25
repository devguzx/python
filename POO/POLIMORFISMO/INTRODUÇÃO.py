#Polimorfismo: poli = muitos, morfos = forma.

#Em POO, significa que um mesmo método pode ter comportamentos diferentes dependendo do objeto que o chama. (mesma interface, diferentes comportamentos)

#Exemplo: falar
class Comunicacao:
    def __init__(self):
        pass

    def falar(self):
        print("Todos seres se comunicam")

class Pessoa(Comunicacao):
    def falar(self):     #override: quando a classe filha redefine um método do pai.
        print("Oi.")

class Cachorro(Comunicacao):
    def falar(self):
        print("AU AU")

class Gato(Comunicacao):
    def falar(self):
        print("miaau")

p1=Pessoa()
c1=Cachorro()
g1=Gato()

p1.falar()
c1.falar()
g1.falar()

#Exemplo: pato (duck typing)
class Pato:
    def andar(self):
        print("O pato anda como um pato.")

class Robopato:
    def andar(self):
        print("O robopato anda com passos mecânicos.")

def fazer_andar(objeto):
    objeto.andar()

fazer_andar(Pato())        
fazer_andar(Robopato())