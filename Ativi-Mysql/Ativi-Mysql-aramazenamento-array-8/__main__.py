import numpy as np
from modules.conector import Interface_db
import pandas as pd



# try:
#         # #array para armazenar varias notas de um aluno, possui 1 dimensao
#         conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "netflix")
#         dados = conexao.selecionar("SELECT idvendedor FROM vendas")
#         test = np.asarray(dados)
#         # print(test)  
#         # for valores in range(len(test)):
#             # print("valor na posicao ", valores, " a valor e: ", test[valores])
            
#         #array para armazenar varias notas de varios alunos, possui 2 dimensoes
#         conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "netflix")
#         dados1 = conexao.selecionar("SELECT idvendedor,valorTotal FROM vendas")
#         test1 = np.array(dados1)
#         for i in range(len(test1)):
            
#             for j in range(len(test)):
#                 print("Está na linha: ", j, "E na coluna: ", i, " O valor é: ", test1[j][i])
        
# except Exception as e:
#     print(str(e))
# ----------------------------------------------------------------------------------------------------------------
# CODIGO DO EDUARDO E EQUIPE 

# import numpy as np


# arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], 
                
#                 [1, 2, 50], [2, 1, 150], [2, 2, 200], 
                
#                 [2, 3, 78], [2, 2, 50]])

# array_contador = np.zeros(len(arr))
                        
# contador, index, maior, maior_cliente, id_vendedor = 0,0,0,0,0

# for i in range(len(arr)):
#     if arr[i][2] > maior:
#         maior = arr[i][2]
   
# for i in range(len(arr)):
#     if arr[i][2] == maior:
#         print(f"id_vendedor -> {arr[i][0]} com o valor -> {maior}")
        
# print(array_contador)

# for i in range(len(arr)):
#     array_contador[arr[i][1]] += 1

# print(array_contador)

# for i in range(len(array_contador)):
#     if array_contador[i] > maior_cliente:
#         maior_cliente = array_contador[i]
#         index =  i    
               
# print(index)

-------------------------------------------------------------------------------------------------------------------------

arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])
print("As duas somas das maiores vendas: {} , {} " .format((arr[0][2]+arr[1][2]+arr[2][2]+arr[3][2]),(arr[4][2]+arr[5][2]+arr[6][2]+arr[7][2])))

for venda in range(len(arr)):   
    print("Os vendedores com maior venda são: {} "  .format(arr[venda][0])) 
    venda = 0
    if venda == 0:
        b = venda + 1
        print("O cliente que mais comprou é: ", arr[b][1])
 
-------------------------------------------------------------------------------------------------------------------------


arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])


total_vendedores = [0,0]
total_clientes = [0,0,0]

vendedor1,vendedor2,clientes,clientes1,clientes2 = [],[],[],[],[]

for i in range(len(arr)):
    
    if arr[i][0] == 1:
        total_vendedores[0] += arr[i][2]
        vendedor1 = arr[0][0]
        
    elif arr[i][0] == 2:
        total_vendedores[1] +=  arr[i][2]
        vendedor2 = arr[4][0]
        
    if arr[i][1] == 1:
        total_clientes[0]  += arr[i][2]
        clientes = arr[0][1]
        
    elif arr[i][1] == 2:
        total_clientes[1]  += arr[i][2]
        clientes1 = arr[1][1]
        
    elif arr[i][1] == 3:
        total_clientes[2] += arr[i][2]
        clientes2 = arr[2][1]


print('Total clientes: ', total_clientes)
print('Total vendedores: ', total_vendedores)
print('O vendedor que mais vendeu foi: {}, {} ' .format(vendedor1,vendedor2))
print('O cliente que mais comprou foi: {} ' .format(clientes1))   
        
        
        
        
        
# -------------------------------------------------------------------------------------------------------------------



try:
        # array para armazenar varias notas de um aluno, possui 1 dimensao
        conexao = Interface_db("root", "Eugostode@55", "127.0.0.1", "boasaude")
        dados = conexao.selecionar("SELECT *  FROM paciente")
        query = conexao.selecionar("SELECT p.nome FROM paciente p ,possui h where h.codpac = p.codpac group by h.codconv;")
        test = np.asarray(dados)
        test1 = np.asarray(query)
        print('Os pacientes que possuem convenio: {}' .format(test1))
        print('O codpaciente e nome dos que não tem convenio é:\n'
            '{} : {} \n'
            '{} : {}'.format(test[1][0], test[1][1],   test[4][0], test[4][1]))  
        

except Exception as e:
    print(str(e))