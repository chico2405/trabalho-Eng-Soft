from Iuser import User
from comandos import * 
from livro import Livro

class sistemaBiblioteca:
    _instancia = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "usuarios") or not hasattr(self, "livros"):  
            self.usuarios = []  
            self.livros = []
    def getUserbyID (self, ID):
        for usuario in self.usuarios:
            if usuario == ID:  
                return usuario
        return None  
    
    def getLivrobyID (self, ID):
        for livro in self.livros:
            if livro.id == ID:  
                return livro
        return None 

    def removeLivro (self, livro):
        self.livros.remove(livro)

    def addLivro(self, livro):
        self.livros.append(livro)

    def emp(self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        if l in self.livros is True:
            if u.empValido(l) is True:
                self.removeLivro(l)    
        else:
            cmd = LivroIndisponivel (l, u)
            return cmd.executar() 
                
    def dev (self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        emprestimos=u.getLivros()
        if l in emprestimos:
            u.removeLivros(l)
            l.setTempoEmprestado(0)
            self.addLivro(l)
            cmd = LivroDevolvido(l, u)
            cmd.executar()       
        else:
            cmd = LivroNaoDevolvido(l, u)
            cmd.executar()
 
    def res (self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        if u.reservaValida() is True:
            u.addReserva(l)
            l.addReserva()
            l.notificarObservadores()


   