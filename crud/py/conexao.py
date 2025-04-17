import mysql.connector  # Importa a biblioteca mysql.connector para conexão com o banco de dados MySQL

# Função para criar uma conexão com o banco de dados MySQL
def criar_conexao(host, usuario, senha, banco):
    # Estabelece uma conexão com o banco de dados
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

# Função para fechar a conexão com o banco de dados
def fechar_conexao(con):
    # Fecha a conexão com o banco de dados
    return con.close()