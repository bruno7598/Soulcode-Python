from modules.pessoa import Pessoa

class Funcionario(Pessoa):
    cargo = ""
    
    def __init__(self, nome, rg, tel, cargo="candidato"):
        super().__init__(nome, rg, tel)
        self.cargo = cargo
        
    def print_dados(self):
        super().print_dados()
        print(self.cargo)