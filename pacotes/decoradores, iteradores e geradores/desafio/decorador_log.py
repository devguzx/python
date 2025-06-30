#Implemente um decorador que seja aplicado a todas as funções de transações. Esse decorador deve registrar (printar) a data e a hora de cada transação, bom commo o tipo de transação.

import datetime 
def log_transacoes(funcao):
    def wrapper(*args, **kwargs):
        agora=datetime.datetime.now()
        agora_formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
        resultado=funcao(*args, **kwargs)
        print(f"""========================
              Data e hora: {agora_formatado}
              Tipo de Transação: {funcao.__name__.title()}  
                 ========================= 
            """)
        return resultado
    return wrapper