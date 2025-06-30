#Decoradores em python: função que recebe outra função como argumento e retorna uma nova função.

#Um decorador serve para adicionar ou modificar o comportamneto de uma função ou método, sem alterar seu código original.

#Exemplo: 
def meu_decorador(funcao):
    def nova_funcao():
        print("Antes da execução da função.")
        funcao()
        print("Depois da execcução da função")

    return nova_funcao

def saudacao():
    print("Ola mundo")

saudacao = meu_decorador(saudacao)
saudacao()

#Sintaxe açúcar (sugar syntax):
@meu_decorador
def saudacao():
    print("Ola mundo")  
saudacao()



