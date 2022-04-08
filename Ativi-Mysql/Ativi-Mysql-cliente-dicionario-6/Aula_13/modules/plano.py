from modules.connector import InterfaceDB, get_db_info

#classe com os metodos do plano
class Plano:
    nome = ""
    preco = ""
    descricao = ""

    #iniciando o construtor
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    #metodo para salvar a nova venda no banco de dados
    def save_plano(self):
        try:
            query = f"insert into plano (nome, preco, descricao) values ('{self.nome}', '{self.preco}', '{self.descricao}');"
            user, password, host, database = get_db_info()
            db = InterfaceDB(user, password, host, database)
            db.executar(query)
            print("Informacao inserida com sucesso!!!")
        except Exception as e:
            print(str(e))

#funcao que solicita as informacoes a serem adicionada para um novo plano
def new_plano(nome=None, preco=None, descricao=None):
    try:
        if nome == None:
            nome = input("Informe o nome do plano: ")
            preco = input("Informe o preço do plano: ")
            descricao = input("Informe a descrição do plano: ")
        p = Plano(nome, preco, descricao)
        return p
    except Exception as e:
        print(str(e))
        

