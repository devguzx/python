#Produto com desconto

class Produto:
    def __init__(self, preco):
        if preco>0:
            self.__preco_com_desconto=preco*0.9
        else:
            raise ValueError("Preço inválido")
            
    @property
    def preco(self):
        return self.__preco_com_desconto
    
    @preco.setter
    def preco(self, valor):
        if valor>0:
            self.__preco_com_desconto=valor*0.9
            print("Preço atualizado")
        else:
            print("Preço inválido") 
        
p = Produto(100)
print(p.preco)     
p.preco = 200
print(p.preco)  
        