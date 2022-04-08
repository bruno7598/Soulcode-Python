try:

    alunos = []
    disciplinas = ["matematica", "portugues", "fisica"]

    while True:
        if input("Continuar cadastrando? S/N: ").upper() == "N": #.upper() para ajudar o usuario quando digitar qualquer linha
            break #comando para parar se digitar o botão selecionado
        else:
            aluno = []
            nome = input("Digite o nome do aluno: ")
            aluno.append(nome)
        for disciplina in disciplinas:
            nota = input("Digite a nota de " + disciplina + ": ")
            aluno.append(nota)
        alunos.append(aluno)
    
    print(alunos)
except Exception as e:
    print(str(e))