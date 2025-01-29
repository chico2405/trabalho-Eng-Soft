from Iuser import User
from comandos import * 
from livro import Livro
from datetime import datetime
from reserva import Reserva

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
        #if l not in u.getReservas():
            #if len(l.getReservas())>=len(l.getExemplares):
                    #cmd = MaisReservasQueExemplares (livro, self)
                    #cmd.executar()
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
            u.removeLivro(l)
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
        if u.reservaValida(l) is True:
            #checar se há mais exemplares do que reservas
            reserva = Reserva(l, datetime.now().strftime("%Y-%m-%d"))
            u.addReserva(reserva)
            l.addReserva()
            if l.getReservas() > 2:
                l.notificarObservadores()
            cmd = ReservaValida(l, u)
            cmd.executar()
        else:
            cmd = LimiteReservas(l, u)
            cmd.executar()

    def obs(self, IDobs, IDlivro):
        o = self.getUserbyID(IDobs)
        l = self.getLivrobyID(IDlivro)
        l.addObservadores(o)
        cmd = ObservadorConfirmado(o, l)
        cmd.executar()

    #def liv(self, IDlivro):
        #l = self.getLivrobyID(IDlivro)
        #res=l.getReservas()
        #for
    
    def usu(self, IDuser):
        u = self.getUserbyID(IDuser)
        livros = u.getLivros()
        res = u.getReservas()
        cmd = ConsultaUsuario(u, livros, res)
        cmd.executar()

    def ntf (self, IDobs):
        obs = self.getUserbyID(IDobs)
        noti = obs.getNotificacoes()
        cmd = Notificacoes(noti)
        cmd.executar()