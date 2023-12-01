#2023-11-30_002>
#Calculadora de média simples

import tkinter as tk    #importando a biblioteca de interface gráfica padrão do python

#- Inicio, Commands ------------------------------------------------------------------------

def calc_media():
    # Obtém os valores do "tk.Text"
    nota1_texto = nota1.get("1.0", "end-1c")
    nota2_texto = nota2.get("1.0", "end-1c")
    nota3_texto = nota3.get("1.0", "end-1c")

    try:
        # Converte os valores de "texto/String" para "Float"
        nota1_float = float(nota1_texto)
        nota2_float = float(nota2_texto)
        nota3_float = float(nota3_texto)

        # Calculo simples de média
        media = (nota1_float + nota2_float + nota3_float) / 3
        
        #Troca o texto da label "resultado"
        resultado.config(text = f'A média final do aluno é: {media:.2f}')
    
    # Caso algo de errado, informa o usuário para colocar valores válidos
    except ValueError: 
        resultado.config(text="Por favor, insira valores numéricos válidos para as notas.")

def clear(): 
    #Limpa as variaveis 
    nota1.delete("1.0", "end")
    nota2.delete("1.0", "end")
    nota3.delete("1.0", "end")
    
    #Limpa a label
    resultado.config(text="")
    
#- Fim, Commands ------------------------------------------------------------------------

#- Inicio, Definição --------------------------------------------------------------------

jan = tk.Tk()

largura = 300
altura = 200
posicao_x = (jan.winfo_screenwidth() - largura) // 2
posicao_y = (jan.winfo_screenheight() - altura) // 2
jan.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

#- Fim, Definição ------------------------------------------------------------------------

#- Inicio, Variaveis/Interface ------------------------------------------------------------------------

jan.title('Calculadora de média simples')

label = tk.Label(jan, text="Digite as três (3) notas do aluno:")
label.pack(pady=2)

nota1 = tk.Text(jan, height=1, width=10)
nota1.pack(pady=2)

nota2 = tk.Text(jan, height=1, width=10)
nota2.pack(pady=2)

nota3 = tk.Text(jan, height=1, width=10)
nota3.pack(pady=2)

calcular_btn = tk.Button(jan, text='Calcular média', command= calc_media)
calcular_btn.pack(pady=2)

resultado = tk.Label(jan, text='')
resultado.pack(pady=2)

reset = tk.Button(jan, text="Limpar valores.", command=clear)
reset.pack()

jan.mainloop()

#- Fim, Variaveis/Interface ------------------------------------------------------------------------