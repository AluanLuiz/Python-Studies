#2023-12-01
#Embaralhador de senha

import tkinter as tk # Importando biblioteca Tkinter
from tkinter import messagebox # Importando o módulo "messagebox", dentro de tkinter
import random as rd # Importando biblioteca random

#------------------------------------------------------------

def embaralhar_senha(): #Função para embaralhar a "senha" digitada pelo usuário
    senha_origin = textBox.get() # A variavel "senha_origin" puxa a informação da variavel "textBox"
    
    if senha_origin: # Se tiver alguma informação dentro de "senha_origin"
        lista_senha = list(senha_origin) # Lista todos os caracteres individualmente
        rd.shuffle(lista_senha) # Embaralha os caracteres listados
        senha_mess = ''.join(lista_senha) # Junta os caracteres embaralhados e atribui a váriavel "senha_mess"
        
        # Exibe um caixa de mensagem, exemplo "Senha Embaralhada, Senha Original: 12345, Senha Embaralhada: 45213"
        messagebox.showinfo("Senha Embaralhada", f"Senha Original: {senha_origin}\nSenha Embaralhada: {senha_mess}")
        
    else: # Se não, exibe a mensagem de aviso
        messagebox.showwarning("Aviso", "Digite uma senha antes de embaralhar.")
        
#------------------------------------------------------------

janela = tk.Tk() # Cria a janela
janela.geometry('450x200') # Define o tamanho da janela, largura x altura

janela.title('Senha embaralhada') # Titulo da janela

# Widgets ...

label = tk.Label(janela, text="Digite a senha para embaralhar: ") # Texto informando o usuário o que fazer
label.pack(pady=5) # Exibe a "label" na janela, com espaçamento vertical de 5 unidades

textBox = tk.Entry(janela, show="*") # Caixa de texto, onde o usuário irá digitar, os caracteres serão exibidos como *  
textBox.pack(pady=5) # Exibe a "textBox" na janela, com espaçamento vertical de 5 unidades

mess = tk.Button(janela, text="Embaralhar", command=embaralhar_senha) # Botão, indicando a ação, comando chama a função "embaralhar_senha"
mess.pack(pady=5) # Exibe o botão "mess" na janela, com espaçamento vertical de 5 unidades

janela.mainloop() # Inicia o Loop principal

#------------------------------------------------------------