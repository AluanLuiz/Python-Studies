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


# Informações úteis:

# !-- obs: as palavras em MAIUSCULO abaixo, no código devem ser escritas minusculo --!

# .PACK() : Ajusta o layout
# SIDE: Define a direção na qual o elemento será exibido, (tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT).
# ANCHOR: Especifica onde o elemento deve ser ancorado dentro do espaço disponível , ('n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'center'). 
# respectivamente (North, South, East, West, Northeast, Northwest, Southeast, Southwest, Center)
# FILL: Indica como o elemento deve se expandir para preencher o espaço disponível, ('none', 'x', 'y', 'both')
# EXPAND: Um valor booleano que indica se o elemento deve expandir para ocupar qualquer espaço extra disponível
# IPADX e IPADY: Adiciona espaço interno ao redor do elemento no eixo x ou y
# PADX e PADY: Adiciona espaço externo ao redor do elemento no eixo x ou y.
# BEFORE e AFTER: Controla a posição do elemento em relação a outros elementos já exibidos.
# IN_ : Especifica o elementro mestre em que o elemento deve ser exibido