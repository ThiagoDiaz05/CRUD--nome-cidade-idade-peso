import sqlite3
class PessoaDAL():
    def salvar_pessoa(self,pessoa):
        conexao = sqlite3.connect("pessoas.db") 
        cursor = conexao.cursor()   
        cursor.execute("INSERT INTO pessoas (nome, idade, cidade, peso) VALUES (?, ?, ?, ?)",
                   (pessoa.getNome(), pessoa.getIdade(), pessoa.getCidade(), pessoa.getPeso()))
        conexao.commit()
        conexao.close()