#Utilizando f strings: forma de formatação mais utilizada.
#Exemplo: Saudação
def saudacao(nome):
    print(f"Bem-Vindo(a) {nome}, essa jornada em python vai ser incrivel!")
saudacao("Guthierry")

#Exemplo: Nome, idade e curso
nome=input("Digite seu nome:")
idade=int(input("Qual a sua idade?"))
curso=input("Qual curso superior vc faz?")

print(f"Ola, me chamo {nome}, tenho {idade} anos e estudo {curso}.")

#Formatação
PI = 3.14159
print(f"O valor de PI é {PI:.2f}.")

porcent=20/100
print(f"20/100 é igual a {porcent:.2%}.")