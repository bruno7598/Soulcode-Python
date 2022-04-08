#CALCULADORA COM MENU
n1 = input("Por favor digite seu nome: \n")
print("-"*20)
print("BEM VINDO",  n1)

print("Para continuar, escolha uma das seguintes opções:\n")
print("-"*20)
while True: 
    start = input("Escolha contas básicas: \n'1'\n"
                "Escholher potências e raízes: \n'2'\n"
                "Sair do programa: \n'3'\n")
    print("-"*20)


#sair do programa

    if start == '3':
        print("ATÉ DAQUI A POUCO!\n")
        exit()


#Contas basicas
    try:
        if start == '1':

            print("CONTAS BÁSICAS: \n")

            primeiro = input("\t Digite o primeiro número:\n ")
            segundo = input("\t Digite o segundo número:\n ")
            operacao = input("\t Digite a operação:\n ")
            
        if operacao == '+':
            resultado = float(primeiro) + float(segundo)
        elif operacao == "-":
            resultado = float(primeiro) - float(segundo)
        elif operacao == "*":
            resultado = float(primeiro) * float(segundo)
        elif operacao == "/":
            resultado = float(primeiro) / float(segundo)
        else:
            print("DEU MOLE DIGITOU ALGUMA MERDA ... VAI ESTUDAR!!!\n ")

        if resultado:
            print("RESULTADO: {0}".format(resultado))
            break
    except Exception as e:
        print("ERRO", e)
            

        continue
  
      
#Raiz quadrada e potência
#     
try:
    if start == '2':
        print("RAIZ E POTÊNCIAÇÃO: \n")
        print("Para prosseguir escolha uma das seguintes opções: ")

    
        while True:
            st = input("Potênciação: \n'1'\n"
                       "Radiação: \n'2'\n"
                       "SAIR: \n'3'\n")

    
            if st == '3':
                print("ATÉ DAQUI A POUCO!!!\n")
                exit()
                break
            
#POTENCIA
            if st == '1':
                print("POTÊNCIAS: \n")
                
                

                a = input("Digite um valor para a: ")
                b = input("Digite um valor para b: ")
                resp = float(a) ** float(b)

                if resp:
                    print("ESULTADO: {0}".format(resp))

                    break 
#RADIACAO            
            if st == '2':
                print("RADIAÇÃO: \n")

            raiz = float(input("Digite um valor: "))
            raiz2 = raiz ** (1/2)
            print("A raiz quadrada é: ",raiz2)
            break
except Exception as e:
    print("ERRO", e)
