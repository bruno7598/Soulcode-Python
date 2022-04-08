from modules.aluno import Aluno




class Aluno_portugues(Aluno):
    nota = [50, 60, 80, 93, 53]
    
    
    
    def print_nota_portugues(self):
        print("NOTAS DE PORTUGUES", self.nota)
        
    