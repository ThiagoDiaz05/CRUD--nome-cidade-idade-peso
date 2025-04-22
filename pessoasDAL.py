import sqlite3
class PessoaDAL():
    def salvar_pessoa(self,pessoa):
        conexao = sqlite3.connect("pessoas.db") 
        cursor = conexao.cursor()   
        cursor.execute("INSERT INTO pessoas (nome, idade, cidade, peso) VALUES (?, ?, ?, ?)",
                   (pessoa.getNome(), pessoa.getIdade(), pessoa.getCidade(), pessoa.getPeso()))
        conexao.commit()
        conexao.close()
    def buscar_pessoa(self,nome):
        conexao = sqlite3.connect("pessoas.db") 
        cursor = conexao.cursor()   
        cursor.execute("SELECT nome, idade, cidade, peso FROM pessoas WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        conexao.close()
        return resultado
    def deletar_pessoa(self,nome, messagebox):
        conexao = sqlite3.connect("pessoas.db") 
        cursor = conexao.cursor()   
        cursor.execute("DELETE FROM pessoas WHERE nome = ?", (nome,))
        conexao.commit() 
        conexao.close()
        return messagebox.showinfo("campo","nome deletado")
    def atualizar_pessoa(self, pessoa, messagebox):
        conexao = sqlite3.connect("pessoas.db")
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE pessoas
            SET idade = ?, cidade = ?, peso = ?
            WHERE nome = ?
        """, ( pessoa.getIdade(), pessoa.getCidade(), pessoa.getPeso(),pessoa.getNome()))
        conexao.commit()
        linhas_afetadas = cursor.rowcount
        conexao.close()

        if linhas_afetadas == 0:
            return messagebox.showinfo("Aviso", "Pessoa não encontrada para atualizar.")
        else:
            return messagebox.showinfo("Sucesso", "Dados atualizados com sucesso.")