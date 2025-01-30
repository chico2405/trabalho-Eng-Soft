from Iuser import User
from livro import Livro
from comandos import *
from datetime import datetime

class alunoPos(User):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=5
        self.limiteEmp = 3
        self.limiteRes = 3
        self.livros = []  #lista com EXEMPLARES
        self.reservas = []
        self.datasReservas = []
        
    def getNome (self):
        return self.nome

    def getID(self):
        return self.id
    
    def getLivros(self):
        return self.livros
    
    def addLivro(self, livro):
        self.livros.append(livro)

    def removeLivro(self, livro):
        self.livros.remove(livro)

    def getTempo(self):
        return self.tempo
    
    def getLimiteReservas(self):
        return self.limiteRes

    def getReservas(self):
        return self.reservas
    
    def addReserva(self, livro):
        self.reservas.append(livro)

    def removeReserva(self, livro):
        self.reservas.remove(livro)

    def empValido(self, exemplar, livro):
        if len(self.livros) < self.limiteEmp:
            for i in self.livros:
                t=i.getTempoEmprestado()
                if t > self.getTempo():
                    cmd = Devedor(livro, self)
                    cmd.executar()
                    return False
            for i in self.getReservas():
                if i.getLivro() == livro:
                    livro.removeReserva(self)
                    self.removeReserva(i)
            self.addLivro(exemplar)
            cmd=EmprestimoValido(livro, self)
            cmd.executar()
            return True
        else:
            cmd=LimiteLivros(livro, self)
            cmd.executar()
            return False
        
    def reservaValida(self, livro):
        lim=self.getLimiteReservas()
        reservas=self.getReservas()
        if len(reservas)<lim and livro not in reservas:
            return True
        else: 
            return False
            