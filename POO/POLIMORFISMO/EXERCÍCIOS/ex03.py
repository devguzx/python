#Desafio: figuras geométricas

class FiguraGeometrica:
    def __init__(self):
        pass

    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
    

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base=base
        self.altura=altura
        self.nome_figura = self.__class__.__name__.lower()

    def calcular_area(self):
        area = self.base*self.altura
        return area
    
class Quadrado(FiguraGeometrica):
    def __init__(self, tamanho_lados, ):
        super().__init__()
        self.tamanho_lados = tamanho_lados
        self.nome_figura = self.__class__.__name__.lower()

    def calcular_area(self):
        area = self.tamanho_lados**2
        return area
    
class Circunferencia(FiguraGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio=raio
        self.nome_figura = self.__class__.__name__.lower()

    def calcular_area(self):
        pi=3.14
        area = pi*(self.raio**2)
        return area


  
def mostrar_areas(figuras):
    for figura in figuras:
        area_figura = figura.calcular_area()
        print(f"""
        {figura.nome_figura.capitalize()}: Area = {area_figura:.2f}m²
        """)


lista_figuras=[
    Circunferencia(4),
    Circunferencia(7),
    Quadrado(10),
    Retangulo(27, 30)
]

mostrar_areas(lista_figuras)