import mysql.connector

class ConexaoDB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='senac',
            database='teste_crud'
        )
        self.cursor = self.conn.cursor()

    def fechar(self):
        self.cursor.close()
        self.conn.close()
