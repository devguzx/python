#Conversão de tipos de dados:

preco = 10 #Inteiro
print(preco)
preco=float(preco) #Conversão para float.
print(preco)

idade="25" #String
print(idade)
idade=int(idade) #Conversão para inteiro.
print(idade)

#Exemplo
ano_atual=2025
ano_nascimento=input("Digite seu ano de nascimento: ") #"ano_nascimento" esta com tipo string, pois não houve a conversão ainda.

print(type(ano_nascimento)) #class str
#Caso quisesse fazer alguma operação ia dar erro! Por isso é importante a conversão.

ano_nascimento=int(ano_nascimento) #Convertendo para inteiro.
print(f"Sua idade atual é de {ano_atual-ano_nascimento} anos")
print(type(ano_nascimento)) #class int





