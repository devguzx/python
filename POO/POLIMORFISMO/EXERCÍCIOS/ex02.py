#Exercício 02:

class Funcionario:
    def __init__(self,nome):
        self.nome=nome

    def calcular_pagamento(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class FuncionarioHorista(Funcionario):
    def __init__(self,nome,horas_trabalhadas):
        super().__init__(nome)
        self.horas_trabalhadas=horas_trabalhadas

    def calcular_pagamento(self):
        salario = self.horas_trabalhadas*10
        print(f"Salario por hora do funcionário {self.nome} = R${salario:.2f}")

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome , salario_mensal):
        super().__init__(nome)
        self.salario_mensal=salario_mensal

    def calcular_pagamento(self): 
        print(f"Salario mensal do funcionário {self.nome} = R${self.salario_mensal:.2f}")

funcionarios = [FuncionarioHorista("Glauber",6),
                FuncionarioMensalista("Gerson",1200),
                FuncionarioHorista("Guthy",10),
                FuncionarioMensalista("Lara",1400)
                ]

for funcionario in funcionarios:
    funcionario.calcular_pagamento()