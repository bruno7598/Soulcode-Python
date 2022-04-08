try:
    idade = -3
    if 0 < idade < 18:
        print("Menor de idade")
    elif 18 <= idade < 60:
        print("Maior de idade")
    elif 60 <= idade < 120:
        print("Idoso")
    else:
        print("ERRO valor: ", idade)
except Exception as e:
    print("Erro", str(e))