# Cifra de césar modificado - Códido de referencia: Julio César,  Código Final: Aluan
#Integrantes do Grupo: Aluan, Daniele, Danilo, Eduardo, Gabriel Toledo, Júlio, João Lucas, Thiago

import tkinter as tk

# Substituições
substituicoes = {
    'A': 'あ', 'B': 'い', 'C': 'う', 'D': 'え', 'E': 'お', 'F': 'か', 'G': 'き', 'H': 'く', 'I': 'け', 'J': 'こ',
    'K': 'さ', 'L': 'し', 'M': 'す', 'N': 'せ', 'O': 'そ', 'P': 'た', 'Q': 'ち', 'R': 'つ', 'S': 'て', 'T': 'と',
    'U': 'な', 'V': 'に', 'W': 'ぬ', 'X': 'ね', 'Y': 'の', 'Z': 'ん', '1': '一', '2': '二', '3': '三', '4': '四',
    '5': '五', '6': '六', '7': '七', '8': '八', '9': '九', '0': '零'
}

substituicoes_inverso = {v: k for k, v in substituicoes.items()}

# Função para cifrar caracteres com cifra de César
def cifrarcesar(texto, shift=3):
    cipher = ''
    for char in texto:
        code = ord(char) + shift
        cipher += chr(code)
    return cipher
 
# Função para decifrar caracteres com cifra de César
def descifrarcesar(texto, shift=3):
    cipher = ''
    for char in texto:
        code = ord(char) - shift
        cipher += chr(code)
    return cipher

# Função de criptografia
def criptografar(texto):
    texto_criptografado = ''.join(substituicoes.get(letra.upper(), letra) for letra in texto)
    texto_criptografado = cifrarcesar(texto_criptografado)
    return texto_criptografado

# Função de descriptografia
def descriptografar(texto_criptografado):
    texto_criptografado = descifrarcesar(texto_criptografado)
    texto = ''.join(substituicoes_inverso.get(letra, letra) for letra in texto_criptografado)
    return texto

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Cifra de César Modificada")
        self.master.geometry("600x420")
        
        self.font1 = ("Arial", 14)

        self.text_input = tk.Text(master, height=5, width=50, font=self.font1)
        self.text_input.pack(pady=10)
        
        self.btn_criptografar = tk.Button(master, text="Criptografar", font=self.font1, command=self.criptografar_texto)
        self.btn_criptografar.pack(pady=5)
        
        self.btn_descriptografar = tk.Button(master, text="Descriptografar", font=self.font1, command=self.descriptografar_texto)
        self.btn_descriptografar.pack(pady=5)
        
        self.text_output = tk.Text(master, height=5, width=50, font=self.font1)
        self.text_output.pack(pady=10)
        
        self.btn_limpar = tk.Button(master, text="Limpar", font=self.font1, command=self.limpar_texto)
        self.btn_limpar.pack(pady=5)

    def criptografar_texto(self):
        texto = self.text_input.get("1.0", tk.END).strip()
        texto_cifrado = cifrarcesar(texto)
        texto_criptografado = criptografar(texto_cifrado)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, texto_criptografado)

    def descriptografar_texto(self):
        texto = self.text_output.get("1.0", tk.END).strip()
        texto_descifrado = descriptografar(texto)
        texto_descriptografado = descifrarcesar(texto_descifrado)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, texto_descriptografado)

    def limpar_texto(self):
        self.text_input.delete("1.0", tk.END)
        self.text_output.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()