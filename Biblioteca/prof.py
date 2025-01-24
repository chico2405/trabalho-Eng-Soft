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
        self.devedor = False

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
    
    def addLivro(self, livro):
        self.livros.append(livro)
    
    def removeLivro(self, livro):
        self.livros.remove(livro)
    

    def getTempo(self):
        return self.tempo
    
    def empValido(self, livro):
        for i in self.livros:
            t=i.getTempoEmprestado()
            if t > self.getTempo():  
                self.devedor = True
                cmd=Devedor(livro, self)
                return cmd.executar()
        livro.setEmprestado(True)
        if livro.getReservas()>0:
            livro.removeReserva()
        self.addLivro(livro)
        cmd=EmprestimoValido(livro, self)
        return cmd.executar()
        

    def reservaValida(self):
        lim=self.getLimiteReservas()
        reservas=self.getReservas()
        if len(reservas)<lim and self.devedor is False:
            return True
        else: 
            return False