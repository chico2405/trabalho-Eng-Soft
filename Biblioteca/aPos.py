from Iuser import User

class alunoPos(User):
    def __init__ (self, id):
        self.id=id
        self.tempo=5
        self.limiteEmp = 3
        self.limiteRes = 3
        self.emprestimos = []
        self.reservas = []

    def getID(self):
        return self.id
    
    def getTempo(self):
        return self.tempo
    
    def empValido(self):
        if len(self.livros) <= self.limiteEmp:
            for i in self.livros:
                if i.tempoEmprestado > self.tempo:
                    return False
            return True