class Pessoa:
    nome = []
    rg = []
    endereco = []
    contato = []
    
    
    def __init__(self, nome, rg, endereco, contato):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
    
    
    def print_indentidade(self):
        print("NOME DA PESSOA: ", self.nome)
        print("RG DA PESSOA: ",self.rg)
        print("ENDEREÇO: ", self.endereco)
        print("CONTATO: ", self.contato)
        