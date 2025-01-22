class EmprestimoValido(Command):
    def __init__ (self, livro, user):
        self.livro=livro
        self.user=user

    def executar(self):
        l=self.livro
        u=self.user
        print("Empréstimo do livro " + l.getTitulo() + " para " + u.getNome + " feito com sucesso!")
    
class LivroIndisponivel(Command):
    def __init__ (self, livro):
        self.livro=livro
    
    def executar(self):
        l=self.livro
        print("Livro " + l.getNome + " indisponível")


 #main pra começar a executar:
    #s="input().split"
    #if s[0] == "emp":
        #sistemaBiblioteca.emp(s[1], s[2])