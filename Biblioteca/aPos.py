from Iuser import User
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
        
    def getNome (self):
        return self.nome

    def getID(self):
        return self.id
    
    def getLivros(self):
        return self.livros
    
    def addLivro(self, livro):
        self.livros.append(livro)

    def removeLivro(self, livro):
        for i in self.livros:
            if i == livro:
                i.Devolvido(datetime.now().strftime("%Y-%m-%d"))

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

    def getEmprestimos_em_curso(self):
        em_curso=[]
        for i in self.livros:
            if i.getEmprestado() is True:
                em_curso.append(i)
        return em_curso

    def empValido(self, livro):
        if len(self.getEmprestimos_em_curso()) < self.limiteEmp:
            if len(livro.getReservas())>=len(livro.getExemplaresDisponiveis()):
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
            