#Exemplo: Veículo

class Veiculo:
    def __init__(self, marca, placa, cor):
        self.marca=marca
        self.placa=placa
        self.cor=cor

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


    

class Carro(Veiculo):
    def __init__(self, marca, placa, cor, qtd_bancos):
        super().__init__(marca, placa, cor)
        self.qtd_bancos=qtd_bancos

    
    
    
class Moto(Veiculo):
    def __init__(self, marca, placa, cor, cilindrada):
        super().__init__(marca, placa, cor)
        self.cilindrada=cilindrada
   


class Caminhao(Veiculo):
    def __init__(self, marca, placa, cor, carregado):
        super().__init__(marca, placa, cor)
        self.carregado = carregado


    def carregamento(self):
        print(f"{'Sim' if self.carregado else 'Nao'} esta carregado!")
    

v1 = Carro("fiat", "abc-123", "cinza",5)
print(v1)
v2 = Moto("ronda", "12345", "vermelha","600cc") 
print(v2)
v3 = Caminhao("fiat", "22222", "branco", False)
v3.carregamento()




