from Iuser import User
from comandos import * 
from livro import Livro

class sistemaBiblioteca:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(sistemaBiblioteca, cls).__new__(cls)
        return cls._instance

    def __init__(self, lista_usuarios=None, lista_livros=None):
        if not hasattr(self, 'usuarios'):
            self.usuarios = lista_usuarios if lista_usuarios else []
            self.livros = lista_livros if lista_livros else []


    def getUserbyID (self, ID):
        for usuario in self.usuarios:
            if usuario.getID() == ID:  
                return usuario
            
        return None
         
    
    def getLivrobyID (self, ID):
        for livro in self.livros:
            if livro.getID() == ID:
                return livro
        return None 


    def emp(self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        if l.getEmprestado() is False:
            if u.empValido(l) is True:
                l.setEmprestado(True)    
        else:
            cmd = LivroIndisponivel (l, u)
            cmd.executar() 
                
    def dev (self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        emprestimos=u.getLivros()
        if l in emprestimos:
            u.removeLivros(l)
            l.setTempoEmprestado(0)
            l.setEmprestado(False)
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
            if len(u.getReservas())>2:
                l.notificarObservadores()


   