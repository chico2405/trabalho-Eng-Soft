from Icomando import Command

class EmprestimoValido(Command):
    def __init__ (self, livro, user):
        self.livro=livro
        self.user=user

    def executar(self):
        l=self.livro
        u=self.user
        print("Empréstimo do livro " + l.getTitulo() + " para " + u.getNome()  + " feito com sucesso!")
    
class LivroIndisponivel(Command):
    def __init__ (self, livro, user):
        self.livro=livro
        self.user=user
    
    def executar(self):
        l=self.livro
        u=self.user
        print("Empréstimo negado do livro " + l.getTitulo() + " para " + u.getNome() +": Livro indisponível")

class Devedor(Command):
    def __init__ (self, livro, usuario):
        self.livro=livro
        self.user=usuario
    
    def executar(self):
        l=self.livro
        u=self.user

        print("Empréstimo negado do livro " + l.getTitulo() + " para " + u.getNome() +": Devedor")

class LimiteLivros(Command):
    def __init__ (self, livro, usuario):
        self.livro=livro
        self.user=usuario
    
    def executar(self):
        l=self.livro
        u=self.user

        print("Empréstimo negado do livro " + l.getTitulo() + " para " + u.getNome() +": Limite de livros emprestados atingido")

class MaisReservasQueExemplares(Command):
    def __init__ (self, livro, usuario):
        self.livro=livro
        self.user=usuario
    
    def executar(self):
        l=self.livro
        u=self.user

        print("Empréstimo negado do livro " + l.getTitulo() + " para " + u.getNome() +": Mais reservas do que exemplares")

class ExemplarEmprestado(Command):
    def __init__ (self, livro, usuario):
        self.livro=livro
        self.user=usuario
    
    def executar(self):
        l=self.livro
        u=self.user

        print("Empréstimo negado do livro " + l.getTitulo() + " para " + u.getNome() +": Exemplar já emprestado ao usuário")

class LivroDevolvido(Command):
    def __init__ (self, livro, usuario):
        self.livro=livro
        self.user=usuario
    
    def executar(self):
        l=self.livro
        u=self.user

        print("Livro " + l.getTitulo() + " emprestado para " + u.getNome() +" devolvido")  

class LivroNaoDevolvido(Command):
    def __init__ (self, livro, usuario):
        self.livro=livro
        self.user=usuario
    
    def executar(self):
        l=self.livro
        u=self.user

        print("Livro " + l.getTitulo() + " emprestado para " + u.getNome() +" não pode ser devolvido")    

class ReservaValida(Command):
    def __init__ (self, livro, user):
        self.livro=livro
        self.user=user

    def executar(self):
        l=self.livro
        u=self.user
        print("Reserva do livro " + l.getTitulo() + " para " + u.getNome()  + " feito com sucesso!")

class LimiteReservas(Command):
    def __init__ (self, livro, user):
        self.livro=livro
        self.user=user

    def executar(self):
        l=self.livro
        u=self.user
        print("Reserva do livro " + l.getTitulo() + " para " + u.getNome()  + " não pode ser feita: Limite de reservas atingido")

class ConsultaUsuario(Command):
    def __init__ (self, u, livros, res):
        self.user = u
        self.livros = livros
        self.reservas = res
    
    def executar(self):
        print("Empréstimos: ")
        for i in self.livros:
            estado = "Disponivel"
            if i.getEmprestado() is True:
                estado="Emprestado"
            print(i.titulo, estado)
            #informações que tem a ver com as datas
        for i in self.reservas:
            print(i.titulo)
            #informações que tem a ver datas

class Notificacoes(Command):
    def __init__ (self, noti):
        self.notificacoes=noti
    
    def executar(self):
        print(self.notificacoes)

class ObservadorConfirmado(Command):
    def __init__ (self, ob, livro):
        self.observador=ob
        self.livro = livro

    def executar(self):
        print(self.observador.getNome() +  " confirmado como observador do livro " +self.livro.getTitulo() )
            