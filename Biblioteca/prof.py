from Iuser import User

class Prof(User):
    def __init__ (self, id):
        self.id=id
        self.tempo=8
        self.emprestimos = []
        self.reservas = []
        self.limiteRes = 3
    def getID(self):
        return self.id
    
    def getTempo(self):
        return self.tempo