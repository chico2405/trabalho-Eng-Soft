from Iuser import User
from livro import Livro
from comandos import *

class alunoGrad(User):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=4
        self.limiteEmp = 2
        self.limiteRes = 3
        self.livros = []
        self.reservas = []
    
    def getNome(self):
        return self.nome

    def getLivros(self):
        return self.livros
    
    def addLivro(self, livro):
        self.livros.append(livro)

    def removeLivro(self, livro):
        self.livros.remove(livro)

    def getID(self):
        return self.id
    
    def getLimiteReservas(self):
        return self.limiteRes

    def getReservas(self):
        return self.reservas

    def addReserva(self, livro):
        self.reservas.append(livro)

    def removeReserva(self, livro):
        self.reservas.remove(livro)

    def getTempo(self):
        return self.tempo
    
    def empValido(self, livro):
        if len(self.livros) < self.limiteEmp:
            if livro not in self.reservas:
                x=0
                for i in self.livros:
                    if i.id == livro.id:
                        x=x+1
                        if len(livro.getReservas())>=x:
                            cmd = MaisReservasQueExemplares (livro, self)
                            cmd.executar()
                            return False
            for i in self.livros:
                t=i.getTempoEmprestado()
                if t > self.getTempo():
                    cmd = Devedor(livro, self)
                    cmd.executar()
                    return False
            if livro in self.reservas:
                livro.removeReserva(self)
                self.removeReserva(livro)
            self.addLivro(livro)
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