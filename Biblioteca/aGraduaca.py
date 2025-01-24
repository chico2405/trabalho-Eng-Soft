from Iuser import User
from livro import Livro

class alunoGrad(User):
    def __init__ (self, id, nome):
        self.id=id
        self.nome=nome
        self.tempo=4
        self.limiteEmp = 2
        self.limiteRes = 3
        self.livros = []
        self.reservas = []
        self.reservaValida = True
        self.devedor = False
    def getNome(self):
        return self.nome

    def getLivros(self):
        return self.livros
    
    def setLivros(self, lista):
        self.livros=lista

    def getID(self):
        return self.id
    
   def getLimiteReservas(self):
        return self.limiteRes

    def getReservas(self):
        return self.reservas

    def getTempo(self):
        return self.tempo
    
    def empValido(self):
        if len(self.livros) < self.limiteEmp:
            for i in self.livros:
                t=i.getTempoEmprestado()
                if t > self.getTempo():
                    self.devedor = True
                    cmd = Devedor(livro, self)
                    return cmd.executar()
            livro.setEmprestado(True)
            if livro.getReservas()>0:
                livro.removeReserva()
            self.addLivro(livro)
            cmd=EmprestimoValido(livro, self)
            return cmd.executar()
        else:
            cmd=LimiteLivros(l, u)
            return cmd.executar()

    def reservaValida(self):
        lim=self.getLimiteReservas()
        reservas=self.getReservas()
        if len(reservas)<lim and self.devedor is False:
            return True
        else: 
            return False