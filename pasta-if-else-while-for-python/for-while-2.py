
try:
    alunos = [ ["joao",80,70,55,69], ["maria",74,68,90,89] ]

    print("matematica fisica quimica ed. fisica")
    for aluno in alunos:#usado para percorrer a primeira lista
        texto = ""
        for dado in aluno:#usado pra percorrer a lista dentro da lsita com notas e os alunos
            texto = texto + " " + str(dado)
        print(texto)
    


except Exception as e:
    print("Erro", e)

