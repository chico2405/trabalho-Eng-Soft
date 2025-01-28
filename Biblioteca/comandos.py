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

