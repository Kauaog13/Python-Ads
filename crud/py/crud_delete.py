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

# Executa o comando SQL para selecionar o registro que será deletado
cod = int(input("Digite o código do usuario: "))

# Comando SQL para deletar o registro
sql = f'delete usuarios set cod= "{cod}'

# Executa o comando SQL
cursor.execute(sql)

# Confirma a atualização
conexao.commit()

# Fecha o cursor
conexao.close()