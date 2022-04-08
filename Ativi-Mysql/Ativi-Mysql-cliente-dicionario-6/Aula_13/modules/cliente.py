from modules.connector import InterfaceDB, get_db_info
from datetime import datetime

#classe com os metodos do cliente
class Cliente:
    nome = ""
    data = ""
    cadastro = ""
    plano = ""
    data_plano = ""
    
    #iniciando o construtor
    def __init__(self, nome, data, cadastro, plano, data_plano):
        self.nome = nome
        self.data = data
        self.cadastro = cadastro
        self.plano = plano
        self.data_plano = data_plano
    

    #metodo para salvar o novo cliente no banco de dados
    def save_cliente(self):
        try:
            query = f"insert into cliente (nome, data, cadastro, plano, data_plano) values ('{self.nome}', '{self.data}', '{self.cadastro}', '{self.plano}', '{self.data_plano}');"
            user, password, host, database = get_db_info()
            db = InterfaceDB(user, password, host, database)
            db.executar(query)
            print("Informacao inserida com sucesso!!!")
        except Exception as e:
            print(str(e))

#funcao que solicita as informacoes a serem adicionada para um novo cliente
def new_cliente(nome=None, data=None, cadastro=None, plano=None, data_plano=None):
    try:
        if nome == None:
            nome = input("Informe o nome do cliente: ")
            data = input("Informe a data do cadastro (ano-mes-dia): ")
            cadastro = input("Informe o código do cliente: ")
            plano = input("Informe o plano: ")
            data_plano = input("Informe a data de adesão ao plano (ano-mes-dia): ")
        c = Cliente(nome, data, cadastro, plano, data_plano)
        return c
    except Exception as e:
        print(str(e))
        
#funcao que gera a query para buscar o percentual de clientes que estao fora da fidelidade
def consulta_porcentagem():
    try:
        query = "SELECT id, TIMESTAMPDIFF(day, data_plano, '2021-11-18') FROM cliente;"
        user, password, host, database = get_db_info()
        db = InterfaceDB(user, password, host, database)
        dados = db.selecionar(query)
        lista_id_maior_365 = []
        lista_id = []
        for i in dados:
            data = i[1]
            id_cliente = i[0]
            lista_id.append(id_cliente)
            if data > 365:
                lista_id_maior_365.append(id_cliente)              
        print(f"O percentual de clientes que estão fora da fidelidade é: ", len(lista_id_maior_365) / len(lista_id) * 100, "%")     
    except Exception as e:
        print(str(e))

#funcao que gera a query para buscar o nome dos clientes que estao fora da fidelidade        
def cliente_fora_fidelidade():
    try:
        query = "SELECT nome, id, TIMESTAMPDIFF(day, data_plano, '2021-11-18') FROM cliente;"
        user, password, host, database = get_db_info()
        db = InterfaceDB(user, password, host, database)
        dados = db.selecionar(query)
        lista_id_maior_365 = []
        lista_nome = []
        for i in dados:
            data = i[2]
            nome_cliente = i[0]
            lista_nome.append(nome_cliente)
            if data > 365:
                lista_id_maior_365.append(nome_cliente)    
        print(f"A quantidade de clientes que estão fora da fidelidade é: ", len((lista_id_maior_365)))                
        print(f"Os clientes que estão fora da fidelidade são: ", (lista_id_maior_365))            
    except Exception as e:
        print(str(e))
        
#funcao que gera a query para buscar os nomes dos clientes com o plano mais caro
def cliente_plano_mais_caro():
    try:
        query = "SELECT CLIENTE.NOME FROM CLIENTE INNER JOIN PLANO ON  plano.nome = cliente.plano WHERE CLIENTE.PLANO = 'Rosa';"
        user, password, host, database = get_db_info()
        db = InterfaceDB(user, password, host, database)
        dados = db.selecionar(query)
        print(f"Os clientes com o plano mais caro são: {dados}")
    except Exception as e:
        print(str(e))