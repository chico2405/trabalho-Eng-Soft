from Iuser import User
from livro import Livro

class alunoPos(User):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=5
        self.limiteEmp = 3
        self.limiteRes = 3
        self.livros = []
        self.reservas = []
        self.reservaValida = True

    def getNome (self):
        return self.nome

    def getID(self):
        return self.id
    
    def getLivros(self):
        return self.livros
    
    def setLivros(self, lista):
        self.livros=lista

    def getTempo(self):
        return self.tempo
    
    def empValido(self):
        if len(self.livros) <= self.limiteEmp:
            for i in self.livros:
                t=i.getTempoEmprestado()
                if t > self.getTempo():
                    self.reservaValida = False
                    return "Devedor"
            return "Valido"
        else:
            return "LimiteAtingido"
        
    def getReservaValida(self):
        self.empValido()
        return self.reservaValida