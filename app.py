import customtkinter as ctk
from pessoas import Pessoas
from pessoasBLL import pessoasBLL
from tkinter import messagebox
#configuracao aparencia
ctk.set_appearance_mode("dark")

#criacao da janela principal
pessoa = Pessoas("Lucas", 30, "Recife", 72.5)
bll= pessoasBLL()
app = ctk.CTk()
app.title("CRUD")
app.geometry("500x500")

def salvar():
    pessoa.setNome(campo_nome.get())
    pessoa.setIdade(campo_idade.get())
    pessoa.setCidade(campo_cidade.get())
    pessoa.setPeso(campo_peso.get())
    bll.valida_pessoa(pessoa,messagebox)

#criacao dos campos
label_nome = ctk.CTkLabel(app, text="Nome:")
label_nome.pack(pady="10")
campo_nome = ctk.CTkEntry(app, placeholder_text="Digite o nome")
campo_nome.pack(pady="10")

label_idade = ctk.CTkLabel(app, text="Idade:")
label_idade.pack(pady="10")
campo_idade = ctk.CTkEntry(app, placeholder_text="Digite o idade")
campo_idade.pack(pady="10")

label_cidade = ctk.CTkLabel(app, text="Cidade:")
label_cidade.pack(pady="10")
campo_cidade = ctk.CTkEntry(app, placeholder_text="Digite o cidade")
campo_cidade.pack(pady="10")

label_peso = ctk.CTkLabel(app, text="Peso:")
label_peso.pack(pady="10")
campo_peso = ctk.CTkEntry(app, placeholder_text="Digite o peso")
campo_peso.pack(pady="10")

button_salvar = ctk.CTkButton(app, text="salvar", command=salvar) 
button_salvar.pack(pady="10")

app.mainloop()
