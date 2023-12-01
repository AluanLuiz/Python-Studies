import tkinter as tk

def clique_do_botao():
    label.config(text="Olá, mundo!")

# Criar uma janela
janela = tk.Tk()

# Definir o tamanho da janela
largura = 400
altura = 300
posicao_x = (janela.winfo_screenwidth() - largura) // 2
posicao_y = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

janela.title("Teste")

# Adicionar um rótulo à janela
label = tk.Label(janela, text="Bem-vindo ao meu software!")
label.pack()

# Adicionar um botão à janela
botao = tk.Button(janela, text="Clique em mim!", 
                  command=clique_do_botao)
botao.pack()

# Iniciar o loop principal da interface gráfica
janela.mainloop()
