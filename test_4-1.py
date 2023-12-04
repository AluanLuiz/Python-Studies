#2023-12-04
#Lista de Tarefas com Banco de Dados simples.

import tkinter as tk 
from tkinter import messagebox
from datetime import datetime
import sqlite3 as sql

# ---------------------------------------------------------------------

class Lista_Tarefas:
    def __init__(self, app):
        self.app = app
        self.app.geometry("400x300")
        self.app.title("Lista de Tarefas")
        
        self.conexao = sql.connect("lista_tarefas.db")
        self.criar_tabela()
        
        self.lista_tarefas = []
        
        self.task_desc = tk.Entry(app, width=50)
        self.task_desc.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn_adicionar = tk.Button(app, text="Adicionar", command=self.adicionar_task)
        self.btn_adicionar.grid(row=0, column=1, padx=10, pady=10)
        
        self.listBox = tk.Listbox(app, selectmode=tk.BROWSE, height=10, width=50)
        self.listBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.btn_deletar = tk.Button(app, text="Deletar", command=self.deletar_task)
        self.btn_deletar.grid(row=2, column=0, padx=10, pady=10)

        self.btn_finalizar = tk.Button(app, text="Finalizar", command=self.finalizar_task)
        self.btn_finalizar.grid(row=2, column=1, padx=10, pady=10)

        self.atualizar_listbox()
    #------------------------------------------
    
    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS lista_tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tarefa TEXT NOT NULL,
                    data_hora TEXT NOT NULL
                )
            ''')
        self.conexao.commit()
     
    #------------------------------------------
       
    def adicionar_task(self):
        tarefa = self.task_desc.get()
        if tarefa:
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tarefa_com_data = f"{tarefa} ({data_hora_atual})"
            self.lista_tarefas.append(tarefa_com_data)

            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO lista_tarefas (tarefa, data_hora) VALUES (?, ?)", (tarefa, data_hora_atual))
            self.conexao.commit()
            
            self.atualizar_listbox()
            self.task_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa para adicionar.")

    #------------------------------------------
    
    def deletar_task(self):
        selecionado = self.listBox.curselection()
        if selecionado:
            index = selecionado[0]
            del self.lista_tarefas[index]
            self.atualizar_listbox()

    #------------------------------------------
    
    def finalizar_task(self):
        selecionado = self.listBox.curselection()
        if selecionado:
            index = selecionado[0]
            tarefa_concluida = self.lista_tarefas.pop(index)
            self.lista_tarefas.append(f"{tarefa_concluida} - Concluída")
            self.atualizar_listbox()

    #------------------------------------------

    def atualizar_listbox(self):
        self.listBox.delete(0, tk.END)

        cursor = self.conexao.cursor()
        cursor.execute("SELECT tarefa, data_hora FROM lista_tarefas")
        registros = cursor.fetchall()

        for registro in registros:
            tarefa_formatada = self.formatar_tarefa(registro)
            self.lista_tarefas.append(registro)
            self.listBox.insert(tk.END, tarefa_formatada)
    
    #------------------------------------------
    
    def formatar_tarefa(self, tarefa):
        return f"{tarefa[0]}, {tarefa[1]}"\
            
# ---------------------------------------------------------------------

app = tk.Tk()
Jan = Lista_Tarefas(app)

app.mainloop()