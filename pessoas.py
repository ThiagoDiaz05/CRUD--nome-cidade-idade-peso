class Pessoas():
    def __init__(self,nome,idade,cidade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cidade = cidade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    
    def getPeso(self):
        return self.peso
    
    def getCidade(self):
        return self.cidade
    
    def setNome(self, novoNome):
        self.nome = novoNome
        
    def setIdade(self, novaIdade):
        self.idade = novaIdade
        
    def setPeso(self, novoPeso):
        self.peso = novoPeso
        
    def setCidade(self, novaCidade):
        self.cidade = novaCidade