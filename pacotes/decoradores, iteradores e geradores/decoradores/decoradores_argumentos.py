#Decoradores com argumentos

#Podemos usar *args (lista de argumentos) e **kwargs (n argumentos com chave e valor) na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chave.

#Exemplo:
def duplicar(funcao):
    def funcao_duplicada(*args, **kwargs):
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    return funcao_duplicada

@duplicar
def apresentacao(nome,tecnologia):
    print(f"Ola meu nome é {nome} e estudo a tecnologia {tecnologia}.")

apresentacao("Guthy", "Python")

#Exemplo:
import functools

def duplicar(funcao):
    @functools.wraps(funcao)  #Correção de instrospecção(preserva nome e docstring da função original)

    def nova_funcao(*args, **kwargs):
        print("faz algo antes")
        resultado= funcao(*args, **kwargs)
        print("Faz algo depois")
        return resultado
    return nova_funcao

@duplicar
def apresentacao(nome,tecnologia):
    print(f"Ola meu nome é {nome} e estudo a tecnologia {tecnologia}.")
    return tecnologia.upper()
    
tecnologia=apresentacao("Elis", "java")
print(tecnologia)
print(apresentacao.__name__)

#Exemplo:
def meu_decorador(funcao):
    def nova_funcao(*args, **kwargs):
        print("Chamando função:", funcao.__name__)
        resultado = funcao(*args, **kwargs)
        print("Função executada.")
        return resultado
    return nova_funcao

def somar(a, b):
    return a + b

print(somar(5, 7))
