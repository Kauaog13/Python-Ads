from conexao import criar_conexao, fechar_conexao  # Importa funções para criar e fechar conexão com o banco de dados

# Função para inserir um aluno no banco de dados
def insere_aluno(con, cod, nome, cidade, uf, data):
    # Cria um cursor para executar comandos SQL
    cursor = con.cursor()
    # Comando SQL para inserir um aluno
    sql = "insert into usuarios values (%s, %s, %s, %s, %s)"
    # Valores a serem inseridos
    valores = (cod, nome, cidade, uf, data)
    # Executa o comando SQL
    cursor.execute(sql, valores)
    # Fecha o cursor
    cursor.close()
    # Confirma as alterações no banco de dados
    con.commit()

# Função para selecionar todos os alunos do banco de dados
def select_alunos(con):
    # Cria um cursor para executar comandos SQL
    cursor = con.cursor()
    # Comando SQL para selecionar todos os alunos
    sql = "select * from usuarios"
    # Executa o comando SQL
    cursor.execute(sql)
    # Imprime os dados dos alunos
    for (cod, nome, cidade, uf, data) in cursor:
        print(cod, nome, cidade, uf, data)
    # Fecha o cursor
    cursor.close()

# Função principal do programa
def main():
    # Cria uma conexão com o banco de dados
    con = criar_conexao("127.0.0.1", "root", "senac", "facsenac")
    # Seleciona todos os alunos do banco de dados
    select_alunos(con)
    # Fecha a conexão com o banco de dados
    fechar_conexao(con)

# Verifica se o script está sendo executado como um programa principal
if __name__ == "__main__":
    # Chama a função principal
    main()