try:
    peso = 20
    altura = 1.85
    IMC = (peso)/(altura**2)
    if 15 < IMC <= 18.5:
        print("Abaixo do peso ", IMC)
    elif 18.6 < IMC < 25:
        print("Peso Normal", IMC)
    elif 25 <= IMC < 30:
        print("SOBREPESO", IMC)
    elif 30 <= IMC < 35:
        print("Obesidade Grau I", IMC)
    elif 35 <= IMC <= 39.9:
        print("Obesidade Grau II", IMC)
    elif IMC >= 40:
        print("Morbida !!!", IMC)
    else:
        print("Morreu provavelmente !", IMC)
except Exception as e:
    print("Erro", str(e))