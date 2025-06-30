#Imagine que você quer:

#- Verificar se o usuário é admin
#- Medir tempo de execução
#- Mostrar um log de execução


import time
import functools

def dados_funcoes(funcao):
    @functools.wraps(funcao)
    def wrapper(usuario):
        if usuario!="admin":
            print("Não é possível salvar dados")
        else:
            inicio = time.time()
            print(f"Executando função: {funcao.__name__}")
            funcao(usuario)
            fim = time.time()
            print(f"{funcao.__name__} foi executada em {fim-inicio:.4f} segundos")
    return wrapper

@dados_funcoes
def salvar_dados(usuario):
    print("Salvando dados para adiministrador.")

salvar_dados("admin")
salvar_dados("funcionario")