#Gerador:
def gerar_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for valor in gerar_fibonacci(6):
    print(valor)