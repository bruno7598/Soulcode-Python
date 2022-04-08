
operacao = input("Digite a operacao desejada (+, -, *, /, raiz, **): ")
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

try:
    if operacao == "+":
	    resultado = float(numero1) + float(numero2)
    
    elif operacao == "-":
	    resultado = float(numero1) - float(numero2)
    
    elif operacao == "*":
	    resultado = float(numero1) * float(numero2)
   
    elif operacao == "/":
	    resultado = float(numero1) / float(numero2)
    
    elif operacao == "raiz":
        resultado = float(numero1)**(1/2)
    
    elif operacao == "**":
        resultado = float(numero1)**float(numero2)
    
    print("{} {} {} é igual a {}" .format(numero1, operacao, numero2, resultado))
except Exception as e:
    print("Erro", e)