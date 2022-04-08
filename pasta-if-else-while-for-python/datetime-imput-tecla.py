import datetime

try:
    tecla = input("ditie primeira tecla: ")
    t1 = datetime.datetime.now()
    print(datetime.datetime.now())

    tecla2 = input("digite segunda tecla: ")
    t2 = datetime.datetime.now()
    print(datetime.datetime.now())

    resultado = t2 - t1
    print("tempo que passou foi: ", resultado)
except Exception as e:
    print("Erro", e)