import mysql.connector

# Conectando MYSQL

def executar(query):
   try:
      con = mysql.connector.connect(user='root', password='Eugostode@55', host='127.0.0.1', database='netflix')
      cursor = con.cursor()
      cursor.execute(query)
      cursor.close()
      con.commit()
      con.close()
   except Exception as e:
    print(e)

def buscar(query):
    try:
      con = mysql.connector.connect(user='root', password='Eugostode@55', host='127.0.0.1', database='netflix')
      cursor = con.cursor()
      cursor.execute(query)
      return cursor.fetchall()
    except Exception as e:
      print(e)
    finally:
        cursor.close()
        con.close()


        
if __name__ == "__main__":
    
    # Montando o menu para o usuario
    
    try:
      while True:
        
        print("-="* 30)
        selecao = input("1 - CADASTRAR VENDA \n"
                        "2 - BUSCAR INFROMAÇÕES SOLICITADAS \n" 
                        "3 - EXCLUIR \n" 
                        "4 - ENCERRAR \n"
                        " Faça sua escolha: ")
        print("-="* 30)
        
        if selecao == "1":
        
         while True:
            
            
            selecao = input("1 - Cadastro passo a passo para usuario: \n"
                            "2 - Cadastro para programador: \n"
                            "3 - Sair do Menu \n"
                            " Escolha o numero: ")
               
            if selecao == "1":
            
                idvendedor = input("Informe o idVendedor 1 a 1000: ")
                idproduto = input("Informe o idProduto 1 a 2000: ")
                valorTotal = input("Informe Valor do Produto: ")
                comissao = 0.08
                valores = "( '{}', '{}', '{}', '{}')".format(idvendedor, idproduto, valorTotal, comissao)
                query = "INSERT INTO vendas (idvendedor, idproduto, valorTotal, comissao) VALUES" + valores+";"
                print("SEU CADASTRO FOI EFETUADO COM SUCESSO!!" .format(query))
                executar(query)
            
            elif selecao == "2":
    
                query = "INSERT INTO vendas (idvendedor, idproduto, valorTotal, comissao) VALUES (60,110,31.00,0.08), (47,111,30.00,0.08), (48,112,30.00,0.08), (49,113,41.00,0.08), (50,114,164.00,0.08), (51,115,165.00,0.08), (60,116,30.00,0.08), (53,117,30.00,0.08), (54,118,2450.00,0.08), (55,119,186.00,0.08), (56,120,545.00,0.08), (57,121,645.00,0.08), (58,122,833.00,0.08), (59,123,120.00,0.08), (60,124,120.00,0.08), (60,852,456.00,0.08), (62,1569,183.50,0.08), (63,1570,190.30,0.08), (64,1610,185.05,0.08), (65,1611,55.00,0.08), (66,1612,60.00,0.08), (60,1613,75.00,0.08), (68,1876,89.00,0.08), (69,860,560.05,0.08), (70,861,600.10,0.08), (60,110,31.00,0.08), (61,111,30.00,0.08), (62,112,30.00,0.08), (63,113,41.00,0.08), (64,114,164.00,0.08), (65,860,560.05,0.08), (66,118,2450.00,0.08), (67,119,186.00,0.08), (65,120,545.00,0.08), (280,121,645.00,0.08), (281,122,833.00,0.08), (282,123,120.00,0.08), (283,124,120.00,0.08), (281,852,456.00,0.08), (282,118,2450.00,0.08), (283,119,186.00,0.08), (278,120,545.00,0.08), (279,121,645.00,0.08), (280,1770,1250.50,0.08), (285,881,533.00,0.08), (282,1568,90.00,0.08), (285,1569,183.50,0.08), (284,1570,190.30,0.08), (285,1610,185.05,0.08), (286,1611,55.00,0.08), (287,1612,60.00,0.08), (285,1613,75.00,0.08), (708,1876,89.00,0.08), (709,122,833.00,0.08), (710,123,120.00,0.08), (711,124,120.00,0.08), (712,852,456.00,0.08), (713,110,31.00,0.08), (710,111,30.00,0.08), (711,112,30.00,0.08), (716,113,41.00,0.08), (717,114,164.00,0.08), (718,1770,1250.50,0.08), (719,1900,250.15,0.08)  "";"
                print("SEU CADASTRO FOI EFETUADO COM SUCESSO!!" .format(query))
                executar(query)
                
            elif selecao == "3":
                break

        
        elif selecao == "2":
            
            print("-="* 30)
            busca = input("1 - O TOTAL DE VENDAS \n"
                            "2 - O FUNCIONARIO ESTRELA NAS VENDAS \n"
                            "3 - O FUNCIONARIO ESTRELA NAS QUANTIDADES \n"
                            "4 - O FORNECEDOR MAIS UTILIZADO \n"
                            "5 - O TOTAL DE COMISSÃO DE CADA FUNCIONARIO  - 8 porcento DE COMISSAO \n"
                            "6 - PARA SAIR \n"
                             "Selecione o numero: ")
            print("-="* 30)
            
            try:
             while True: 
                
            
                if busca == "1":
                
                    query = "SELECT sum(h.valorTotal) FROM  vendas h " ";"
                    dados = buscar(query)
                    linha = []
                    for linha in dados:
                        print("TOTAL DE VENDA É: ", linha[0])
                    break
               
                    
                elif busca == "2":
                    
                    query = "SELECT v.nome_vendedor, sum(h.valorTotal) AS soma_das_Vendas FROM  vendedor v  INNER JOIN  vendas h  ON v.idvendedor = h.idvendedor WHERE h.valorTotal > any (SELECT h.valorTotal from vendas h) GROUP BY v.nome_vendedor ORDER BY soma_das_Vendas DESC LIMIT 1"  ";"
                    dados = buscar(query)
                    linha = []
                    for linha in dados:
                        print("O NOME DO FUNCIONARIO: {} \n" 
                              "O SEU TOTAL DE VENDAS: {} \n" .format(linha[0],linha[1]))
                    break


                elif busca == "3":
                    
                    query = "SELECT v.nome_vendedor, count(h.idvendedor) AS Quantidade_DE_Vendas FROM vendedor v INNER JOIN vendas h ON v.idvendedor = h.idvendedor GROUP BY v.nome_vendedor ORDER BY Quantidade_DE_Vendas DESC LIMIT 1" ";"
                    dados = buscar(query)
                    linha = []
                    for linha in dados:
                        print("O NOME DO FUNCIONARIO: {} \n" 
                              "A QUANTIDADE QUE ELE VENDEU: {} \n" .format(linha[0],linha[1]))
                    break
                
                elif busca == "4":
                    
                    query = "SELECT f.nome_fornecedor, count(p.idfornecedor) AS Quantidade_de_fornecedor FROM fornecedor f INNER JOIN produto p ON p.idfornecedor = f.idfornecedor GROUP BY p.idfornecedor ORDER BY quantidade_de_fornecedor DESC LIMIT 2"";"
                    dados = buscar(query)
                    linha = []
                    for linha in dados:
                        print("O NOME DO FORNECEDOR: {} \n"
                              "QUANTAS VEZES COMPRAMOS: {} \n" .format(linha[0],linha[1]))
                    break
                
                elif busca == "5":
                    
                    query = "SELECT v.nome_vendedor, TRUNCATE((sum(h.valorTotal)*h.comissao),2) AS Valor_da_Comissao FROM vendedor v INNER JOIN vendas h ON v.idvendedor = h.idvendedor GROUP BY v.nome_vendedor ORDER BY Valor_da_Comissao desc"";"
                    dados = buscar(query)
                    linha = []
                    for linha in dados:
                        print("NOME DO VENDEDOR: {} \n"
                              "A COMISSÃO QUE ELE VAI RECEBER: {} \n" .format(linha[0],linha[1]))
                    break
                
                elif selecao == "6":
                    break
                
            except Exception as e:
                print(str(e))
                    
        elif selecao == "3":
            
            id_vendas = input("informe o idvendas: ")
            valores = " '{}' ".format(id_vendas)
            query = "DELETE FROM vendas WHERE idvendas  =" + valores +";"
            print("FOI DELETADO COM SUCESSO!!" .format(query))
            executar(query)
        
        elif selecao == "4":
            break
            
    except Exception as e:
        print(str(e))
        