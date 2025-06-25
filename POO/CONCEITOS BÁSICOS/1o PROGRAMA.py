# João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.

#Classe
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BIBIIIIII!")

    def parar(self):
        print("Parando a bike...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm!")

    def __str__(self):
        return f"{self.__class__.__name__}:{', '. join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


#Objeto
b1 = Bicicleta("Vermelha", "caloi", 2020, 1000)
b1.buzinar()
b1.correr()
b1.parar()
print(b1)
    