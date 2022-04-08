""" AS IMPORTAÇÕES UTILIZADAS PARA INSERIR OS ARQUIVOS E CALCULAR ELES DA MELHOR FORMA
"""
from pandas.core.frame import DataFrame
from pandas.io.sql import table_exists
from modules.conector import Conexao
from numpy import true_divide
import statistics as st
import pandas as pd
import numpy as np

# --------------------------------------------------------------------------------------------------
# INCLUINDO DUAS TABELAS NO BANCO DE DADOS UTILIZANDO O PYTHON
# --------------------------------------------------------------------------------------------------

# # IMPORTANDO AS DUAS TABELAS COM PANDAS
df = pd.read_csv("C:/Users/isa66/Desktop/Visualcode/.vscode/Aula_16/DADOS_1.csv")
df1 = pd.read_csv('C:/Users/isa66/Desktop/Visualcode/.vscode/Aula_16/DADOS_2.csv')



# # UNINDO E TRATANDO AS DUAS TABELAS USANDO PANDAS
x = pd.concat([df, df1])
df2 = x.dropna()


# # PERCORRENDO E INSERINDO OS DADOS EM UMA TABELO NO BANCO
for index, row in df2.iterrows():
    conexao = Conexao("localhost", "Trabalho", "postgres", "Eugostode@55")
    valores = "('{}',{})".format(row.data,row.valor)  
    conexao.manipular("INSERT INTO informa (data,valor) values " + valores + ";")





# # --------------------------------------------------------------------------------------------------
# # DIVIDIR TABELA INCLUIDA EM BLOCOS E REGISTRANDO OS MESMO EM UMA TABELA
# # --------------------------------------------------------------------------------------------------

# TO ENTRANDO NO MEU BANCO E BUSCANDO AS INFORMAÇÕES DA TABELA PRA TRATAR
try:
    conexao = Conexao("localhost", "Trabalho", "Brunom", "Eugostode@55")
    y = conexao.consultar(f"SELECT id_dados, TO_TIMESTAMP(data, 'MM/DD/YYYY'), valor FROM informa ORDER BY TO_TIMESTAMP(data, 'MM/DD/YYYY');")
    tabela_bruno = pd.DataFrame(y)
except Exception as e:
    print(str(e))

# AS VARIAVEIS PARA CAPTURAR O VALOR DETERMINADO PELO CLIENTE
data,media,mediana,moda,des_padrao,maximo,minimo = [],[],[],[],[],[],[]



# PEGANDO TODAS AS INFORMAÇÕES DO SELECT DO BANCO E TRANSFORMANDO EM BLOCOS DE 50 PARA MELHOR CALCULAR
max_row = 50
dataframes = []
while len(tabela_bruno) > max_row:
    top = tabela_bruno[:max_row]
    dataframes.append(top)
    tabela_bruno = tabela_bruno[max_row:]
else:
    dataframes.append(tabela_bruno)  



# USANDO UM FOR DENTRO DE OUTRO PARA PERCORRER E TRATAR CADA INFORMAÇÃO DE CADA BLOCO
for i in range(len(dataframes)):
    i = 0
    try:
        for j in range(len(dataframes[i])):
            
            a1 = np.min(dataframes[i][1])
            data.append(a1)
            
            x1 = np.mean(dataframes[i][2])
            media.append(x1)
            
            
            y1 = np.median(dataframes[i][2])
            mediana.append(y1)
            
            
            z1 = st.mode(dataframes[i][1])
            moda.append(z1)
            
            
            h1 = st.stdev(dataframes[i][2])
            des_padrao.append(h1)
            
            
            g1 = np.max(dataframes[i][2])
            maximo.append(g1)
            
            
            l1 = np.min(dataframes[i][2])
            minimo.append(l1)
            
            i += 1
        break
    except Exception as e:
        print(str(e))
    break

uniao = pd.DataFrame([data,media, mediana, moda, des_padrao, maximo, minimo])
uniao = uniao.T


# for index, row in uniao.iterrows():
#     conexao = Conexao("localhost", "Trabalho", "Brunom", "Eugostode@55")
#     valores = "('{}',row({},{},'{}',{},{},{}))".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])  
#     conexao.manipular("INSERT INTO dados (data_final,calculos) values " + valores + ";")




