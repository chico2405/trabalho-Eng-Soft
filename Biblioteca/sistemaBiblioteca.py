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

    def emp(self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        if l in self.livros:
            if u.empValido()=="Valido":
                l.setEmprestado(True)
                l.setReservado(False)
                u.addLivro(l)
                cmd=EmprestimoValido(l, u)
                cmd.executar()
            else if u.empValido()=="Devedor":
                cmd=Devedor(l, u)
                cmd.executar()
        else:
            cmd = LivroIndisponivel (l, u)
            cmd.executar() 
                
    def dev (self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        emprestimos=u.getLivros
        if l in emprestimos:
            emprestimos.remove(l)
            u.setLivros(emprestimos)
            l.setEmprestado(False)
            l.setTempoEmprestado(0)
            self.livros.append(l)
            #comando devolvido        
        else:
            #comando nao-devolvido

   