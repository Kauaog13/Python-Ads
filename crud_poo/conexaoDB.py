import mysql.connector

class Conexao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'crud_poo',
            port = 3306
        )
        self.cursor = self.conn.cursor()
    def fechar(self):
        self.cursor.close()
        self.conn.close()