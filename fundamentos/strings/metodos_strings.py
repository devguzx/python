#Métodos úteis da classe string:

string = "PyThOn"

print(string.upper()) #Maiuscula
print(string.lower()) #Minuscula
print(string.title()) #Título(Primeira letra maiuscula, restante minuscula.)

string1 = " Meu nome é Guthy        "
print(string1.strip()) #Remove os espaços em branco(Começo e fim)
print(string1.strip().center(20,"#")) #Centralizar
posicao=string1.find("G")#Encontrar posição de um caractere específico.Função .find()
print(posicao)
