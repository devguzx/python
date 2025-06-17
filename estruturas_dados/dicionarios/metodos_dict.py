#Métodos dicionários:

#Método get:
dados_clientes={
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"9999-9999"},
    "amanda@gmail.com":{"nome":"Amanda", "telefone":"1111-9999"},
    "fausto@gmail.com":{"nome":"Fausto", "telefone":"9999-1111"},
}
print(dados_clientes.get("guilherme@gmail.com"))
print(dados_clientes.get("falso@gmail.com",0))


#Método items
dado_cliente1={ "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"9999-9999"}}
print(dado_cliente1.items()) #Retorna uma tupla

#Método keys
print(dado_cliente1["guilherme@gmail.com"].keys())

#Método values
print(dado_cliente1["guilherme@gmail.com"].values())

#Método setdefault
dado_cliente1.setdefault("Idade", "23")
print(dado_cliente1)