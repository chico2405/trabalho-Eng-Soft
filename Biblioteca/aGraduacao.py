from Iuser import User
from datetime import datetime

class alunoGrad(User):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=4
        self.limiteEmp = 2
        self.limiteRes = 3
        self.livros = [] #lista com EXEMPLARES
        self.reservas = []

    def getNome(self):
        return self.nome

    def getLivros(self):
        return self.livros
    
    def addLivro(self, livro):
        self.livros.append(livro)

    def removeLivro(self, livro):
        for i in self.livros:
            if i == livro:
                i.Devolvido(datetime.now().strftime("%Y-%m-%d"))

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
            if len(livro.getReservas())>=len(livro.getExemplares()):
                if livro not in self.getReservas():
                        print("Empréstimo negado do livro " + livro.getTitulo() + " para " + self.getNome() +": Mais reservas do que exemplares")
                        return False
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
        else:
            print("Empréstimo negado do livro " + livro.getTitulo() + " para " + self.getNome() +": Limite de livros emprestados atingido")
            return False

    def reservaValida(self, livro):
        lim=self.getLimiteReservas()
        reservas=self.getReservas()
        if len(reservas)<lim and livro not in reservas:
            return True
        else: 
            return False