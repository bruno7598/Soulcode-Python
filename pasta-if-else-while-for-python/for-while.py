
try:
    lista = ["joao", "maria", "steve", "gustavo", "jorge", "aline"]

    
    #while notas != 0:
        #item = input()
        #if item == "": #aspas vazias é vazio
            #nota = 0
        #else:
            #alunos.append(item) #adiciona itens na lista
    #print(alunos)


    for item in lista:
        if item == "steve":
           continue
        else:
            print(item)
    
    
except Exception as e:
    print(str(e))
