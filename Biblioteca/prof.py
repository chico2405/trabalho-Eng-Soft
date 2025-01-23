from Iuser import User
from livro import Livro
class Prof(User, Oberservador):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=8
        self.livros = []
        self.reservas = []
        self.limiteRes = 3
        self.reservaValida = True
        self.notificacoes = 0
    
    def getNome(self):
        return self.nome

    def getID(self):
        return self.id
    
    def getNotificacoes(self):
        return self.notificacoes

    def addNotificacao(self):
        self.notificacoes=self.notificacoes + 1

    def getLivros(self):
        return self.livros
    
    def setLivros(self, lista):
        self.livros=lista
    

    def getTempo(self):
        return self.tempo
    
    def empValido(self):
        for i in self.livros:
            t=i.getTempoEmprestado()
            if t > self.getTempo():  
                self.reservaValida = False
                return "Devedor"  
        return "Valido"

    def getReservaValida(self):
        self.empValido()
        return self.reservaValida