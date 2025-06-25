#Acesso negado a método privado

class Segredo:
    def __init__(self):
        pass
        

    def tentar_revelar(self):
        self.__mostrar_mensagem()
            

    def __mostrar_mensagem(self):
        print("Segredo revelado")

s = Segredo()
s.__mostrar_mensagem() #observe como o name mangling protege métodos.