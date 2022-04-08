# -*- Sempre funciona -*-
#
#
# -*- CALCULADORA PLAY
#


print("\t FRRE CALCULATOR!!!\n ")

continuar = input(" \t Por favor digite seu nome: \n")

print("\t BEM VINDO",continuar)

print(" \t Para continuar, escolha uma das seguintes opções:\n")

while True:
    start = input("Para contas básicas: \n'1'\n"
                  "Para circulos: \n'2'\n"
                  "Para equação de segundo grau: \n'3'\n"
                  "Para potências e raízes: \n'4'\n"
                  "Para conversor de unidade: \n'5'\n"
                  "Para geometria: \n'6'\n"
                  "Para função: \n'7'\n"
                  "Para velocidade média: \n'8'\n"
                  "Para sair do programa: \n'n'\n")





    if start == 'n':
        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
        exit()


        

    if start == '1':

        print("\t CONTAS BÁSICAS: \n")

        import math

        primeiro = input("\t Digite o primeiro número:\n ")
        segundo = input("\t Digite o segundo número:\n ")
        operacao = input("\t Digite a operação:\n ")

        resultado = None
        if operacao == '+':
            resultado = float(primeiro) + float(segundo)
        elif operacao == "-":
            resultado = float(primeiro) - float(segundo)
        elif operacao == "*":
            resultado = float(primeiro) * float(segundo)
        elif operacao == "/":
            resultado = float(primeiro) / float(segundo)
        else:
            print("\t IMPOPSSÍVEL REALIZAR A OPERAÇÃO!!!\n ")

        if resultado:
            print("\t RESULTADO: {0}".format(resultado))

            break

        continue
        
        


            #
            #Fim do programa
            #
            

    if start == '2':
        print("\t CIRCULOS: \n")


        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPÇÕES: \n")

        a = input("ÁREA DO CIRCULO ----> \n'1'\n"
                  "COMPRIMENTO DO CIRCULO ----> \n'2'\n"
                  "SAIR ----> \n'n'\n")


        if a == 'n':
            print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")

            exit()


        if a == '1':
            print("\t ÁREA DO CIRCULO: \n")

            import math

            pi = 3.14

            r = input("DIGITE O VALOR DO RAIO: ")

            resp = (float(r) * float(r)) * pi

            print("\t A ÁREA DO CIRCULO É:",resp,"\n")

            break


        if a == '2':
            print("\t COMPRIMENTO DO CIRCULO: \n")

            import math


            pi = 3.14

            r = input("DIGITE O VALOR DO RAIO: ")

            resp = (float(r) * 2) * pi

            print("\t O COMPRIMENTO DO CIRCULO É:",resp,"\n")


            break


        else:
            print("\t CARACTERE INVÁLIDO!!!\n")

            continue



        































    if start == '3':

        print("\t EQUAÇÃOD DE SEGUNDO GRAU: \n")
        import math

        a = int(input("Digite um valor para a: "))
        b = int(input("Digite um valor para b: "))
        c = int(input("Digite um valor para c: "))

        delta = b*b - 4 * a * c

        if delta < 0:
             print("\t ESTA OPERAÇÃO NÃO POSSUÍ RAÍZES REAIS\n ")
        elif delta == 0:
            raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
            print("\t A EQUAÇÃO POSSUÍ APENAS UMA RAIZ REAL",raiz)
        elif delta > 0:
            raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-1 * b - math.sqrt(delta)) / (2 *a)
            print("\t  AS RAÍZES DA EQUAÇÃO SÃO:",raiz1, "E",raiz2)

            break










    if start == '4':
        print("\t RADIAÇÃO E POTÊNCIAÇÃO: \n")
        print("Para prosseguir escolha uma das seguintes opções: ")


        
        while True:
            st = input("Potênciação: \n'1'\n"
                       "Radiação: \n'2'\n"
                       "SAIR: \n'n'\n")


            if st == 'n':
                print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                exit()


                break
            

            if st == '1':
                print("\t POTÊNCIAS: \n")
                

                import math
                

                a = input("Digite um valor para a: ")
                b = input("Digite um valor para b: ")
                

                resp = None
                
        
                resp = float(a) ** float(b)

                if resp:
                    print("\t RESULTADO: {0}".format(resp))

                    break

                      


        

            if st == '2':
                print("\t RADIAÇÃO: \n")

            import math

            raiz = float(input("Digite um valor: "))
            radical = float(input("Digite o radical: "))

            if radical == '2':
                raiz2 = raiz ** (1/2)
                print("A raiz quadrada é:",raiz2)


            if radical == '3':
                raiz3 = raiz ** (1/3)
                print("A raiz cúbica é:",raiz3)

            else:
                print("\t CARACTERE INVÁLIDO!!!\n")











    if start == '6':
        print("\t CONVERSSOR DE UNIDADE: \n")
        print("Para prosseguir escolha uma das seguintes opções: ")

        while True:
            un = input("Comprimento: \n'1'\n"
                       "Área: \n'2'\n"
                       "Temperatura: \n'3'\n"
                       "Volume: \n'4'\n"
                       "Massa: \n'5'\n"
                       "Dados: \n'6'\n"
                       "SAIR: \n'n'\n")


            if un == 'n':
                print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                exit()

                break


            if un == '1':
                print("\t COMPRIMENTO: \n")

                print("Para prosseguir, escolha uma das opções abaixo: ")

                while True:
                    a = input("M ----> Cm: \n'1'\n"
                              "M ----> Mm: \n'2'\n"
                              "Cm ----> M: \n'3'\n"
                              "Cm ----> mm: \n'4'\n"
                              "Mm ----> M: \n'5'\n"
                              "Mm ----> Cm: \n'6'\n"
                              "SAIR: \n'n'\n")


                    if a == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()


                        break

                    if a == '1':
                        print("\t M ----> CM\n")

                        import math

                        v1 = input("Digite o comprimento inicial: ")

                
                        
                            
                        resp = float(v1) * (100)
                        print(" O COMPRIMENTO É:",resp)




                        break

                    if a == '2':
                        print("\t M ----> MM\n")

                        import math

                        v1 = input("Digite o comprimento inicial: ")



                        
                        resp = float(v1) * 10000
                        print("O COMPRIMENTO É:",resp)


                        break


                    if a == '3':
                        print("\t CM ----> M\n")

                        import math

                        v1 = input("Digite o comprimento em centímetros: ")



                        
                        resp = float(v1) / 100
                        print("O COMPRIMENTO É:",resp)


                        break


                    if a == '4':
                        print("\t CM ----> MM\n")

                        import math

                        v1 = input("Digite o comprimento em centímetros: ")



                        
                        resp = float(v1) * 100
                        print("O COMPRIMENTO É:",resp)


                        break

                    if a == '5':
                        print("\t MM ----> M\n")

                        import math

                        v1 = input("Digite o comprimento em milímetros: ")


                        
                        resp = float(v1) / 10000
                        print(" COMPRIMENTO É:",resp)


                        break


                    if a == '6':
                        print("\t MM ----> CM\n")

                        import math

                        v1 = input("Digite o comprimento em milímetros: ")



                        
                        resp = float(v1) / 100
                        print("O COMPRIMENTO É:",resp)

                        break



            if un == '2':
                print("\t ÁREA: \n")

                print("Para prosseguir, escolha uma das opções abaixo: ")

                while True:
                    b = input("Área do quadrado: \n'q'\n"
                              "Área do retângulo: \n'r'\n"
                              "Área do triângulo: \n't'\n"
                              "Área do trapézio: \n'tp'\n"
                              "SAIR: \n'n'\n")


                    if b == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()

                        break


                    if b == 'q':
                        print("\t ÁREA DO QUADRADO: \n")

                        import math

                        a = input("Digite um dos lados do quadrado: ")


                        resp = float(a) * float(a)
                        print("A ÁREA DO QUADRADO É:",resp)


                        break



                    if b == 'r':
                        print("\t ÁREA DO RETÂNGULO: ")

                        import math

                        a = input("Digite o lado a do retângulo: ")
                        b = input("Digite o lado b do retângulo: ")

                        resp = float(a) * float(b)
                        print("A ÁREA DO RETÂNGULO É:",resp)


                        break


                    if b == 't':
                        print("\t ÁREA DO TRIÂNGULO: \n")

                        import math

                        a = input("Digite o valor da basa do triângulo: ")
                        b = input("Digite o valor da altura do triângulo: ")

                        resp = (float(a) * float(b)) / 2
                        print("A ÁREA DO TRIÂNGULO É:",resp)


                        break


                    if b == 'tp':
                        print("\t ÁREA DO TRAPÉZIO: \n")

                        import math

                        a = input("Digite o valor da base do trapézio: ")
                        b = input("Digite o valor da parte superior do trapézio: ")
                        h = input("Digite o valor da altura do trapézio: ")

                        resp = (float(a) + float(b) * float(h)) / 2
                        print("A ÁREA DO TRAPÉZIO É:",resp)


                        break


                    break


            if un == '3':
                print("\t CONVERSOR DE TEMPERATURA: \n")

                print("Para prosseguir, escolha uma das opções: ")

                while True:
                    t = input("º Celsius ----> ºFahrenheit: \n'1'\n"
                              "º Celsius ----> Kelvin: \n'2'\n"
                              "º Fahrenheit ----> º Celsius: \n'3'\n"
                              "º Fahrenheit ----> Kelvin: \n'4'\n"
                              "Kelvin ----> º Celsius: \n'5'\n"
                              "Kelvin ----> º Fahrenheit: \n'6'\n"
                              "SAIR: \n'n'\n")


                    if t == 'n':
                        print(" \t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()


                        break


                    if t == '1':
                        print("\t ºCELSIUS ----> ºFAHRENHEIT: \n")

                        import math

                        a = input("Digite a temperatura me graus celsius: ")

                        resp1 = float(a) * 9
                        
                        resp = ( float(resp1) + 160) / 5
                        print("A TEMPERATURA EM ºF É:",resp)


                        break


                    if t == '2':
                        print("\t CELSIUS ----> KELVIN: \n")

                        import math

                        a = input("Digite a temperatura em graus celsius: ")

                        resp = float(a) + 273
                        print("A TEMPERATURA EM K É:",resp)


                        break


                    if t == '3':
                        print("\t FAHRENHEIT ----> CELSIUS: \n")

                        import math

                        a = input("Digite a temperatura em graus fahrenheit: ")

                        resp1 = float(a) * 5

                        resp = (float(resp1) - 160) / 9
                        print("A TEMPERATURA EM ºC É:",resp)


                        break


                    if t == '4':
                        print("\t FAHRENHEIT ----> KELVIN: \n")

                        import math

                        a = input("Digite a temperatura em fahrenheit: ")

                        resp1 = float(a) + 459.67

                        resp = float(resp1) / 1.8
                        print("A TEMPERATURA EM K É:",resp)


                        break


                    if t == '5':
                        print("\t KELVIN ----> CELSIUS: \n")

                        import math

                        a = input("Digite a temperatura em kelvin: ")

                        resp = float(a) - 273
                        print(" A TEMPERETURA EM ºC É:",resp)


                        break


                    if t == '6':
                        print("\t KELVIN ----> FAHRENHEIT: \n")

                        import math

                        a = input("Digite a temperatura em kelvin: ")

                        resp1 = float(a) * 1.8

                        resp = float(resp1) - 459.67
                        print("A TEMPERATURA EM ºF É:",resp)


                        break


            if un == '4':
                print("\t CONVERSOR DE VOLUME: \n")

                print("Para prosseguir, escolha uma das opções: ")

                while True:
                    v = input("Litro ----> mililitro: \n'1'\n"
                              "Litro ----> Metro cúbico: \n'2'\n"
                              "Litro ----> Centímetro cúbico: \n'3'\n"
                              "Mililitro ----> Litro: \n'4'\n"
                              "SAIR: \n'n'\n")



                    if v == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()



                    if v == '1':
                        print("\t LITRO ----> MILILITRO: \n")

                        a = input("Digite o volume em litros:")

                        resp = float(a) * 1000
                        print("O VOLUME EM ML É:",resp)


                        break


                    if v == '2':
                        print("\t LITRO ----> METRO CÚBICO:\n")

                        a = input("Digite o volume em litros: ")

                        resp = float(a) / 1000
                        print("O VOLUME EM M³ É:",resp)


                        break


                    if v == '3':
                        print("\tLITRO ----> CENTÍMETRO CÚBICO: \n")

                        a = input("Digite o volume em litros: ")

                        resp = float(a) * 1000
                        print("O VOLUME EM CM³ É:",resp)


                        break


                    if v == '4':
                        print("\tMILILITRO ----> LITRO: \n")

                        a = input("DIgite o volume em mililitros: ")

                        resp = float(a) / 1000
                        print("O VOLUME EM L É:",resp)


                        break



            if un == '5':
                print("\t MASSA: \n")

                print("Para prosseguir, escolha umas das opções: ")

                while True:
                    a = input("TONELADAS ----> KG: \n'1'\n"
                              "TONELADAS ----> G: \n'2'\n"
                              "TONELADAS ----> MG: \n'3'\n"
                              "QUILOGRAMAS ----> T: \n'4'\n"
                              "QUILOGRAMAS ----> G: \n'5'\n"
                              "QUILOGRAMAS ----> MG: \n'6'\n"
                              "GRAMAS ----> T: \n'7'\n"
                              "GRAMAS ----> KG: \n'8'\n"
                              "GRAMAS ----> MG: \n'9'\n"
                              "SAIR: \n'n'\n")


                    if a == 'n':
                        a
                        print("\tOBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()
                        break


                    




                    

                    if a == '1':
                        print("\t TONELADA ----> KG:\n")
                        
                        c = input("Digite o valor a ser convertido: ")

                        resp = float(c) * 1000
                        print("A MASSA EM KG É:",resp)
                        break

                        

                    if a == '2':
                        print("\t TONELADA ----> G: \n")
                        
                        c = input("Digite o valor a ser convertido: ")

                        resp = float(c) * 1000000
                        print("A MASSA EM G É:",resp)
                        break


                    if a == '3':
                        print("\t TONELADA ----> MG: \n")
                        
                        c = input("Digite o valor a ser convertido: ")

                        resp = float(c) * 1000000000
                        print("A MASSA EM MG É:",resp)
                        break



                    if a == '4':
                        print("\t QUILOGRAMAS ----> T: \n")
                        
                        c = input("Digite o valor a ser convertido: ")

                        resp = float(c) / 1000
                        print("A MASSA EM T É:",resp)
                        break


                    if a == '5':
                        print("\t QUILOGRAMAS ----> G: \n")
                        
                        c = input("Digite o valor a ser convertido: ")

                        resp = float(c) * 1000
                        print(" A MASSA EM G É:",resp)
                        break


                    if a == '6':
                        print("\t QUILOGRAMAS ----> MG: \n")
                        
                        c= input("Digite o valor a ser convertido: ")

                        resp = float(c) * 1000000
                        print("A MASSA EM MG É:",resp)
                        break



                    if a == '7':
                        print("\t GRAMAS ----> T: \n")
                        
                        c= input("Digite o valor a ser convertido: ")

                        resp = float(c) / 1000000
                        print("A MASSA EM T É:",resp)
                        break


                    if a == '8':
                        print("\t GRAMAS ----> KG: \n")
                        
                        c = input("Diigte o valor a ser convertido: ")

                        resp = float(c) / 1000
                        print("A MASSA EM KG É:",resp)
                        break


                    if a == '9':
                        print("\t GRAMAS ----> MG: \n")
                        
                        c = input("Digite o valor a ser convertido: ")

                        resp = float(c) * 1000
                        print("A MASSA EM MG É:",resp)
                        break


            if un == '6':
                print("\t DADOS: \n")

                print("Para prosseguir, esoclha uma das seguintes opções: ")

                while True:
                    d = input("BIT ----> BYTE: \n'1'\n"
                              "BYTE ----> MEGABYTE: \n'2'\n"
                              "BYTE ----> GIGABYTE: \n'3'\n"
                              "MEGABYTE ----> BITE: \n'4'\n"
                              "MEGABYTE ----> GIGABYTE: \n'5'\n"
                              "MEGABYTE ----> TERABYTE: \n'6'\n"
                              "GIGABYTE ----> BYTE: \n'7'\n"
                              "GIGABYTE ----> MEGABYTE: \n'8'\n"
                              "GIGABYTE ----> TERABYTE: \n'9'\n"
                              "TERABYTE ----> MEGABYTE: \n'10'\n"
                              "TERABYTE ----> GIGABYTE: \n'11'\n"
                              "SAIR: \n'n'\n")


                    if d == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()
                        break


                    if d == '1':
                        print("\t BIT ----> BYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: \n")

                        resp = float(a) * 0.125 

                        print("OS DADOS EM BYTES SÃO:",resp)
                        break


                    if d == '2':
                        print("\t BYTE ----> MEGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: \n")

                        resp = float(a) * 1000000

                        print("OS DADOS EM MEGABYTE SÃO:",resp)
                        break


                    if d == '3':
                        print("\t BYTE ----> GIGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: \n")

                        resp = float(a) * 125000000

                        print("OS DADOS EM GIGABYTES SÃO:",resp)
                        break


                    if d == '4':
                        print('\t MEGABYTE ----> BYTE: \n')

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) / 100000
                        print("OS DADOS EM BYTES SÃO: ",resp)
                        break


                    if d == '5':
                        print("\t MEGABYTE ----> GIGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) / 0.008
                        print("OS DADOS EM GIGABYTES SÃO:",resp)
                        break


                    if d == '6':
                        print("\t MEGABYTE ----> TERABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) / 0.000000125

                        print("OS DADOS EM TERABYTE SÃO:",resp)
                        break


                    if d == '7':
                        print("\t GIGABYTE ----> BYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) * 125000000

                        print("OS DADOS EM BYTES SÃO:",resp)
                        break


                    if d == '8':
                        print("\t GIGABYTE ----> MEGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) * 1000

                        print("OS DADOS EM MEGABYTES SÃO:",resp)
                        break


                    if d == '9':
                        print("\t GIGABYTE ----> TERABYTE: \n")

                        a = input('DIGITE O VALOR A SER CONVERTIDO: \n')

                        resp = float(a) / 0.000125

                        print("OS DADOS EM TERABYTES SÃO:",resp)
                        break





                    if d == '11':
                        print("\t TERABYTE ----> MEGABYTE: \n")

                        a = input("DIGITE O VALOR A SER CONVERTIDO: ")

                        resp = float(a) * 1000000

                        print("OS DADOS EM MEGABYTES SÃO:",resp)
                        break


                    if d == '12':
                        print('\t TERABYTE ----> GIGABYTE: \n')

                        a = input('DIGITE O VALOR A SER CONVERTIDO: ')

                        resp = float(a) * 1000

                        print("OS DADOS EM GIGABYTES SÃO:",resp)
                        break


                    else:
                        print("\t CARACTERE INVÁLIDO!!!\n")

                        break


            break


        break


    if start == '7':
        print("\t GEOMETRIA: \n")

        print("PARA PROSSEGUIR, ESCOLHA UMAS DAS SEGUINTES OPÇÕES: \n")

        g = input("TEOREMA DE PITÁGORAS: \n'1'\n"
                  "SENO, COSSENO E TANGENTE: \n'2'\n"
                  "ÁREAS: \n'3'\n"
                  "PERÍMETRO: \n'4'\n"
                  "SEMELHANÇA ENTRE TRIÂNGULOS: \n'5'\n"
                  "SAIR: \n'n'\n")


        if g == 'n':
            print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
            exit()


            break

        if g == '1':
            import math
            
            print("\t TEOREMA DE PITÁGORAS: \n")

            a = float(input("DIGITEO VALOR DO CATETO 1: "))
            b = float(input("DIGITE O VALOR DO CATETO 2: "))

            resp = math.sqrt((a*a)+(b*b))

            print("O VALOR DA HIPOTENUSA É:",resp)
            break


        if g == '2':
            import math

            print("\t SENO, COSSENO E TANGENTE: \n")







            break


        if g == '3':
            print("\t ÁREAS: \n")

            print("PARA PROSSEGUIR, ESCOLHA UMA DAS SEGUINTES OPÇÕES: ")

            o = input("ÁREA DO QUADRADO ----> \n'1'\n"
                      "ÁREA DO RETÂNGULO ----> \n'2'\n"
                      "ÁREA DO TRIÂNGULO ----> \n'3'\n"
                      "ÁREA DO TRAPÉZIO ----> \n'4'\n"
                      "ÁREA DO CUBO ----> \n'5'\n"
                      "SAIR ----> \n'n'\n")


            if o == 'n':
                print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                exit()


                break


            if o == '1':
                print("\t ÁREA DO QUADRADO: \n")

                a = input("DIGITE O VALOR DE UM DOS LADOS DO QUADRADO: ")

                resp = float(a) * float(a)

                print("A ÁREA DO QUADRADO É:",resp)

                while True:
                    a = input("\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE \n'N'\n PARA SAIR\n")

                    if a == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()
                        break


                    elif a:
                        print("\t CARACTERE INVÁLIDO!!\n")
                        continue


                    break


            if o == '2':
                print("\t ÁREA DO RETÂNGULO: \n")

                a = input("DIGITE O VALOR DA BASE DO RETÂNGULO: ")
                b = input("DIGITE O VALOR DO LADO DO TRIÂNGULO: ")

                resp = float(a) * float(b)

                print("A ÁREA DO RETÂNGULO É:",resp)

                while True:
                    a = input("\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE \n'N'\n PARA SAIR\n")

                    if a == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()

                    elif a:
                        print('\t CARACTERE INVÁLIDO!!!\n')
                        continue


                    break


            if o == '3':
                print("\t ÁREA DO TRIÂNGULO: \n")

                a = input("DIGITE O VALOR DA BASE DO TRIÂNGULO: ")
                b = input("DIGITE O VALOR DA ALTURA DO TRIÂNGULO: ")

                resp = (float(a) * float(b)) / 2

                print("A ÁREA DO TRIÂNGULO É:",resp)

                while True:
                    a = input("\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE \n'N'\n PARA SAIR\n")

                    if a == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()

                    elif a:
                        print ("\t CARACTERE INVÁLIDO!!!\n")
                        continue


                    break


            if o == '4':
                print("\t ÁREA DO TRAPÉZIO: \n")

                a = input("DIGITE O VALOR DA BASE MAIOR DO TRAPÉZIO: ")
                b = input("DIGITE O VALOR DA BASE MENOR DO TRAPÉZIO: ")
                c = input("DIGITE O VALOR DA ALTURA DO TRAPÉZIO: ")
                

                resp = ((float(a) + float(b)) * float(c)) / 2

                print("A ÁREA DO TRAPÉZIO É:",resp)

                while True:
                    a = input("\t GOSTARIA DE SAIR DO PROGRAMA? PRESSIONE \n'N'\n PARA SAIR\n")

                    if a == 'n':
                        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
                        exit()


                    elif a:
                        print("\t CARACTERE INVÁLIDO!!!\n")

                        continue


                    break

                


            if o == '5':
                print("\t ÁREA DO CUBO: \n")

                a = input("DIGITE O VALOR DO LADO DO QUADRADO: ")

                resp = float(a) * 6

                print("A ÁREA DO CUBO É:",resp)
                break




    if start == '8':
        print("\t FUNÇÕES: \n")

        print("PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPÇÕES: ")

        a = input("DESCOBRIR O VALOR DE Y ----> \n'1'\n"
                  "DESCOBRIR O VALOR DE X ----> \n'2'\n"
                  "SAIR ----> \n'n'\n")


        if a == 'n':
            print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")

            exit()

            break


        if a == '1':
            print('\t VALOR DE Y: \n')

            b = input("DIGITE O VALOR DE X: ")
            c = input("DIGITE O VALOR DE B: ")

            resp = float(c) + float(b)

            print("\t O VALOR DE Y É:",resp,"\n")

            break


        if a == '2':
            print("\t VALOR DE X: \n")

            b = input("DIGITE O VALOR DE Y: ")
            c =input('DIGITE O VALOR DE B: ')

            resp = float(c) - float(b)

            print('\t O VALOR DE X É:',resp,'\n')

            break


        else:
            print ("\t CARACTERE INVÁLIDO!!!\n")
            continue


        break



    if start == '9':
        print ("\t VELOCIDADE MÉDIA: \n")

        a = input('DIGITE A DISTÂNCIA PERCORRIDA: ')
        b = input("DIGITE O TEMPO GASTO (EM HORAS): ")
                  



        resp = float(a) / float(b)

        print("\t A VELOCIDADE MÉDIA É:",resp,"\n")

        


    
        
        


    #
    # -*- FIM DO PROGRAMA -*-

        


    



