from comandos import * 
from datetime import datetime
from reserva import Reserva

class sistemaBiblioteca:
    def __init__(self, lista_usuarios = None, lista_livros = None):
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
                exemplar = l.getExemplarDisponivel()
                u.addLivro(exemplar)
                exemplar.setEmprestado(datetime.now().strftime("%Y-%m-%d"), u)     
        else:
            cmd = LivroIndisponivel (l, u)
            cmd.executar() 
                
    def dev (self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        for i in l.getExemplares():
            if i in u.getLivros():
                u.removeLivro(i)
                cmd = LivroDevolvido(l, u)
                return cmd.executar()
        
        cmd = LivroNaoDevolvido(l, u)
        return cmd.executar()
 
    def res (self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        if u.reservaValida(l) is True:
            reserva = Reserva(l, datetime.now().strftime("%Y-%m-%d"))
            u.addReserva(reserva)
            l.addReserva(u)
            if len(l.getReservas()) > 2:
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

    def liv(self, IDlivro):
        l = self.getLivrobyID(IDlivro)
        res=l.getReservas()
        cmd = ConsultaLivro(l,res)
        cmd.executar()

    
    def usu(self, IDuser):
        u = self.getUserbyID(IDuser)
        res = u.getReservas()
        cmd = ConsultaUsuario(u, res)
        cmd.executar()

    def ntf (self, IDobs):
        obs = self.getUserbyID(IDobs)
        noti = obs.getNotificacoes()
        cmd = Notificacoes(noti)
        cmd.executar()