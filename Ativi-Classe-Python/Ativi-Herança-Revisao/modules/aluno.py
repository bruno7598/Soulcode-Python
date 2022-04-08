from modules.pessoa import Pessoa

class Aluno(Pessoa):
    matricula = ""
    
    def print_dados(self):
        super().print_dados()
        print(self.matricula)