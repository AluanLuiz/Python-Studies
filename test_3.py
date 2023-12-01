#2023-12-01
#Embaralhador de senha

import tkinter as tk
from tkinter import messagebox
import random as rd

#------------------------------------------------------------

def embaralhar_senha():
    senha_origin = textBox.get()
    
    if senha_origin:
        lista_senha = list(senha_origin)
        rd.shuffle(lista_senha)
        senha_mess = ''.join(lista_senha)
        
        messagebox.showinfo("Senha Embaralhada", f"Senha Original: {senha_origin}\nSenha Embaralhada: {senha_mess}")
        
    else:
        messagebox.showwarning("Aviso", "Digite uma senha antes de embaralhar.")

#------------------------------------------------------------

janela = tk.Tk()
janela.geometry('450x200')

janela.title('Senha embaralhada')

label = tk.Label(janela, text="Digite a senha para embaralhar: ")
label.pack(pady=8)

textBox = tk.Entry(janela, show="*")
textBox.pack(pady=5)

convert = tk.Button(janela, text="Embaralhar", command= embaralhar_senha)
convert.pack(pady=5)

janela.mainloop()