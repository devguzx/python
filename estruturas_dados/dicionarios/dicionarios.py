#Estutura de dados: dicionário (Conjunto não ordenado de pares chave:valor)

idade_clientes={"Matheus":21, "Camila":19, "Guthierry":18, "Elis":18}
print(idade_clientes["Elis"]) #Acessa um valor por meio da chave.
idade_clientes["Jose"]=26 #Adiciona um elemento se não houver.
print(idade_clientes)

#Dicionários aninhados:

dados_clientes={
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"9999-9999"},
    "amanda@gmail.com":{"nome":"Amanda", "telefone":"1111-9999"},
    "fausto@gmail.com":{"nome":"Fausto", "telefone":"9999-1111"},
}
telefone_guilherme=dados_clientes["guilherme@gmail.com"]["telefone"]
print(telefone_guilherme)

for dado in dados_clientes:
    print(f"Dados de {dado} - {dados_clientes[dado]}")

