# Importa a biblioteca mysql.connector para conexão com o banco de dados MySQL
import mysql.connector

# Estabelece conexão com o banco de dados
conexao = mysql.connector.connect(
    # Endereço do servidor do banco de dados
    host = 'localhost',  # Servidor local
    # Usuário do banco de dados
    user = 'root',  # Usuário padrão do MySQL
    # Senha do banco de dados
    password = '',  # Senha do usuário
    # Nome do banco de dados
    database = 'faculdade',  # Nome do banco de dados a ser conectado
    # Porta do servidor do banco de dados
    port = '3307', # Porta padrão do MySQL
)

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()  # Cursor para executar comandos SQL

# Define a consulta SQL para selecionar todos os registros da tabela 'usuario'
sql = f'select * from usuario'  # Consulta SQL para selecionar todos os registros da tabela 'usuario'

# Executa a consulta SQL
cursor.execute(sql)  # Executa a consulta SQL

# Recupera todos os registros da consulta
resultado = cursor.fetchall()  # Recupera todos os registros da consulta

# Imprime o resultado da consulta
print(resultado)  # Imprime o resultado da consulta

# Fecha a conexão com o banco de dados
conexao.close()  # Fecha a conexão com o banco de dados