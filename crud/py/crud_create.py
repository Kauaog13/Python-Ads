# Importa a biblioteca de conexão com o MySQL
import mysql.connector  

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

# Define o código do usuário como nulo (será gerado automaticamente pelo banco de dados)
cod = 'null'

# Solicita ao usuário que digite o nome, cidade e estado
nome = input("Digite o nome do usuario: ") 
cidade = input("Digite a cidade do usuario: ")
uf = input("Digite o estado do usuario: ")

# Cria a string SQL para inserir o novo usuário
sql = f'insert into usuarios values({cod}, "{nome}", "{cidade}", "{uf}", now())'

# Executa a string SQL
cursor.execute(sql)

# Confirma a operação no banco de dados
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()