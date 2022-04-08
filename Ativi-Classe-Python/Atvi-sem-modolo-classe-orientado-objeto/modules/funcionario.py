from modules.pessoa import Pessoa


class Funcionario(Pessoa):
    id = [300,301,302,303,304]
    cargo = ['Ferreiro', 'Maga', 'Professor','Diretor', 'Medico']
    
    
    def __init__(self, nome, rg, endereco, contato, cargo):
        super().__init__(nome, rg, endereco,contato)
        self.cargo = cargo
    
    def print_id_funcionario(self):
        print("ID DO CARGO: ",self.id)
        print("CARGO DO FUNCIONARIO: ", self.cargo)