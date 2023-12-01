#2023-11-30_001
#Sorteio de 6 números

import tkinter as tk    #importando a biblioteca de interface gráfica padrão do python
import random as rd     #importando a biblioteca de sorteio

#Definindo a função "click_btn"
def click_btn():
    list = [] #lista vazia
    for i in range(0,6): # repetindo 6 vezes
        num = rd.randint(0,60) # sortea um número de 0 a 60
        list.append(num) # adiciona esse número a lista vazia
    label1.config(text = list)   #exibe o resustado final com os 6 números salvos dentro da lista
    
#Cria a janela(tela)    
janela = tk.Tk()

#Definindo o tamanho da tela
largura = 200
altura = 100
posicao_x = (janela.winfo_screenwidth() - largura) // 2
posicao_y = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

janela.title("Teste")

# Adicionar um rótulo(texto) à janela
label = tk.Label(janela, text="Bem-vindo ao meu software!")
label.pack()

# Adicionar um botão à janela
botao = tk.Button(janela, text="Clique em mim!", 
                  command=click_btn)
botao.pack()

label1 = tk.Label(janela, text="Números sorteados. ")
label1.pack()

# Iniciar o loop principal da interface gráfica
janela.mainloop()