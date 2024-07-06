import tkinter as tk
from tkinter import messagebox as msg
import pyperclip #!pip3 install pyperclip

#-----------------------------

class Cripto:
    def __init__(self, master):
        self.crip = master
        self.crip.title("Criptografia Simples.")
        
        self.crip.grid_rowconfigure(5, weight=2)
        self.crip.grid_columnconfigure((0,1,2,3,4), weight=1)
        
        self.font1 = ("Arial", 14)
        self.font2 = ("Arial", 10)
        
        self.desc_lbl = tk.Label(self.crip, font=self.font2, text="Digite abaixo, para criptografar ou descriptografar um texto.")
        self.desc_lbl.grid(row=0, column=0, columnspan=5 ,padx=5, pady=5)
        
        self.text_ent =  tk.Entry(self.crip, font=self.font1, width=40)
        self.text_ent.grid(row=1, column=0, columnspan=5 ,padx=5, pady=5)
        
        self.cript_bt = tk.Button(self.crip, font=self.font1,  text="Criptografar \n Texto", height=2, width=14, 
                                  highlightthickness=2, bd=2, command=self.criptografar)
        self.cript_bt.grid(row=2, column=0,padx=10, pady=5)
        
        self.descript_bt = tk.Button(self.crip, font=self.font1,  text="Descriptografar \n Texto", height=2, width=14, 
                                     highlightthickness=2, bd=2, command=self.descriptografar)
        self.descript_bt.grid(row=2, column=4,padx=10, pady=5)
        
        self.exit_bt = tk.Button(self.crip, font=self.font1, text="Sair", height=1, width=10 ,command=self.exit)
        self.exit_bt.grid(row=5, column=4, padx=2, pady=5)
        
        self.text_lbl = tk.Label(self.crip, font=self.font1, text="----Texto convertido----")
        self.text_lbl.grid(row=5, column=0, columnspan=3, padx=2, pady=5)
        self.text_lbl.bind("<Button-1>", self.copy_to_clipboard)
    
    #--------
    
    def exit(self):
        self.crip.destroy()
        
    #--------
    
    def criptografar(self):
        texto = self.text_ent.get()
        
        substituicoes = {'A': 'あ', 'B': 'い', 'C': 'う', 'D': 'え', 'E': 'お', 'F': 'か', 'G': 'き', 'H': 'く', 'I': 'け', 'J': 'こ',
                     'K': 'さ', 'L': 'し', 'M': 'す', 'N': 'せ', 'O': 'そ', 'P': 'た', 'Q': 'ち', 'R': 'つ', 'S': 'て', 'T': 'と',
                     'U': 'な', 'V': 'に', 'W': 'ぬ', 'X': 'ね', 'Y': 'の', 'Z': 'ん', 
                     '1':'一', '2':'二', '3':'二', '4':'四', '5':'五', '6':'六', '7':'七', '8':'八', '9':'九', '0':'〇'}
        
        texto_criptografado = ''.join(substituicoes.get(letra.upper(), letra) for letra in texto)
        self.text_lbl.config(text=f"{texto_criptografado}")
        #msg.showinfo("Texto Criptografado", texto_criptografado)
    
    #--------
    
    def descriptografar(self):
        texto = self.text_ent.get()
        substituicoes = {'あ': 'A', 'い': 'B', 'う': 'C', 'え': 'D', 'お': 'E', 'か': 'F', 'き': 'G', 'く': 'H', 'け': 'I', 'こ': 'J',
                     'さ': 'K', 'し': 'L', 'す': 'M', 'せ': 'N', 'そ': 'O', 'た': 'P', 'ち': 'Q', 'つ': 'R', 'て': 'S', 'と': 'T',
                     'な': 'U', 'に': 'V', 'ぬ': 'W', 'ね': 'X', 'の': 'Y', 'ん': 'Z',
                     '一':'1', '二':'2', '二':'3', '四':'4', '五':'5', '六':'6', '七':'7', '八':'8', '九':'9', '〇':'0'}
    
        texto_descriptografado = ''.join(substituicoes.get(letra, letra) for letra in texto)
        self.text_lbl.config(text=f"{texto_descriptografado}")
        #msg.showinfo("Texto Descriptografado", texto_descriptografado)
     
    #--------
    
    def copy_to_clipboard(self, event):
        # Copia o texto da label para a área de transferência
        pyperclip.copy(self.text_lbl.cget("text"))
        msg.showinfo("Copiado", "Texto copiado para a área de transferência.")
    
#-----------------------------
        
app = tk.Tk()
app.geometry("500x200")
Jan = Cripto(app)

app.mainloop()