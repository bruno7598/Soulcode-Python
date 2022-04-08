from modules.produtos import Produto
from modules.pessoas import Pessoa


class Vendas(Produto):
    
    
 
 
# INSERINDO AS FUNÇÕES DOS PRODUTOS    
    def inserir_dados1(self):
        return super().inserir_dados1() 
    
    
    
# FUNÇÃO CHAMANDO OS DADOS DE PRODUTOS E CLIENTES PARA RETORNAR    
    def inserir_dados(self):
    
        vendas = []
        
        for i in range(1):
            constru = Produto(pessoas=None)
            id_venda = input('ID Vendas : ')
            quantidade = int(input('Quantidade comprada: '))
     

            vendas.append({ 'ID Vendas': id_venda, 'Quantidade comprada': quantidade ,'Quantidade estoque': constru.get_estoque() })
        
        print('=-'*30)
        print('AS VENDAS FEITAS')
        print('=-'*30)         
        
# CALCULO DA VENDA TIRANDO DO ESTOQUE        
        
    
        constru = Produto(pessoas=None)
        b = quantidade
        a = constru.get_estoque()
        total = a - b            
        print("O que sobrou no estoque foi: ", total)       
            
# PRINTANDO AS INFORMAÇÕES DE VENDAS  
            
        for pessoa in vendas:
            for chave, valor in pessoa.items():
                
                print("{} => {}".format(chave, valor))
        print("=_"*30) 
            
           
        return super().inserir_dados()
        

    