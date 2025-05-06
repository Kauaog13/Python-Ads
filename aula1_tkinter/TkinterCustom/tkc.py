#Importa a Biblioteca Grafica Tkinter Custom
import customtkinter as ctk
ctk.set_appearance_mode('dark')

#Verifica se os campos de login estão preenchidos
def validar_login():
    #Pega os valores dos campos de login
    usuario = campo_user.get()
    senha = campo_pass.get()

    #Valida o usuario e senha
    if usuario == "root" and senha == "1234":
        resultado.configure(text = "Login efetuado com Sucesso!!!", text_color = "green")
    else:
        resultado.configure(text = "Login Inválido!!!", text_color = "red")

#Criar as Funcionalidades
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('500x500')

#CAMPO USER
lab_user = ctk.CTkLabel(app, text = "Usuário")
lab_user.pack(pady = 10)
campo_user = ctk.CTkEntry(app, placeholder_text = "Digite o nome do Usuário", width = 170)
campo_user.pack(pady = 10)

#CAMPO PASS
lab_senha = ctk.CTkLabel(app, text = "Senha")
lab_senha.pack(pady = 10)
campo_pass = ctk.CTkEntry(app, placeholder_text = "Digite a sua Senha", width = 170)
campo_pass.pack(pady = 10)

#BOTÃO LOGIN
botao = ctk.CTkButton(app, text = "Login", command = validar_login)
botao.pack(pady = 10)

#VALIDAR O LOGIN
resultado = ctk.CTkLabel(app, text = "")
resultado.pack(pady = 10)

#Inicia a Aplicação
app.mainloop()