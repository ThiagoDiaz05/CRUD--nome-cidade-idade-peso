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
app.geometry("500x600")

def salvar():
    pessoa.setNome(campo_nome.get())
    pessoa.setIdade(campo_idade.get())
    pessoa.setCidade(campo_cidade.get())
    pessoa.setPeso(campo_peso.get())
    bll.valida_pessoa(pessoa,messagebox)
def mostrar():
    pessoa.setNome(campo_nome.get())
    bll.valida_nome(pessoa, campo_idade, campo_cidade, campo_peso, messagebox)
def limpar():
    campo_nome.delete(0,"end")
    campo_idade.delete(0, "end")
    campo_cidade.delete(0, "end")
    campo_peso.delete(0, "end")
def deletar():
    pessoa.setNome(campo_nome.get())
    bll.valida_nomeDeletar(pessoa,messagebox)
def atualizar():
    pessoa.setNome(campo_nome.get())
    pessoa.setIdade(campo_idade.get())
    pessoa.setCidade(campo_cidade.get())
    pessoa.setPeso(campo_peso.get())
    
    bll.valida_nomeAtualizar( pessoa, messagebox)

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

button_mostrar = ctk.CTkButton(app, text="mostrar", command=mostrar) 
button_mostrar.pack(pady="10")

button_limpar = ctk.CTkButton(app, text="limpar", command=limpar) 
button_limpar.pack(pady="10")

button_deletar = ctk.CTkButton(app, text="deletar", command=deletar) 
button_deletar.pack(pady="10")

button_atualizar = ctk.CTkButton(app, text="atualizar", command=atualizar) 
button_atualizar.pack(pady="10")

app.mainloop()
