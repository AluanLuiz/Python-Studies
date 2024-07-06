import customtkinter as ctk

def button_fucion():
    print("Botao funcionado!")
    
app = ctk.CTk()
app.title("my app")
app.geometry("400x150")

app.grid_columnconfigure(0, weight=1)

button = ctk.CTkButton(app, text="Botao 1", command=button_fucion)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

app.mainloop()