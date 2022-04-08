import datetime

tecla = input("Aperte qualquer tecla: ")
try:

    
    if tecla:
        t1 = datetime.datetime.now()
        tecla2 = input("Aperte qualquer tecla pra encerrar: ")
        if tecla2:
            t2 = datetime.datetime.now()
    resultado = t2 - t1 
    print("O tempo que passou foi: ", resultado)   



except Exception as e:
    print("Erro", e)