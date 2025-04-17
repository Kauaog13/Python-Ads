import mysql.connector  # Importa a biblioteca de conexão com o MySQL

# Estabelece conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',  # Endereço do servidor
    user='root',  # Usuário do banco de dados
    password='senac',  # Senha do banco de dados
    database='facsenac'  # Nome do banco de dados
    #port = 3306 ou 3307 - Caso não esteja conectando diretamente
)

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Define a consulta SQL
sql = f'select * from usuarios'  # Seleciona todos os registros da tabela 'usuarios'

# Executa a consulta SQL
cursor.execute(sql)

# Recupera os resultados da consulta
resultado = cursor.fetchall()

# Imprime os resultados
print(resultado)

# Fecha a conexão com o banco de dados
conexao.close()
