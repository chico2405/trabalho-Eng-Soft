from Iuser import User
from Iobservador import Observador
from datetime import datetime

class Prof(User, Observador):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=8
        self.livros = [] #lista com EXEMPLARES
        self.reservas = []
        self.limiteRes = 3
        self.notificacoes = 0
       

    def getNome(self):
        return self.nome

    def getID(self):
        return self.id
    
    def getNotificacoes(self):
        return self.notificacoes

    def addNotificacao(self):
        self.notificacoes=self.notificacoes + 1

    def getLimiteReservas(self):
        return self.limiteRes

    def getReservas(self):
        return self.reservas

    def getLivros(self):
        return self.livros
    
    def addLivro(self, exemplar):
        self.livros.append(exemplar)

    def removeLivro(self, livro):
        for i in self.livros:
            if i == livro:
                i.Devolvido(datetime.now().strftime("%Y-%m-%d"))
    
    def addReserva(self, livro):
        self.reservas.append(livro)

    def removeReserva(self, livro):
        self.reservas.remove(livro)

    def getTempo(self):
        return self.tempo
    
    def empValido(self, livro):
        for i in self.livros:
            t=i.getTempoEmprestado()
            if t > self.getTempo():  
                print("Empréstimo negado do livro " + livro.getTitulo() + " para " + self.getNome() +": Devedor")
                return False
        for i in self.getReservas():
            if i.getLivro() == livro:
                livro.removeReserva(self)
                self.removeReserva(i)
        return True
        
    def reservaValida(self, livro):
        lim=self.getLimiteReservas()
        reservas=self.getReservas()
        if len(reservas)<lim and livro not in reservas:
            return True
        else: 
            return False
    