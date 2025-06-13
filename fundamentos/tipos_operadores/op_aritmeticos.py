#Operadores Aritméticos: 
#Precedência - Mesmas regras da matemática
a=15
b=10

print(a+b)#adição

print(a-b)#subtração

print(a*b)#multiplicação

print(a/b)#divisão

print(a//b)#divisão_inteira

print(a**b)#potencia

print(a%b)#modulo = resto

#Exemplo de uso: calculadora simples 
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Qual operação deseja realizar (+, -, *, /)? ")

    if operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1 - num2)
    elif operacao == "*":
        print(num1 * num2)
    elif operacao == "/":
        if num2 == 0:
            print("Inválido - Divisão por 0")
        else:
            print(num1 / num2)
    else:
        print("Operação inválida!")

except ValueError:
    print("Você digitou um valor inválido.")


