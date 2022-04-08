import mysql.connector

class connector():
 def conectar():
        



    try:
        con = mysql.connector.connect(user='root', password = 'Eugostode@55', host = '127.0.0.1', database = 'universidade')
        query = "SHOW TABLES"
        cursor = con.cursor()
        cursor.execute(query)
        for row in cursor:
            print(str(row))
        cursor.close()
        con.close()
    except Exception as e:
        print(str(e))
        
       