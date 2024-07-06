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
        self.app.geometry("400x350")
        self.app.title("Lista de Tarefas")
        
        self.conexao = sql.connect("lista_tarefas.db")
        self.criar_tabela()
        
        self.task_desc = tk.Entry(app, width=50)
        self.task_desc.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn_adicionar = tk.Button(app, text="Adicionar", command=self.adicionar_task)
        self.btn_adicionar.grid(row=0, column=1, padx=10, pady=10)
        
        self.listBox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=50)
        self.listBox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.btn_deletar = tk.Button(app, text="Deletar", command=self.deletar_task)
        self.btn_deletar.grid(row=2, column=0, padx=10, pady=10)

        self.btn_finalizar = tk.Button(app, text="Finalizar", command=self.finalizar_task)
        self.btn_finalizar.grid(row=2, column=1, padx=10, pady=10)
        
        self.btn_reload = tk.Button(app, text="atualizar", command=self.atualizar_listbox)
        self.btn_reload.grid(row=3, column=1, padx=10, pady=10)

        self.atualizar_listbox()
    
    #------------------------------------------
       
    def adicionar_task(self):
        tarefa = self.task_desc.get()
        if tarefa:
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M")

            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO lista_tarefas (tarefa, data_hora) VALUES (?, ?)", (tarefa, data_hora_atual))
            self.conexao.commit()
            
            self.atualizar_listbox()
            self.task_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa para adicionar.")

    #------------------------------------------
    
    def deletar_task(self):
        tarefa_id = self.obter_id()

        if tarefa_id is not None:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM lista_tarefas WHERE id = ?", (tarefa_id,))
            self.conexao.commit()
            self.atualizar_listbox()
        else:
            messagebox.showwarning("Aviso", "Selecione um item para deletar.")
            
    #------------------------------------------
    
    def finalizar_task(self):
        tarefa_id = self.obter_id()

        if tarefa_id is not None:
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M")
        
            cursor = self.conexao.cursor()
            cursor.execute("SELECT tarefa FROM lista_tarefas WHERE id = ?", (tarefa_id,))
            tarefa_original = cursor.fetchone()[0]

            tarefa_finalizada = f"{tarefa_original} - Finalizada em {data_hora_atual}"

            cursor.execute("UPDATE lista_tarefas SET tarefa = ?, data_hora = ? WHERE id = ?", (tarefa_finalizada, data_hora_atual, tarefa_id))
            self.conexao.commit()

            self.atualizar_listbox()
        else:
            messagebox.showwarning("Aviso", "Selecione um item para finalizar.")
        
    #------------------------------------------

    def atualizar_listbox(self):
        self.listBox.delete(0, tk.END)

        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, tarefa, data_hora FROM lista_tarefas")
        registros = cursor.fetchall()

        for registro in registros:
            tarefa_formatada = self.formatar_tarefa(registro)
            self.listBox.insert(tk.END, tarefa_formatada)
    
    #------------------------------------------
    
    def formatar_tarefa(self, tarefa):
        return f"{tarefa[0]}, {tarefa[1]}, {tarefa[2]}"\
            
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
    
    def obter_id(self):
        selecionado_indices = self.listBox.curselection()

        if selecionado_indices:
            index = selecionado_indices[0]
            tarefa_selecionada = self.listBox.get(index).split(", ")[0]

            cursor = self.conexao.cursor()
            cursor.execute("SELECT id FROM lista_tarefas WHERE id = ?", (tarefa_selecionada,))
            tarefa_id = cursor.fetchone()

            if tarefa_id:
                return tarefa_id[0]
            else:
                print(f"Tarefa selecionada: {tarefa_selecionada}")
                print("ID não encontrado no banco de dados.")
                return None
        else:
            print("Nenhum item selecionado.")
            return None
             
# ---------------------------------------------------------------------

app = tk.Tk()
Jan = Lista_Tarefas(app)

app.mainloop()