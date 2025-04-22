from pessoasDAL import PessoaDAL
dal = PessoaDAL()
class pessoasBLL():
    def valida_pessoa(self,pessoa,messagebox):
        if(pessoa.getNome() == ""):
            return messagebox.showinfo("campo","O campo nome é de preenchimento obrigatório...")
        if(pessoa.getIdade() == ""):
            return messagebox.showinfo("campo","O campo idade é de preenchimento obrigatório...")
        if(pessoa.getCidade() == ""):
            return messagebox.showinfo("campo","O campo cidade é de preenchimento obrigatório...")
        if(pessoa.getPeso() == ""):
            return messagebox.showinfo("campo","O campo peso é de preenchimento obrigatório...")
        dal.salvar_pessoa(pessoa)
    def valida_nome(self,pessoa, campo_idade, campo_cidade, campo_peso,messagebox):
        if(pessoa.getNome() == ""):
            return messagebox.showinfo("campo","O campo nome é de preenchimento obrigatório...")
        resultado = dal.buscar_pessoa(pessoa.getNome())

        if resultado:
            campo_idade.insert(0, resultado[1])
            campo_cidade.insert(0, resultado[2])
            campo_peso.insert(0, resultado[3])
        else:
            messagebox.showinfo("Erro", "Pessoa não encontrada.")
        
    def valida_nomeDeletar(self,pessoa,messagebox):
        if(pessoa.getNome() == ""):
            return messagebox.showinfo("campo","O campo nome é de preenchimento obrigatório...")
        dal.deletar_pessoa(pessoa.getNome(), messagebox)

    def valida_nomeAtualizar(self,  pessoa, messagebox):

        if pessoa.getNome() == "":
            return messagebox.showwarning("Campo obrigatório", "O novo nome não pode estar em branco.")

        if pessoa.getIdade() == "":
            return messagebox.showwarning("Campo obrigatório", "A idade é obrigatória.")

        if pessoa.getCidade() == "":
            return messagebox.showwarning("Campo obrigatório", "A cidade é obrigatória.")

        if pessoa.getPeso() == "":
            return messagebox.showwarning("Campo obrigatório", "O peso é obrigatório.")

        return dal.atualizar_pessoa( pessoa, messagebox)