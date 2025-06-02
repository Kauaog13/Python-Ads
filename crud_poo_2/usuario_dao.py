from db import ConexaoDB
from usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.db = ConexaoDB()

    def criar(self, usuario: Usuario):
        sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
        valores = (usuario.nome, usuario.email)
        self.db.cursor.execute(sql, valores)
        self.db.conn.commit()

    def listar(self):
        self.db.cursor.execute("SELECT * FROM usuarios")
        resultados = self.db.cursor.fetchall()
        return [Usuario(id=row[0], nome=row[1], email=row[2]) for row in resultados]

    def atualizar(self, usuario: Usuario):
        sql = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s"
        valores = (usuario.nome, usuario.email, usuario.id)
        self.db.cursor.execute(sql, valores)
        self.db.conn.commit()

    def deletar(self, id_usuario):
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.db.cursor.execute(sql, (id_usuario,))
        self.db.conn.commit()

    def fechar_conexao(self):
        self.db.fechar()
