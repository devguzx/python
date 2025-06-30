#Decorador:
import time
def tempo_execucao(funcao):
    def wrapper():
        inicio = time.time()
        funcao()
        fim=time.time()
        print(f"Função {funcao.__name__} executada em {fim-inicio:.4f} segundos")
    return wrapper

@tempo_execucao
def calcular():
    total = 0
    for i in range(1000000):
        total += i
    return total

calcular()
