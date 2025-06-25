#Exercício 01: Cadastro de clientes.

qtd_cadastro=int(input("Digite a quantidade de cadastros: "))


cadastros=[]
for i in range(qtd_cadastro):
    cadastro_pessoa={}
    nome=input("Informe o nome da pessoa que deseja cadastrar: ").strip()
    idade=int(input("Informe a idade da pessoa que deseja cadastrar: "))

    cadastro_pessoa["nome"]=nome
    cadastro_pessoa["idade"]=idade

    print(f"\nCidadão cadastrado: {cadastro_pessoa}\n")

    cadastros.append(cadastro_pessoa)

#Todos os cadastros
print(f"Lista completa de cadastros: {cadastros}\n")


#Clientes maiores de 18:
clientes_maiores_18=[]
for cadastro in cadastros:
    if cadastro["idade"]>=18:
        clientes_maiores_18.append(cadastro["nome"])
print(f"Pessoas maiores de 18 anos cadastradas: {", ".join(clientes_maiores_18)}.\n")


#Pessoa mais velha e mais nova:
idades = [pessoa["idade"] for pessoa in cadastros]
idade_min = min(idades)
idade_max = max(idades)

mais_novos = [pessoa["nome"] for pessoa in cadastros if pessoa["idade"]  == idade_min]
mais_velhos = [pessoa["nome"] for pessoa in cadastros if pessoa["idade"]  == idade_max]

print(f"""
Cliente(s) mais novo(s) com {idade_min} anos: {', '.join(mais_novos)}.
Cliente(s) mais velho(s) com {idade_max} anos: {', '.join(mais_velhos)}.
""")








    