
from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("300x400")
root.title("Aplicação")
root.config(bg="black")
label = tk.Label(
    text = "Olá, Seja Bem Vindo!",
    bg = "black",
    fg = "green",
    font = 20,
    width = 30,
    height = 5
)
label.pack()

#CAMPO NOME
label = tk.Label(
    text = "Nome:",
)
entry = tk.Entry(width = 50)
label.pack()
entry.pack(pady=(5,5))

#CAMPO EMAILL
email = tk.Label(
    text = "Email:",
)
entry = tk.Entry(width = 50)
email.pack()
entry.pack(pady=(5,5))

#BOTAO LOGIN
botao = tk.Button(
    root, 
    text = "Login",
    width = 6,
    height  = 2,
    bg = "green",
    fg = "black"
)
botao.pack(pady = (10,5))



#Inicia o Programa
root.mainloop()