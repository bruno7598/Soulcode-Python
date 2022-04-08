class Test:
    
    pessoas = []
    lugares = []
    casas = []
    
    
    def __init__(self, pessoas, lugares, casas):
        self.set_pessoas(pessoas)
        self.set_lugares(lugares)
        self.set_casas(casas)
   
   
    try:   
        def set_pessoas(self, pessoas):
            self.pessoas = pessoas
            
        def set_lugares(self, lugares):
                self.lugares = lugares
            
            
        def set_casas(self, casas):
            self.casas = casas
        
        def add_pessoas(self,pessoas):
            self.pessoas.append(pessoas)
            
            
            
    except Exception as e:
        print(str(e))
    
    
    try:    
        def get_pessoas(self):
            return self.pessoas
        
        def get_lugares(self):
            return self.lugares
        
        def get_casas(self):
            return self.casas
    except Exception as e:
        print(str(e))
    