#Herança Múltipla: 

class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"Dispositivo: {self.marca} {self.modelo}"
    
class Conectavel:
    def __init__(self, conectado=False):
        self.conectado = conectado

    def conectar(self):
        self.conectado = True
        print("Dispositivo conectado à internet.")

    def desconectar(self):
        self.conectado = False
        print("Dispositivo desconectado da internet.")

class Recarregavel:
    def __init__(self, bateria=100):
        self.bateria = bateria

    def recarregar(self):
        self.bateria = 100
        print("Bateria recarregada.")

    def usar(self):
        if self.bateria > 0:
            self.bateria -= 10
            print(f"Usando dispositivo... Bateria em {self.bateria}%")
        else:
            print("Bateria descarregada!")

class Smartphone(Dispositivo, Conectavel, Recarregavel):
    def __init__(self, marca, modelo):
        Dispositivo.__init__(self, marca, modelo)
        Conectavel.__init__(self)
        Recarregavel.__init__(self)

    def status(self):
        conectado = "Sim" if self.conectado else "Não"
        return f"{self.info()}, Conectado: {conectado}, Bateria: {self.bateria}%"
    
s = Smartphone("Samsung", "Galaxy S23")

print(s.status())
s.conectar()
s.usar()
s.usar()
print(s.status())
s.desconectar()
s.recarregar()
print(s.status())