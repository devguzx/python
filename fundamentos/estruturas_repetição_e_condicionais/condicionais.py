#Estruturas Condicionais:

#if - "se"
#elif - "senao se"
#else - "senao"

#exemplo: imc
def calcular_imc(peso,altura):
    imc=peso/(altura**2)

    if imc<18.5:
        print(f"IMC = {imc:.2f} | Classificação = MAGREZA | Obesidade(grau)= 0")
    elif 18.5<=imc<25.0:
        print(f"IMC = {imc:.2f} | Classificação = NORMAL | Obesidade(grau)= 0")
    elif 25.0<=imc<30:
        print(f"IMC = {imc:.2f} | Classificação = SOBREPESO | Obesidade(grau)= 1")
    elif 30.0<=imc<40.0:
        print(f"IMC = {imc:.2f} | Classificação = OBESIDADE | Obesidade(grau)= 2")
    else:
        print(f"IMC = {imc:.2f} | Classificação = OBESIDADE GRAVE | Obesidade(grau)= 3")

try:

    peso_teste=float(input("Digite seu peso em kg (ex:70):"))
    altura_teste=float(input("Digite sua altura em metros (ex:1.70):"))
    calcular_imc(peso_teste,altura_teste)

except ValueError:
    print("Por favor, respeite as convenções!")

#If ternário:

saque=float(input("Valor do saque: "))
saldo=1000

status= "Sucesso" if saldo>=saque else "Falha"

print(f"{status} ao realizar o saque!")