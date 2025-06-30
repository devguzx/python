#Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando infornações básicas de cada conta (número,agencia, usuario).

class ContaIterador:
    def __init__(self,lista):
        self.atual=0
        self.lista=lista

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual<len(self.lista):
            dados_conta=self.lista[self.atual]
            self.atual+=1
            return dados_conta
        else:
            raise StopIteration
        
