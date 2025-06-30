#Geradores: Tpio especial de função que mantém o estado da execução entre as chamadas. Ele produz valores sob demanda com a palavra chave "yield".

#Eles economizam memória porque não armazenam todos os valores em memória de uma vez, ao contrário de listas.

#Caracteristicas: 
#1- Se um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.
#2- O estado interno é mantido entre chamadas
#3- A execução é pausada na declaração "yield" e retomada na próxima vez que le for chamado.

#Exemplo: 
def gerador_exemplo():
    yield 1
    yield 2
    yield 3
    yield 4

for valor in gerador_exemplo():
    print(valor)

#Exemplo com lógica
def contar_ate(n):
    i=0
    while i<=n:
        yield i   #Gera um número enquanto i<=n
        i+=1

for num in contar_ate(10):
    print(num)


#Gerador x Função:
def funcao_normal(n):
    return list(range(n))  #Ocupa mais memória
print(funcao_normal(10))

def gerador(n):
    for i in range(n):
        yield i       #Mais eficiente gera um item po r vez
for num in gerador(10):
    print(num)