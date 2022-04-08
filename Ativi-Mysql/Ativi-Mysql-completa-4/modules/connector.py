# Import da lib para conexao
import mysql.connector
import numpy as np



class Interface_db:
    """CLASSE INTERFACE_DB

    Args:
            usuario (string): usuario para conexao ao banco
            senha (string): senha para acesso ao banco
            host (string): string contendo o endereco do host
            banco (string): string contendo o nome do banco
    """
    usuario, senha, host, banco = "", "", "", ""
    
    
    def __init__(self, usuario, senha, host, banco):
    
        try:
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
        except Exception as e:
            print(str(e))
    
    """Metodo para conectar
        returns: 
            con (Object)
            cursor (object)
    """
    def conectar(self):
        try:
            con = mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.banco)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))
            
    """Metodo para desconectar
    """         
    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))
            
    """Metodo para selecionar
        returns: 
            cursor (object)
    """
    def selecionar(self, comandosql):
        try:
            con, cursor = self.conectar()
            cursor.execute(comandosql)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            
    """Metodo para inserir
        returns: 
            cursor (object)
    """        
    def inserir(self, comandosql):
        try:
            con, cursor = self.conectar()
            cursor.execute(comandosql)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
    
    



    
    
            
    