from modules.vendas import Venda
from modules.connector import Interface_db   

"""
  description:
    Faz inserção de venda  
    Faz Seleção de venda
    Faz Atualização de venda
    Faz Exclusão de venda 
    Atualiza o campo estoque na tabela de produtos
  @author:
    Daniele Nogueira
    Eduardo de Souza D'Antona
    Diego Alves
    Robson Motta
    Tais Santos
    Bruno Miranda
""" 
       
if __name__ == "__main__":
    try: 
      while True:
        
        print("-="* 30)
        selecao = input("1 - INSERIR VENDA \n"
                        "2 - CONSULTAR VENDA \n" 
                        "3 - ATUALIZAR VENDA \n" 
                        "4 - EXCLUIR VENDA \n"
                        " Faça sua escolha: ")
        print("-="* 30)


# INSERINDO
        if selecao == "1":
             
          conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "boasaude")
          idvenda = input("Digite o codigo da Venda: ")
          idproduto = input("Digite o codigo do produto: ")
          quantidade = input("Digite a quantidade: ")
          v = Venda(None,idvenda, idproduto, quantidade)
          valores = "( {}, {}, {})".format(int(v.get_venda()),int(v.get_produto()),int(v.get_quantidade()))
          dados = conexao.inserir("INSERT INTO itensvenda (venda, produto, quantidade) VALUES" + valores + ";")
          conexao.inserir("UPDATE produtos SET estoque = estoque - " + v.get_quantidade() + " WHERE referencia = " +v.get_produto()+ ";")

# SELECT          
        elif selecao == "2":
          
          conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "boasaude")
          dados = conexao.selecionar("SELECT * FROM itensvenda")
          lista_vendas = []
          for dado in dados:
              v = Venda(dado[0], dado[1], dado[2], dado[3])
              lista_vendas.append(v)  
          for i in range(len(lista_vendas)):
              print(lista_vendas[i].get_id(), " - ", lista_vendas[i].get_venda()," - ",lista_vendas[i].get_produto(), " - ",lista_vendas[i].get_quantidade())
              
              
# ATUALIZAÇÃO        
        elif selecao == "3":
          
          conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "boasaude")
          id = input("Digite o id da venda: ")
          quantidade_nova = input("Digite a quantidade nova: ")
          dados = conexao.selecionar(f"SELECT quantidade, produto FROM itensvenda where id = {id}")
          v1 = dados[0][0]
          v2 = dados[0][1]
          conexao.inserir(f"UPDATE itensvenda SET quantidade = {quantidade_nova} WHERE id = {id};")
          conexao.inserir(f"UPDATE produtos SET estoque = estoque + ({v1} - {quantidade_nova}) WHERE referencia = {v2};")
          
          print("Deu certo!", dados)
  
          
# DELETE
        elif selecao == "4":
          
          conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "boasaude")
          id = input("Digite o id da venda: ")
          dados = conexao.selecionar(f"SELECT quantidade, produto FROM itensvenda where id = {id}")
          v1 = dados[0][0]
          v2 = dados[0][1]
          conexao.inserir(f"DELETE FROM itensvenda WHERE id  = {id} ;")
          conexao.inserir(f"UPDATE produtos SET estoque = estoque + {v1} WHERE referencia = {v2};")
          print("Deu certo!") 
          
          
    except Exception as e:
      print(str(e))
      
 
        
          
