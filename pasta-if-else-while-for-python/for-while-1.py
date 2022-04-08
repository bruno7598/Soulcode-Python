try:
    alunos = ["joao", "maria", "steve", "gustavo", "jorge", "aline"]
    notas = []

    for aluno in alunos: #Estrutura de repetição para usar na lista
        print("Qual a nota de:", aluno) #printando cada nome de aluno na lista
        nota = input() #inputando logo apos o print, a nota que vc vai querer adicionar para cada aluno
        notas.append(nota) #add cada nota em seu lugar na lista
# A SEGUIR ALUNOS APROVADOS VAI EXIBIR NA TELA    
    print("Alunos aprovados") 
    for i in range(0, len(alunos)): #Estrutura de repetição para (i) se uma RANGE (0, ler alunos).
        if float(notas[i]) <= 60: #mostrando que notas estão a cima ou igual 60 
            continue # ai ele continua rodando para saber das outras notas
        print(alunos[i], " ", notas[i])# vai printar o nome dos alunos que passaram em sequencia um espaço e as notas!!
    

except Exception as e:
    print(str(e))
