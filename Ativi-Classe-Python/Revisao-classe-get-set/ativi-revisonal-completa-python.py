
# 1 - do parabéns
try:
    print("-"*20)
    n1 = int(input("Digite o primeiro: "))
    n2 = int(input("Digite o segundo : "))
    n3 = int(input("Digite o terceiro: "))
    n4 = int(input("Digite o quarto  : "))
    print("-"*20)
except Exception as e:
    print("Erro", str(e))
try:
    if n1 == 1:
        print("Parabéns")
    elif n2 == 2:
        print("Parabéns")
    elif n3 == 3:
        print("Parabéns")
    elif n4 == 4:
        print("Parabéns")
    print("-"*20)    
except Exception as e:
    print("Erro", str(e))



# 2 - nome em sequencia
try:
    nomes = []
    print("Aprendendo a sequecia")
    while True:
            if input("Continuar cadastrando? S/N: ").upper() == "N":
                break 
            else:
                aluno = []
                nome = input("Digite o nome do aluno: ")
                aluno.append(nome)
            nomes.append(aluno)       
    print(nomes)
except Exception as e:
    print("Erro", str(e))


# 3 - Estado por extenso
cont = ("Acre", "Alagoas","Amapá","Amazonas", "Bahia", "Ceará", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná","Pernambuco","Piauí","Rio de Janeiro","Rio Grande do Norte","Rio Grande do Sul","Rondônia","Roraima", "Santa Catarina","São Paulo","Sergipe","Tocantins","Distrito Federal")

try:
    while True:
        if input("Continuar Procurando ESTADOS DO BRASIL S/N: ").upper() == "N":
                print("-"*20)
                break
        print("-"*30)
        codigo_porestado = str(input("Digite o estado que deseja abreviado: "))

        if codigo_porestado == "AC":
            print(cont[0])
        elif codigo_porestado == "AL":
	        print(cont[1])
        elif codigo_porestado == "AP":
    	    print(cont[2])
        elif codigo_porestado == "AM":
            print(cont[3])
        elif codigo_porestado == "BA":
    	    print(cont[4])
        elif codigo_porestado == "CE":
    	    print(cont[5])
        elif codigo_porestado == "ES":
    	    print(cont[6])
        elif codigo_porestado == "GO":
    	    print(cont[7])
        elif codigo_porestado == "MA":
    	    print(cont[8])
        elif codigo_porestado == "MT":
    	    print(cont[9])
        elif codigo_porestado == "MS":
    	    print(cont[10])
        elif codigo_porestado == "MG":
    	    print(cont[11])
        elif codigo_porestado == "PA":
    	    print(cont[12])
        elif codigo_porestado == "PB":
    	    print(cont[13])
        elif codigo_porestado == "PR":
    	    print(cont[14])
        elif codigo_porestado == "PE":
    	    print(cont[15])
        elif codigo_porestado == "PI":
    	    print(cont[16])
        elif codigo_porestado == "RJ":
    	    print(cont[17])
        elif codigo_porestado == "RN":
    	    print(cont[18])
        elif codigo_porestado == "RS":
    	    print(cont[19])
        elif codigo_porestado == "RO":
    	    print(cont[20])
        elif codigo_porestado == "RR":
    	    print(cont[21])
        elif codigo_porestado == "SC":
    	    print(cont[22])
        elif codigo_porestado == "SP":
    	    print(cont[23])
        elif codigo_porestado == "SE":
    	    print(cont[24])
        elif codigo_porestado == "TO":
    	    print(cont[25])
        elif codigo_porestado == "DF":
    	    print(cont[26])
except Exception as e:
    print("Erro", str(e))


# 4 - Resolver potência

try:   
    print("POTÊNCIAS: \n")
                
                
    print("-"*20)
    a = float(input("Digite um valor para base: "))
    b = float(input("Digite um valor para expoente: "))
    print("-"*20)
    a1 = float(input("Digite um valor para base 2: "))
    b1 = float(input("Digite um valor para expoente 2: "))
    print("-"*20)
    resp = float(a) ** float(b)
    resp1 = float(a1) ** float(b1)

    print("-"*20)    
    print("RESULTADO: {0} , {1} ".format(resp, resp1))
    print("-"*20)
except Exception as e:
    print("Erro", str(e))

# 5 - Quantos segundos foi pressionada a tecla


import datetime
try:
    t2 = datetime.datetime.now()
    tecla = input("Aperte qualquer tecla: ")
    t1 = datetime.datetime.now()
    result = t1 - t2
    print("O tempo que passou foi: ", result)

except Exception as e:
    print("Erro", str(e))


# 6 - Produto (nome_do_produto, descrição, preço e quantidade_estoque)

try:
    descricao = []
    nome_do_produto = []
    precos = []
    quantidade_estoque = []

    while True:
        
        print("-"*30)
        descrito = []
        print("Qual a descrição do produto: ") 
        descrito = input() 
        descricao.append(descrito)
        
        print("-"*30)
        nome = []
        print("Qual o nome do produto: ") 
        nome = input() 
        nome_do_produto.append(nome)

        print("-"*30)
        preco = []
        print("Qual o preço do produto: ") 
        preco = input() 
        precos.append(preco) 
        
        print("-"*30)
        quantidade = []
        print("Qual a quantidade do produto:") 
        quantidade = input() 
        quantidade_estoque.append(quantidade)
        
        print(descricao, nome_do_produto, precos, quantidade_estoque)
        break

except Exception as e:
    print(str(e))



# 7 - Matriz adicional

