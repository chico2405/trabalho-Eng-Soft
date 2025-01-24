class EmprestimoValido(Command):
    def __init__ (self, livro, user):
        self.livro=livro
        self.user=user

    def executar(self):
        l=self.livro
        u=self.user
        print("Empréstimo do livro " + l.getTitulo() + " para " + u.getNome()  + " feito com sucesso!")
    
class LivroIndisponivel(Command):
    def __init__ (self, livro):
        self.livro=livro
    
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

 #main pra começar a executar:
    #s="input().split"
    #if s[0] == "emp":
        #sistemaBiblioteca.emp(s[1], s[2])