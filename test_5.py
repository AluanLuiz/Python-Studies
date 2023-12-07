#2023-12-06
#Controle de Estoque, com bd

import tkinter as tk
from tkinter import messagebox
from tkinter import font
import sqlite3 as sql
#import os "Ative se quiser verificar pelo terminal o reload -1"

#- Início da classe ControleEstoque -----------------------------------------

class ControleEstoque:
    def __init__(self,master):
        self.master = master
        
        self.master.title("Controle de Estoque")
        
        self.conexao = sql.connect("armazem.db")
        self.criar_tabela()
        
        self.start_timer()
        
        self.font_1 = font.Font(family="Arial", size=16)
        self.font_2 = font.Font(family="Arial", size=14)
        self.font_3 = font.Font(family="Arial", size=10)


        self.title = tk.Label(master, text="Controle de Estoque", font=self.font_1)
        self.title.grid(row=0, column=1, columnspan=2, pady=10)

        self.bt_cadProdut = tk.Button(master, text="Cadastrar Produto", font=self.font_2, command=self.forms_CadProd)
        self.bt_cadProdut.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.bt_volVendas = tk.Button(master, text="Volume de Vendas", font=self.font_2, command=self.grafic_vendas)
        self.bt_volVendas.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

        self.listViewer = tk.Listbox(master, selectmode=tk.MULTIPLE, height=20, width=88, font=self.font_3)
        self.listViewer.grid(row=2, column=1, columnspan=3, padx=15, pady=10)

        self.bt_reload = tk.Button(master, text="Atualizar  ", font=self.font_2, command=self.load_listview)
        self.bt_reload.grid(row=3, column=2, pady=10)
        self.bt_darBaixa = tk.Button(master, text="Dar Baixa", font=self.font_2, command=self.saidaProdut)
        self.bt_darBaixa.grid(row=3, column=3, pady=10)
        
        self.load_listview()
          
    #------------------------------------------
    
    def forms_CadProd(self):
        cad_produt = tk.Toplevel(self.master)
        cadProdut_Forms = CadastroProduto(cad_produt)

    #------------------------------------------
    
    def grafic_vendas(self):
        print(f"Botão funcionando 2")

    #------------------------------------------
    
    def saidaProdut(self):
        print(f"Botão funcionando 3")
                
    #------------------------------------------
    
    def load_listview(self):
        self.listViewer.delete(0, tk.END)
        
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, cod_barras, nome_produto, quant_dispon, valor_venda, fornecedor, valor_fornecedor FROM estoque")
        registros = cursor.fetchall() 
        
        for registro in registros:
            info_produt = self.formatar_info(registro)
            self.listViewer.insert(tk.END, info_produt)
            #print(info_produt) -1
                        
    def formatar_info(self, item):
        return f"{item[0]}, {item[1]} - {item[2]}, Disponível: {item[3]}, R${item[4]} - {item[5]}, ultímo preço R${item[6]}"\
    
    #------------------------------------------
    
    def start_timer(self, interval_ms=5000):
        self.master.after(interval_ms, self.reload_listview)
    
    def reload_listview(self):
        #self.clear_terminal() -1
        self.load_listview()
        self.start_timer()
    
    #------------------------------------------
    
    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS estoque (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           nome_produto TEXT NOT NULL,
                           cod_barras TEXT CHECK(LENGTH(cod_barras) = 13),
                           quant_dispon INTERGER NOT NULL,
                           valor_venda REAL NOT NULL,
                           fornecedor TEXT NOT NULL,
                           valor_fornecedor REAL NOT NULL
                        )
                    ''')
        self.conexao.commit()

    #------------------------------------------
  
    # def clear_terminal(self): Utíl para manutenção e/ou verificação do banco -1
    #     os.system('cls' if os.name == 'nt' else 'clear') -1
    
#- Fim da classe ControleEstoque -----------------------------------------

#- Início da classe CadastroProduto -----------------------------------------

class CadastroProduto:
    def __init__(self, cad):   
        self.cad = cad
        self.cad.geometry("430x350")
        self.cad.title("Cadastro de Produto")
        
        self.conexao = sql.connect("armazem.db")

        self.font_2 = font.Font(family="Arial", size=14)

        self.lbl_nome = tk.Label(cad, text="Nome do Produto:", font=self.font_2)
        self.lbl_nome.grid(row=0, column=0, padx=10, pady=10)
        self.txt_nome = tk.Entry(cad)
        self.txt_nome.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_codBarras = tk.Label(cad, text="Código de Barras do Produto:", font=self.font_2)
        self.lbl_codBarras.grid(row=1, column=0, padx=10, pady=10)
        self.txt_codBarras = tk.Entry(cad)
        self.txt_codBarras.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_quant = tk.Label(cad, text="Quantidade Disponível:", font=self.font_2)
        self.lbl_quant.grid(row=2, column=0, padx=10, pady=10)
        self.txt_quant = tk.Entry(cad)
        self.txt_quant.grid(row=2, column=1, padx=10, pady=10)
        
        self.lbl_valorVenda = tk.Label(cad, text="Valor de Venda: R$", font=self.font_2)
        self.lbl_valorVenda.grid(row=3, column=0, padx=10, pady=10)
        self.txt_valorVenda = tk.Entry(cad)
        self.txt_valorVenda.grid(row=3, column=1, padx=10, pady=10)
        
        self.lbl_fornecedor = tk.Label(cad, text="Fornecedor:", font=self.font_2)
        self.lbl_fornecedor.grid(row=4, column=0, padx=10, pady=10)
        self.txt_fornecedor = tk.Entry(cad)
        self.txt_fornecedor.grid(row=4, column=1, padx=10, pady=10)
        
        self.lbl_valorFornec = tk.Label(cad, text="Valor do fornecedor: R$", font=self.font_2)
        self.lbl_valorFornec.grid(row=5, column=0, padx=10, pady=10)
        self.txt_valorFornec = tk.Entry(cad)
        self.txt_valorFornec.grid(row=5, column=1, padx=10, pady=10)
        
        self.btn_salvar = tk.Button(cad, text="Salvar", font=self.font_2, command=self.salvar_produto)
        self.btn_salvar.grid(row=6, column=1, columnspan=2, padx=10, pady=10)
        
        self.btn_sair = tk.Button(cad, text="Sair", font=self.font_2, command=self.sair)
        self.btn_sair.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
                     
    #------------------------------------------

    def salvar_produto(self):
        cadastroValido = self.validarCad()
                
        if cadastroValido == "Válido":
            nome_prod = self.txt_nome.get()
            codBarras_prod = self.txt_codBarras.get()
            quant_prod = self.txt_quant.get()
            valorV = self.txt_valorVenda.get()
            fornecedor = self.txt_fornecedor.get()
            valorF = self.txt_valorFornec.get()
            
            cursor = self.conexao.cursor()
                       
            try:
                cursor.execute("INSERT INTO estoque (nome_produto, cod_barras, quant_dispon, valor_venda, fornecedor, valor_fornecedor) VALUES (?, ?, ?, ?, ?, ?)",
                               (nome_prod, codBarras_prod, quant_prod, valorV, fornecedor, valorF))
                self.conexao.commit()
                
                self.txt_nome.delete(0, tk.END)
                self.txt_codBarras.delete(0, tk.END)
                self.txt_quant.delete(0, tk.END)
                self.txt_valorVenda.delete(0, tk.END)
                self.txt_fornecedor.delete(0, tk.END)
                self.txt_valorFornec.delete(0, tk.END)            
            except sql.Error as e:
                print("Erro ao salvar o cadastro do produto:", e)
                messagebox.showerror("Erro", "Não foi possível salvar o cadastro do produto")
                     
    #------------------------------------------

    def validarCad(self):
        nome_prod = self.txt_nome.get()
        codBarras_prod = self.txt_codBarras.get()
        quant_prod = self.txt_quant.get()
        valorV = self.txt_valorVenda.get()
        fornecedor = self.txt_fornecedor.get()
        valorF = self.txt_valorFornec.get()
        
        cursor = self.conexao.cursor()
        
        try:
            
            if nome_prod.strip() == "":
                messagebox.showerror("Erro", "Nome do produto não pode ser vazio")
                return
            
            cursor.execute("SELECT cod_barras FROM estoque WHERE cod_barras = ? ", (codBarras_prod,))
            cod_salvo = cursor.fetchone()
            if cod_salvo and cod_salvo[0] == codBarras_prod:
                messagebox.showerror("Erro", "O Código de Barras já existe.")
                return
                
            elif len(codBarras_prod) != 13:
                messagebox.showerror("Erro", "Código de Barras Invalido")
                return
            
            try:
                quant_prod = int(quant_prod)
                if quant_prod < 0:
                    messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
                return
            
            try:
                valorV = float(valorV)
                if valorV < 0:
                    messagebox.showerror("Erro", "O valor de venda deve ser um número positivo.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "O valor de venda deve ser um número.")
                return
            
            if fornecedor.strip() == "":
                messagebox.showerror("Erro", "Nome do Fornecedor não pode ser vazio")
                return
            
            try:
                valorF = float(valorF)
                if valorF < 0:
                    messagebox.showerror("Erro", "O valor de compra do fornecedor deve ser um número positivo.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "O valor de compra do fornecedor deve ser um número.")
                return
            
        except sql.Error as e:
            print("Erro ao salvar o cadastro do produto:", e)
            messagebox.showerror("Erro", "Não foi possível salvar o cadastro do produto")
            return 
        finally:
            cursor.close()
        
        return "Válido"
    
    #------------------------------------------

    def sair(self):
        self.cad.destroy()

#- Fim da classe CadastroProduto -----------------------------------------
   
if __name__ == "__main__":
    root = tk.Tk()
    app = ControleEstoque(root)
    root.geometry("650x530")
    root.mainloop()