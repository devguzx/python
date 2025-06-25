#Método construtor sempre é executado quando uma nova instância da classe é criada. (__init__)

#Método destrtutor sempre é xecutado quando uma instância (objeto) é destruída. (__del__)

class apresentacao:
    #Construtor
    def __init__(self, nome, idade, faculdade, area_interesse):
        self.nome=nome
        self.idade=idade
        self.faculdade=faculdade
        self.area_interesse=area_interesse
    
    #Destrutor
    def __del__(self):
        print("Removendo a instância da classe.")

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome}, tenho {self.idade} anos, faço faculdade de {self.faculdade} e quero se especializar em {self.area_interesse}.")
    
a1=apresentacao("Elis", 18, "Engenharia de Energias", "Hidrogênio verde")
a1.apresentar()

a2=apresentacao("Guthierry", 18, "Ciência da computação", "dados")
a2.apresentar()