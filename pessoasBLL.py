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