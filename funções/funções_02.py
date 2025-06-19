#Função Recursiva: Função que chama a si mesma para resolver um problema. (Analogia:boneca russa)

#Partes Fundamentais:
#- Caso Base: condição que encerra a recursão (impede o loop infinito).
#- Chamada recursiva: onde a função se chama, reduzindo o problema.

#Vantagens: código mais simples e elegante e solução natural para problemas que têm natureza recursiva.
#Desvantagens: consome muita memória e risco de stack overflow (estouro de pilhas).

#Exemplos: Fatorial
def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(4))

#Exemplos: Fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(12):
    print(fibonacci(i), end=" ")
print()

#Exemplos: MDC
def mdc(a, b):
    if b==0:
        return a
    else:
        return mdc(b, a%b)

print(mdc(48,12))

#Exemplo: Contagem regressiva
def contagem_regressiva(n):
    if n==0:
        return "FIM"
    else:
        print(n)
        return contagem_regressiva(n-1)
print(contagem_regressiva(5))

#Exemplo: Exponenciação
def exponeciacao(b,e):
    if e==0:
        return 1
    else:
        return b * exponeciacao(b,e-1) 
print(exponeciacao(10,3))

#Desafio: exponenciação com expoente negativo
def expo_neg(base, expoente):
    if expoente==0:
        return 1
    else:
        return (1/base) * expo_neg(base,expoente+1)
print(expo_neg(10, -2))