#Aplicação de verificação:
def acesso_administrador(funcao):
    def wrapper(usuario):
        if usuario!="diretor":
            print("Acesso negado! Você não é administrador.")
        else:
            funcao(usuario)
    return wrapper

@acesso_administrador
def acessar(usuario):
    print(f"Acesso validado para {usuario}")

acessar("aluno")
acessar("professor")
acessar("diretor")

#Registrar logs sempre que uma função for chamada:
def registro_logs(funcao):
    def wrapper(*args, **kwargs):
        print(f"Executando função: {funcao.__name__.upper()} com {args} {kwargs} como argumentos.")
        resultado = funcao(*args, **kwargs)
        return resultado
    return wrapper

@registro_logs
def compra(item, valor):
    print(f"Comprou {item} - R${valor:.2f}")

@registro_logs
def venda(item, valor):
    print(f"Vendeu {item} - R${valor:.2f}")

compra("Camisa", 20)
compra("Calça", 30)
venda("Short", 50)


