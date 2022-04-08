
class Venda():
    """Classe venda

    Returns:
        venda(string): A venda é uma indentificador da venda
        produto(string): O indetificador do produto
        quantidade(string): A quantidade de produtos vendidos
    """
    id = ""
    venda = ""
    produto = ""
    quantidade = ""
    
    def __init__(self, id, venda, produto, quantidade):
        self.id = id
        self.venda = venda
        self.produto = produto
        self.quantidade = quantidade
    
# SETTERS     
    def set_id(self, i):
        try:
            self.id = i
        except Exception as e:
            print(str(e))
    
    def set_venda(self, i):
        try:
            self.venda = i
        except Exception as e:
            print(str(e))
            
    def set_produto(self, i):
        try:
            self.produto = i
        except Exception as e:
            print(str(e))
            
    def set_quantidade(self, i):
        try:
            self.quantidade = i
        except Exception as e:
            print(str(e))
    
    
# GETTERS            
    def get_id(self):
        return self.id        
    
    def get_venda(self):
        return self.venda
        
            
    def get_produto(self):
        return self.produto
        
            
    def get_quantidade(self):
        return self.quantidade
        