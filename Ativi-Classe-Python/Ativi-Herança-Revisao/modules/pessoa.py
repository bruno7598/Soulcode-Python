class Pessoa:
    rg = ""
    nome = ""
    tel = ""
    
    def __init__(self, nome, rg, tel):
        self.nome = nome
        self.rg = rg
        self.tel = tel
        
    def print_dados(self):
        print(self.nome)
        print(self.rg)
        print(self.tel)