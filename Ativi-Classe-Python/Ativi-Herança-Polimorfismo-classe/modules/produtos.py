from modules.clientes import Clientes



class Produto(Clientes):
    
    
        
# FUNÇÃO PARA INSERIR DADOS    
    def inserir_dados1(self):
        produto = []
        
        
        for i in range(1):
            constru = Produto(pessoas=None)
            nome_produto = input('Nome produto : ')
            validade = input('Validade : ')
            valor = input('Valor : ')
            constru.set_estoque(int(input("Digite a quantidade no estoque: ")))
            
            produto.append({ 'nome produto': nome_produto, 'validade':validade, 'Valor':valor, 'Quantidade de estoque:': constru.get_estoque()})
           



# APRESENTANDO OS DADOS DE PRODUTOS
           
        print('=-'*30)
        print('TODOS OS PRODUTOS')
        print('=-'*30)  
        
        
        for pessoa in produto:
            for chave, valor in pessoa.items():
                print("{} => {}".format(chave, valor))
     



# SET E GET PARA FUNCIONAMENTO DO ESTOQUE     
    def set_estoque(self,estoque):
        try:
            self.estoque = estoque
        except Exception as e:
            print(str(e))
                
    def get_estoque(self):
        return self.estoque
    
    
    