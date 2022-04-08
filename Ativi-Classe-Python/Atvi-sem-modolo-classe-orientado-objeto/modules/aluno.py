from modules.pessoa import Pessoa


class Aluno(Pessoa):
    matricula = [1, 2, 3, 4, 5]
    
    
    
    def print_matricula(self):
        print("NUMERO DA MATRICULA: ", self.matricula)
    
