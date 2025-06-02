# Supondo que usuario.py tenha algo como:
# class Usuario:
#     def __init__(self, id=None, nome=None, email=None):
#         self.id = id
#         self.nome = nome
#         self.email = email
#
#     def __str__(self):
#         return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}"

# Supondo que usuario_dao.py tenha a classe UsuarioDAO com os métodos:
# criar(usuario), listar(), atualizar(usuario), deletar(id), fechar_conexao()

from usuario import Usuario
from usuario_dao import UsuarioDAO

# --- Funções do Menu CRUD ---

def mostrar_menu_opcoes():
    """Exibe as opções do menu."""
    print("\n----- MENU CRUD USUÁRIOS -----")
    print("1. Criar Usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Sair")
    return input("Escolha uma opção: ")

def criar_novo_usuario(dao: UsuarioDAO):
    """Solicita dados e cria um novo usuário."""
    print("\n--- Criar Novo Usuário ---")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    if nome and email:
        novo_usuario = Usuario(nome=nome, email=email)
        try:
            dao.criar(novo_usuario)
            print("✅ Usuário criado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao criar usuário: {e}")
    else:
        print("⚠️ Nome e email são obrigatórios.")

def listar_todos_usuarios(dao: UsuarioDAO):
    """Lista todos os usuários cadastrados."""
    print("\n--- Lista de Usuários ---")
    usuarios = dao.listar()
    if usuarios:
        for usuario in usuarios:
            print(usuario)  # Garanta que sua classe Usuario tenha um método __str__
    else:
        print("ℹ️ Nenhum usuário cadastrado.")

def atualizar_dados_usuario(dao: UsuarioDAO):
    """Solicita ID e novos dados para atualizar um usuário."""
    print("\n--- Atualizar Usuário ---")
    try:
        id_usuario = int(input("Digite o ID do usuário que deseja atualizar: "))
    except ValueError:
        print("❌ ID inválido. Por favor, insira um número.")
        return

    # Para atualizar, precisamos do objeto usuário.
    # A forma mais eficiente seria ter um dao.buscar_por_id(id_usuario).
    # Como o exemplo original não mostra isso, vamos listar e encontrar:
    usuarios_cadastrados = dao.listar()
    usuario_para_atualizar = None
    for u in usuarios_cadastrados:
        if u.id == id_usuario:
            usuario_para_atualizar = u
            break

    if not usuario_para_atualizar:
        print(f"❌ Usuário com ID {id_usuario} não encontrado.")
        return

    print(f"Usuário encontrado: {usuario_para_atualizar}")
    novo_nome = input(f"Novo nome (atual: {usuario_para_atualizar.nome}) (deixe em branco para não alterar): ")
    novo_email = input(f"Novo email (atual: {usuario_para_atualizar.email}) (deixe em branco para não alterar): ")

    alterado = False
    if novo_nome:
        usuario_para_atualizar.nome = novo_nome
        alterado = True
    if novo_email:
        usuario_para_atualizar.email = novo_email
        alterado = True

    if alterado:
        try:
            dao.atualizar(usuario_para_atualizar)
            print("✅ Usuário atualizado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao atualizar usuário: {e}")
    else:
        print("ℹ️ Nenhuma alteração fornecida.")

def deletar_um_usuario(dao: UsuarioDAO):
    """Solicita ID e deleta um usuário."""
    print("\n--- Deletar Usuário ---")
    try:
        id_usuario = int(input("Digite o ID do usuário que deseja deletar: "))
    except ValueError:
        print("❌ ID inválido. Por favor, insira um número.")
        return

    # Opcional: Adicionar uma confirmação antes de deletar
    # usuarios = dao.listar()
    # usuario_existe = any(u.id == id_usuario for u in usuarios)
    # if not usuario_existe:
    #     print(f"❌ Usuário com ID {id_usuario} não encontrado.")
    #     return
    # confirmacao = input(f"Tem certeza que deseja deletar o usuário com ID {id_usuario}? (s/N): ")
    # if confirmacao.lower() != 's':
    #     print("Operação cancelada.")
    #     return

    try:
        # Assumindo que dao.deletar espera o ID do usuário, como no seu exemplo original
        dao.deletar(id_usuario) # Se o DAO retornar um status, seria bom verificar
        print(f"✅ Usuário com ID {id_usuario} deletado com sucesso (se existia).")
    except Exception as e:
        print(f"❌ Erro ao deletar usuário: {e}")

# --- Função Principal do Menu ---
def executar_menu_crud():
    """Função principal que executa o menu CRUD."""
    # Instancia o DAO (Data Access Object)
    # Este objeto será usado por todas as operações do CRUD
    dao = UsuarioDAO()

    # Exemplo inicial: Adicionar um usuário para ter dados para manipular (opcional)
    # Se o banco já tiver dados ou você não quiser isso, pode remover.
    # print("Configurando dados iniciais (apenas para demonstração)...")
    # usuario_exemplo = Usuario(nome="Carlos Antunes", email="carlos.antunes@example.com")
    # try:
    #     dao.criar(usuario_exemplo)
    # except Exception:
    #     pass # Pode já existir, ou erro na criação silenciosa aqui.

    while True:
        escolha = mostrar_menu_opcoes()

        if escolha == '1':
            criar_novo_usuario(dao)
        elif escolha == '2':
            listar_todos_usuarios(dao)
        elif escolha == '3':
            atualizar_dados_usuario(dao)
        elif escolha == '4':
            deletar_um_usuario(dao)
        elif escolha == '5':
            print("🚪 Saindo do sistema...")
            break
        else:
            print("⚠️ Opção inválida. Por favor, tente novamente.")
        
        input("\nPressione Enter para continuar...") # Pausa para o usuário ler a saída

    # Fecha a conexão com o banco de dados ao sair do loop
    dao.fechar_conexao()
    print("Conexão com o banco de dados fechada.")

# --- Ponto de Entrada da Aplicação ---
if __name__ == "__main__":
    # Para este script funcionar, você precisa ter os arquivos:
    # 1. usuario.py: com a definição da classe Usuario.
    #    Exemplo de Usuario em usuario.py:
    #    class Usuario:
    #        def __init__(self, id=None, nome=None, email=None):
    #            self.id = id
    #            self.nome = nome
    #            self.email = email
    #
    #        def __str__(self):
    #            # O ID pode ser None antes de ser inserido no banco e o DAO atribuir um
    #            id_display = self.id if self.id is not None else "N/A"
    #            return f"ID: {id_display}, Nome: {self.nome}, Email: {self.email}"

    # 2. usuario_dao.py: com a definição da classe UsuarioDAO, que lida com a persistência
    #    (ex: conexão com SQLite, criação de tabela, e os métodos criar, listar, etc.).
    
    print("Bem-vindo ao sistema de Gerenciamento de Usuários!")
    executar_menu_crud()