"""class aluno:
    nome = "teste"
    nota_matematica = 0
    nota_portugues = 0

if __name__ == "__main__":
    try:
        maria = aluno()
        maria.nome = input("Digite o nome: ")
        maria.nota_portugues = 80
        maria.nota_matematica = 70
        jose = aluno()
        jose.nome = "jose"
        
        print(jose.nome, maria.nome)
        
    except Exception as e:
        print(str(e))"""
        
        
class cliente:
    nome = "teste"
    cpf = 0
    data_nascimento = 0
    
    def __init__(self, nome, cpf):
        """Altera o cpf do cliente para o valor informado 
        
        Args:
            nome (string): nome do cliente
            cpf (string): cpf do cliente
        """
        try:
            self.nome = nome
            self.cpf = str(cpf)
        except Exception as e:
            print(str(e))

    def set_nome(self, nome):#
        self.nome = nome
    
    def get_nome(self): #Ele pega o valor direto da get
        return self.nome
    def get_cpf(self): #Ele pega o valor direto da get
        return self.cpf
    
    def set_cpf (self, cpf):
        """Altera o cpf do cliente para o valor informado 
        
        Args:
            cpf (string): cpf do cliente
        """
        try:
            
            self.cpf = str(cpf)
        except Exception as e:
            print(str(e))
        
    
if __name__ == "__main__":
    try:
        maria = cliente("Maria", "118.131.786-07")
        print("nome é: ", maria.get_nome())
        print(maria.get_cpf())
        
    except Exception as e:
        print(str(e))