# --------------------------------------------------------------------------------------------------
# MENU PRO AJUDAR O CLIENTE A RECONHECER E CONFERIR OS DADOS
# --------------------------------------------------------------------------------------------------

while True:
        
        print("-="* 30)
        selecao = input("1 - SELECIONAR EM BLOCO DE 50 ORDENADOS POR DATA  \n"
                        "2 - CONSULTAR OS DADOS ESTATÍSTICOS DE CADA BLOCO \n" 
                        "3 - CONSULTAR A LISTA LOG \n" 
                        "4 - INSERIR UM DADO NA TABELA INFORMA \n"
                        "5 - ATUALIZAR UM DADO NA TABELA INFORMA \n"
                        "6 - DELETAR UM DADO NA TABELA INFORMA \n"
                        "7 - ENCERRAR \n"
                        " Faça sua escolha: ")
        print("-="* 30)
        



# --------------------------------------------------------------------------------------------------
# MENU USANDO A CONDIÇÃO IF INDO BUSCAR INFORMAÇÕES NO BANCO PARA AUXILIAR O USUARIO
# --------------------------------------------------------------------------------------------------  
        
# dividindo a tabela informa em blocos de 50
        if selecao == "1":
            
            const = np.array(dataframes)
            print(const)
            print("-="* 30)
           

           
# pegando todos os dados estatisticos dos 37 blocos de 50 que tabela gerou             
        if selecao == '2':
            
            
            conexao = Conexao("localhost", "Trabalho", "Brunom", "Eugostode@55")
            consulta = conexao.consultar('SELECT data_final, (calculos).media, (calculos).mediana, (calculos).moda,(calculos).desvio_prad,(calculos).maior, (calculos).menor  from dados order by data_final;')
            const = pd.DataFrame(consulta)
            const.columns = ['data', 'media', 'mediana','moda', 'desvio padrao', 'maior', 'menor']
            print(const)
            print("-="* 30)
            
 
 
# Pegando do banco as informações da tabela log para mostrar as modificações           
        if selecao == '3':
            
            i = int(input('Coloque aonde inicia sua busca id LOG: '))     
            j = int(input('Coloque aonde finaliza sua busca id LOG: '))
            if i != j:
                conexao = Conexao("localhost", "Trabalho", "Brunom", "Eugostode@55")
                consulta = conexao.consultar(f'SELECT * from log_trabalho WHERE id_log BETWEEN {i} and {j} ;')
                const = pd.DataFrame(consulta)
            print(consulta)
            
        
# Inserir um dado novo na tabela informa para o cliente        
        if selecao == '4':
            
            a = input('Informe uma data: ')
            b = input('Informe um valor: ')
            conexao = Conexao("localhost", "Trabalho", "postgres", "Eugostode@55")
            valores = "('{}',{})".format(a, b)  
            conexao.manipular("INSERT INTO informa (data,valor) values " + valores + ";")
            consulta = conexao.consultar('SELECT * FROM log_trabalho WHERE id_log=(SELECT max(id_log) FROM log_trabalho);')
            print('Foi INSERIDO com sucesso!! :::  ',  consulta)
        
        
# Atualizar valores da tabela informando o id            
        if selecao == '5':

            a = input('Informe um id_dados a ser atualizado: ')
            c = input('Informe um valor: ')
            conexao = Conexao("localhost", "Trabalho", "postgres", "Eugostode@55")    
            conexao.manipular(f"UPDATE informa SET valor = {c}  WHERE id_dados = {a}")
            consulta = conexao.consultar('SELECT * FROM log_trabalho WHERE id_log=(SELECT max(id_log) FROM log_trabalho);')
            print('Foi ATUALIZADO com sucesso!! :::  ',  consulta)
        
        
# Deletar da tabela informando id        
        if selecao == '6':
            
            
            a = input('Informe um id_dados a ser atualizado: ')
            conexao = Conexao("localhost", "Trabalho", "postgres", "Eugostode@55")  
            conexao.manipular(f"DELETE FROM informa WHERE id_dados = {a};")
            consulta = conexao.consultar('SELECT * FROM log_trabalho WHERE id_log=(SELECT max(id_log) FROM log_trabalho);')
            print('Foi DELETADO com sucesso!! :::  ',  consulta)

# Encerrar programa            
        if selecao == '7':
            
            break