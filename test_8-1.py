import tkinter as tk
from tkinter import messagebox as msg

class Cripte:
    def __init__(self, master):
        self.master = master
        self.master.title("Criptografia 2.0")

        self.frame_campos = tk.Frame(self.master, bg="#B2B3B3")
        self.frame_campos.grid(row=1, column=1, columnspan=4, sticky="ew")
        
        self.frame_btns = tk.Frame(self.master, bg="#B2B3B3")
        self.frame_btns.grid(row=4, column=2, columnspan=2, sticky="s")
        
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.frame_campos.grid_rowconfigure(4, weight=1)
        self.frame_campos.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.frame_btns.grid_rowconfigure(1, weight=1)
        self.frame_btns.grid_columnconfigure((0,1,2), weight=1)
        
        self.campos()
    
    def campos(self):
        self.font_regular = ("Arial", 14)
        self.font_medium = ("Arial", 16)
        self.font_high = ("Arial", 20)
        
        self.lbl_title = tk.Label(self.frame_campos, font=self.font_high, text="Criptografia de chave simétrica.")
        self.lbl_title.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        
        self.lbl_txtOrigin = tk.Label(self.frame_campos, font=self.font_medium, text="Digite o texto para \nser criptografado:")
        self.lbl_txtOrigin.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.lbl_key = tk.Label(self.frame_campos, font=self.font_medium, text="Insira a chave:")
        self.lbl_key.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.lbl_cripted = tk.Label(self.frame_campos, font=self.font_medium, text="Criptografado: ")
        self.lbl_cripted.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
       


def init_cript():
    Cript = tk.Tk()
    app = Cripte(Cript)
    Cript.geometry("800x500")
    Cript.mainloop()
    
init_cript()