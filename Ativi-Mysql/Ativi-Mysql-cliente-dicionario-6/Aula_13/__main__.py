from modules.connector import InterfaceDB
from modules.cliente import Cliente, new_cliente, consulta_porcentagem, cliente_plano_mais_caro, cliente_fora_fidelidade
from modules.plano import Plano, new_plano
import datetime

#criacao do menu
if __name__ == "__main__":
    try:
        while True:
            selecao = input(" 1 - Cadastrar novo cliente \n 2 - Consulta porcentagem de clientes fora da fidelidade \n 3 - Consulta clientes fora da fidelidade \n 4 - Consulta clientes com o plano mais caro \n 5 - Cadastrar novo cliente \n 0 - Sair \n Digite a opção: " )
            if selecao == "1":
               cadastro = new_cliente()
               cadastro.save_cliente()
            elif selecao == "2":
               consulta_porcentagem()
            elif selecao == "3":   
               cliente_fora_fidelidade()
            elif selecao == "4":
                cliente_plano_mais_caro()
            elif selecao == "5":
                cadastro = new_plano()    
                cadastro.save_plano()
            elif selecao == "" or "0":
                break     
    except Exception as e:
        print(str(e))