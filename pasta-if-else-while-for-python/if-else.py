#Estrutura de decisão
try:
    total_de_vendas = 9800
    meta_de_vendas = 10000
    if total_de_vendas < meta_de_vendas:
        print("NAO ATINGIMOS A META!!!!!!!!!!")
    else:
        print("ATINGIMOS A META!!!!!")  

except Exception as erro:
    print('Meta não foi atingida', str(erro))