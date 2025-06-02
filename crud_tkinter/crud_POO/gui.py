import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from usuario import Usuario #
from usuario_dao import UsuarioDAO #

class CrudApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Gerenciador de Usuários Pro")
        self.root.geometry("750x650") # Aumentei um pouco para o campo de pesquisa

        self.light_theme_name = "arc"
        self.dark_theme_name = "equilux"
        self.current_theme_is_dark = False
        self.root.set_theme(self.light_theme_name)

        self.all_users_list = [] # Para armazenar todos os usuários para filtragem

        try:
            self.dao = UsuarioDAO() #
        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco: {e}")
            self.root.destroy()
            return

        self.style = ttk.Style()
        self.setup_global_styles()

        content_frame = ttk.Frame(self.root, padding="10 10 10 10")
        content_frame.pack(expand=True, fill="both")

        header_frame = ttk.Frame(content_frame)
        header_frame.pack(fill='x', pady=(0, 15))
        app_title_label = ttk.Label(header_frame, text="Gerenciamento de Usuários", font=('Segoe UI', 18, 'bold'))
        app_title_label.pack(side='left', padx=5)
        self.theme_toggle_button = ttk.Button(header_frame, text="🌙", command=self.toggle_theme, width=3, style="Toggle.TButton")
        self.theme_toggle_button.pack(side='right', padx=5, pady=5)

        self.input_frame = ttk.LabelFrame(content_frame, text="Dados do Usuário", padding="15 15 15 15")
        self.input_frame.pack(padx=10, pady=10, fill="x")
        # ... (código dos campos de ID, Nome, Email igual ao anterior) ...
        ttk.Label(self.input_frame, text="ID:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        self.id_entry = ttk.Entry(self.input_frame, state="readonly", width=45)
        self.id_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        ttk.Label(self.input_frame, text="Nome:").grid(row=1, column=0, padx=5, pady=10, sticky="w")
        self.nome_entry = ttk.Entry(self.input_frame, width=45)
        self.nome_entry.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        ttk.Label(self.input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.email_entry = ttk.Entry(self.input_frame, width=45)
        self.email_entry.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.input_frame.columnconfigure(1, weight=1)


        self.button_frame = ttk.Frame(content_frame, padding="10 0 10 0")
        self.button_frame.pack(pady=15)
        # ... (código dos botões Criar, Atualizar, Deletar, Limpar igual ao anterior) ...
        self.create_button = ttk.Button(self.button_frame, text="Criar Usuário", command=self.criar_usuario)
        self.create_button.grid(row=0, column=0, padx=10, pady=5)

        self.update_button = ttk.Button(self.button_frame, text="Atualizar Usuário", command=self.atualizar_usuario)
        self.update_button.grid(row=0, column=1, padx=10, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Deletar Usuário", command=self.deletar_usuario)
        self.delete_button.grid(row=0, column=2, padx=10, pady=5)

        self.clear_button = ttk.Button(self.button_frame, text="Limpar Campos", command=self.limpar_campos_e_foco_pesquisa)
        self.clear_button.grid(row=0, column=3, padx=10, pady=5)


        # --- Frame de Pesquisa ---
        search_frame = ttk.Frame(content_frame, padding="5 0 5 0")
        search_frame.pack(fill="x", padx=10, pady=(5,0))

        ttk.Label(search_frame, text="Pesquisar:", font=('Segoe UI', 10, 'italic')).pack(side="left", padx=(0,5))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.on_search_change) # Chama on_search_change a cada alteração
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=50)
        self.search_entry.pack(side="left", expand=True, fill="x", padx=(0,5))
        
        self.clear_search_button = ttk.Button(search_frame, text="Limpar Pesquisa", command=self.clear_search_field, style="Toggle.TButton")
        self.clear_search_button.pack(side="left")


        # --- Treeview Frame ---
        self.tree_frame = ttk.Frame(content_frame)
        self.tree_frame.pack(padx=10, pady=(5,10), fill="both", expand=True)
        # ... (código da Treeview e scrollbars igual ao anterior) ...
        self.tree_scroll_y = ttk.Scrollbar(self.tree_frame, orient="vertical")
        self.tree_scroll_y.pack(side="right", fill="y")
        
        self.tree_scroll_x = ttk.Scrollbar(self.tree_frame, orient="horizontal")
        self.tree_scroll_x.pack(side="bottom", fill="x")

        self.user_tree = ttk.Treeview(
            self.tree_frame,
            columns=("id", "nome", "email"),
            show="headings",
            yscrollcommand=self.tree_scroll_y.set,
            xscrollcommand=self.tree_scroll_x.set
        )
        self.tree_scroll_y.config(command=self.user_tree.yview)
        self.tree_scroll_x.config(command=self.user_tree.xview)

        self.user_tree.heading("id", text="ID")
        self.user_tree.heading("nome", text="Nome Completo")
        self.user_tree.heading("email", text="Endereço de E-mail")

        self.user_tree.column("id", width=70, anchor="center", stretch=tk.NO)
        self.user_tree.column("nome", width=250)
        self.user_tree.column("email", width=300)

        self.user_tree.pack(fill="both", expand=True)
        self.user_tree.bind("<<TreeviewSelect>>", self.carregar_dados_selecionados)


        self.status_bar_frame = ttk.Frame(self.root, relief=tk.SUNKEN, padding=(2,2))
        self.status_bar_frame.pack(side=tk.BOTTOM, fill="x")
        self.status_bar = ttk.Label(self.status_bar_frame, text="Pronto", anchor="w")
        self.status_bar.pack(fill="x", padx=5)

        self.carregar_e_exibir_usuarios() # Carrega todos os usuários e aplica filtro inicial
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    def setup_global_styles(self): # Igual ao anterior
        default_font_family = 'Segoe UI'
        base_font_size = 10
        heading_font_size = 11
        self.style.configure('.', font=(default_font_family, base_font_size))
        self.style.configure('TLabel', padding=5)
        self.style.configure('Treeview', rowheight=28)
        self.style.configure('Treeview.Heading', font=(default_font_family, heading_font_size, 'bold'), padding=5)
        self.style.configure('TButton', padding=(10, 6), font=(default_font_family, base_font_size, 'bold'))
        self.style.configure("Toggle.TButton", font=(default_font_family, 10), padding=(5,5))
        self.style.configure('TEntry', padding=(5,5))

    def toggle_theme(self): # Igual ao anterior
        self.current_theme_is_dark = not self.current_theme_is_dark
        if self.current_theme_is_dark:
            self.root.set_theme(self.dark_theme_name)
            self.theme_toggle_button.config(text="☀️")
            self.set_status(f"Tema alterado para: {self.dark_theme_name}")
        else:
            self.root.set_theme(self.light_theme_name)
            self.theme_toggle_button.config(text="🌙")
            self.set_status(f"Tema alterado para: {self.light_theme_name}")

    def set_status(self, message): # Igual ao anterior
        self.status_bar.config(text=message)

    def limpar_campos_e_foco_pesquisa(self):
        """ Limpa os campos de dados e foca no campo de pesquisa. """
        self.limpar_campos_dados()
        self.search_entry.focus_set() # Foca no campo de pesquisa
        self.set_status("Campos limpos. Foco na pesquisa.")

    def limpar_campos_dados(self):
        """ Limpa apenas os campos de ID, Nome e Email. """
        self.id_entry.config(state="normal")
        self.id_entry.delete(0, tk.END)
        self.id_entry.config(state="readonly")
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        if self.user_tree.selection():
            self.user_tree.selection_remove(self.user_tree.selection())
        # self.set_status("Campos de dados limpos.") # Status será definido pela função chamadora

    def validar_campos(self): # Igual ao anterior
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        if not nome:
            messagebox.showwarning("Campo Obrigatório", "O campo 'Nome Completo' é obrigatório.", parent=self.root)
            self.nome_entry.focus()
            return False
        if not email:
            messagebox.showwarning("Campo Obrigatório", "O campo 'Endereço de E-mail' é obrigatório.", parent=self.root)
            self.email_entry.focus()
            return False
        if "@" not in email or "." not in email.split('@')[-1]:
            messagebox.showwarning("Email Inválido", "Por favor, insira um endereço de e-mail válido.", parent=self.root)
            self.email_entry.focus()
            return False
        return True

    def carregar_e_exibir_usuarios(self):
        """ Carrega todos os usuários do DAO e atualiza a Treeview aplicando o filtro. """
        try:
            self.all_users_list = self.dao.listar() or [] #
            self.filtrar_e_atualizar_treeview() # Aplica o filtro atual (ou mostra todos)
        except Exception as e:
            messagebox.showerror("Erro ao Carregar", f"Não foi possível carregar os usuários: {e}", parent=self.root)
            self.all_users_list = [] # Garante que a lista esteja vazia em caso de erro
            self.filtrar_e_atualizar_treeview() # Tenta atualizar a treeview mesmo vazia
            self.set_status("Erro ao carregar usuários.")

    def on_search_change(self, *args):
        """ Chamado quando o texto no campo de pesquisa muda. """
        self.filtrar_e_atualizar_treeview()

    def clear_search_field(self):
        """ Limpa o campo de pesquisa e atualiza a treeview. """
        self.search_var.set("") # Isso vai disparar on_search_change e atualizar a treeview
        self.search_entry.focus_set()
        self.set_status("Pesquisa limpa. Exibindo todos os usuários.")


    def filtrar_e_atualizar_treeview(self):
        """Filtra self.all_users_list com base no search_entry e atualiza a Treeview."""
        search_term = self.search_var.get().lower().strip()

        # Limpa a Treeview antes de adicionar novos itens
        for i in self.user_tree.get_children():
            self.user_tree.delete(i)

        if not search_term:
            display_list = self.all_users_list
            count = len(display_list)
            self.set_status(f"{count} usuário(s) listado(s).")
        else:
            display_list = [
                user for user in self.all_users_list
                if search_term in user.nome.lower() or \
                   search_term in user.email.lower() or \
                   search_term == str(user.id) # Permite pesquisar por ID também
            ]
            count = len(display_list)
            self.set_status(f"{count} usuário(s) encontrado(s) para '{search_term}'.")
        
        for usuario in display_list:
            self.user_tree.insert("", tk.END, values=(usuario.id, usuario.nome, usuario.email))

    def criar_usuario(self):
        if not self.validar_campos():
            return
        # ... (lógica de criar igual, mas no final chama carregar_e_exibir_usuarios) ...
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        novo_usuario = Usuario(nome=nome, email=email) #
        try:
            self.dao.criar(novo_usuario) #
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!", parent=self.root)
            self.limpar_campos_dados()
            self.carregar_e_exibir_usuarios() # Recarrega e atualiza a treeview
            self.set_status("Usuário criado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro ao Criar", f"Não foi possível criar o usuário: {e}", parent=self.root)
            self.set_status("Erro ao criar usuário.")


    def carregar_dados_selecionados(self, event=None): # Igual ao anterior
        try:
            selected_item = self.user_tree.selection()
            if not selected_item:
                return
            item_values = self.user_tree.item(selected_item[0], "values")
            self.id_entry.config(state="normal")
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, str(item_values[0]))
            self.id_entry.config(state="readonly")
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(0, str(item_values[1]))
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, str(item_values[2]))
            self.set_status(f"Usuário ID {item_values[0]} selecionado.")
        except IndexError:
            self.set_status("Erro ao carregar seleção.")
        except Exception as e:
            self.set_status(f"Erro inesperado ao carregar dados: {e}")

    def atualizar_usuario(self):
        if not self.id_entry.get(): # Verifica se um usuário está selecionado (ID preenchido)
            messagebox.showwarning("Seleção Necessária", "Selecione um usuário da lista para atualizar.", parent=self.root)
            return
        if not self.validar_campos():
            return
        # ... (lógica de atualizar igual, mas no final chama carregar_e_exibir_usuarios) ...
        id_usuario = int(self.id_entry.get())
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        usuario_atualizado = Usuario(id=id_usuario, nome=nome, email=email) #
        try:
            self.dao.atualizar(usuario_atualizado) #
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!", parent=self.root)
            self.limpar_campos_dados()
            self.carregar_e_exibir_usuarios() # Recarrega e atualiza a treeview
            self.set_status(f"Usuário ID {id_usuario} atualizado.")
        except Exception as e:
            messagebox.showerror("Erro ao Atualizar", f"Não foi possível atualizar o usuário: {e}", parent=self.root)
            self.set_status("Erro ao atualizar usuário.")


    def deletar_usuario(self):
        if not self.id_entry.get(): # Verifica se um usuário está selecionado
            messagebox.showwarning("Seleção Necessária", "Selecione um usuário da lista para deletar.", parent=self.root)
            return
        # ... (lógica de deletar igual, mas no final chama carregar_e_exibir_usuarios) ...
        id_val = self.id_entry.get()
        nome_val = self.nome_entry.get() 
        confirm_message = f"Tem certeza que deseja deletar o usuário '{nome_val}' (ID: {id_val})?"
        if not messagebox.askyesno("Confirmar Deleção", confirm_message, icon='warning', parent=self.root):
            self.set_status("Deleção cancelada pelo usuário.")
            return
        try:
            id_usuario = int(id_val)
            self.dao.deletar(id_usuario) #
            messagebox.showinfo("Sucesso", f"Usuário com ID {id_usuario} deletado com sucesso!", parent=self.root)
            self.limpar_campos_dados()
            self.carregar_e_exibir_usuarios() # Recarrega e atualiza a treeview
            self.set_status(f"Usuário ID {id_usuario} deletado.")
        except Exception as e:
            messagebox.showerror("Erro ao Deletar", f"Não foi possível deletar o usuário: {e}", parent=self.root)
            self.set_status("Erro ao deletar usuário.")


    def fechar_janela(self): # Igual ao anterior
        if messagebox.askokcancel("Sair", "Deseja realmente sair do sistema?", icon='question', parent=self.root):
            try:
                if hasattr(self, 'dao') and self.dao:
                    self.dao.fechar_conexao() #
                self.set_status("Conexão com o banco de dados fechada.")
            except Exception as e:
                self.set_status(f"Erro ao fechar conexão: {e}")
            finally:
                self.root.destroy()

if __name__ == "__main__":
    main_window = ThemedTk()
    app = CrudApp(main_window)
    main_window.mainloop()