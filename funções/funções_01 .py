# Funções: bloco de código que pode ser reutilizado no decorrer do programa.
# Usar funções torna o código mais limpo e possibilita o reaproveitamento de código. 
# Programar baseado em funções significa que estamos programando de maneira estruturada.

#Exemplo: saudação
def saudacao(name):
    print(f"Hello {name}, seja bem-vindo(a)")
saudacao("Guthy")

#Retornando valores
#Exemplo: soma números
def soma(*num):
    valor_soma=sum(num)
    return valor_soma

print(soma(2,4,5,6,7,8,9))
print(soma(3,4,-5))

#Exemplo: antecessor e sucessor
def ant_suc(valor):
    antecessor=valor-1
    sucessor=valor+1
    return antecessor, sucessor

antecessor_sucessor=ant_suc(8)
antecessor=antecessor_sucessor[0]
sucessor=antecessor_sucessor[1]
print(f"Antecessor: {antecessor}. Sucessor: {sucessor}.")

#Escopo local: Dentro da função
#Escopo global: Todo o código
