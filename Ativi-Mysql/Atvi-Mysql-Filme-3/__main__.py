from modules.conector import interface_db
from modules.Filme import film

if __name__ == "__main__":
    try:
        #Conexao com o banco, retorno de dados brutos
        interface_banco = interface_db("root", "Eugostode@55", "127.0.0.1", "sakila")
        dados = interface_banco.selecionar("film_id, title, release_year, lenght", "film", "length ")
        
        #Organizacao dos dados brutos dentro de objetos
        lista_film = []
        for dado in dados:
            item = film(dado[0],dado[1],dado[2], dado[3])
            lista_film.append(item)

        nome_film.index(min)

        min_tam_film = min(lista_film[3])
        max_tam_film = max(lista_film[3])
        print("Os titulos do filme são: ")
        #Utilizacao da lista de objetos, no caso procura-se o maior id dentro dos objetos
        #qtde_film = len(lista_film)
        #for i in range(len(lista_film)):
         
         #   if lista_film[i].get_film() > qtde_film:
          #      film_id = lista_film[i].get_film()
           # elif lista_film[i].get_film() < qtde_film:
        #print("O ano com maior numero de lançamentos: ", qtde_film)
                    
                    
    except Exception as e:
        print(str(e))