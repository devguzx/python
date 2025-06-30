#Iterador personalizado

class MultiplosDeN:
    def __init__(self, multiplo_base, limite):
        self.multiplo_base=multiplo_base
        self.limite=limite
        self.multiplo=0
        self.multiplicador=0



    def __iter__(self):
        return self
    
    def __next__(self):
        if  self.multiplo_base*self.multiplicador<=self.limite:
            self.multiplo=self.multiplo_base*self.multiplicador
            numero=self.multiplo
            self.multiplicador+=1
            return numero
        else:
            raise StopIteration
        
for valor in MultiplosDeN(5, 21):
    print(valor)
