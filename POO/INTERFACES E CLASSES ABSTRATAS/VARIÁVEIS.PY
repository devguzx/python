#Variáveis de classe e Váriaveis de instância:

#Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

class Estudante:
    escola = "DIO" #Variável de classe

    def __init__(self, nome, numero): 
        self.nome=nome #Variável de instância
        self.numero=numero #Variável de instância

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"
    
aluno1 = Estudante("Guthierry", 7)
aluno2 = Estudante("Elis Maria", 6)

print(aluno1.__str__())
print(aluno2.__str__())

Estudante.escola = "Alura" #Geral em todos os objetos.

aluno1.numero = 8 #Mudança apena no objeto aluno1.
aluno2.numero = 9 #Mudança apena no objeto aluno2.
print(aluno1.__str__())
print(aluno2.__str__())


