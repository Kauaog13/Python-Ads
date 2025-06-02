from conexaoDB import Conexao
from cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.conexaoDB = Conexao()
    def criar(self, cliente: Cliente):
        sql = "insert into clientes values(%s,%s,%s,%s,%s,%s)"
        valores = (cliente.idCliente, cliente.nome, cliente.tel, cliente.email, cliente.cidade, cliente.data_cadastro)
        self.conexaoDB.cursor.execute(sql,valores)
        self.conexaoDB.conn.commit()
    def listar(self):
        self.conexaoDB.cursor.execute("Select * from clientes")
        resultados = self.conexaoDB.cursor.fetchall()
        return [Cliente(idCliente=row[0], nome=row[1], tel=row[2], email=row[3], cidade=row[4], data_cadastro=row[5]) for row in resultados]
    def atualizar(self, cliente: Cliente):
        sql = "update clientes set nome= %s, tel= %s, email= %s, cidade= %s, data_cadastro= %s where idCliente= %s"
        valores = (cliente.nome, cliente.tel, cliente.email, cliente.cidade, cliente.data_cadastro)
        self.conexaoDB.conn.commit()
    def deletar(self, id_cliente):
        sql = "delete from clientes where idCliente = %s"
        self.conexaoDB.cursor.execute(sql, (id_cliente,))
        self.conexaoDB.conn.commit()
        
    def fechar_conexao(self):
        self.conexaoDB.fechar()