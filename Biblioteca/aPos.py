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
    
    def getLimiteReservas(self):
        return self.limiteRes

    def getReservas(self):
        return self.reservas
    
    def addReserva(self, livro):
        self.reservas.append(livro)

    def empValido(self, livro):
        if len(self.livros) < self.limiteEmp:
            if livro not in u.reservas:
                x=0
                for i in self.livros:
                    if i.id == livro.id:
                        x=x+1
                        if livro.getReservas()>=x:
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
                livro.removeReserva()
                self.removeReserva(livro)
            self.addLivro(livro)
            cmd=EmprestimoValido(livro, self)
            cmd.executar()
            retun True
        else:
            cmd=LimiteLivros(livro, self)
            cmd.executar()
            return False
        
    def reservaValida(self):
        lim=self.getLimiteReservas()
        reservas=self.getReservas()
        if len(reservas)<lim:
            return True
        else: 
            return False
            