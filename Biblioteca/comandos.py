from Icomando import Command
from datetime import datetime, timedelta
from reserva import Reserva

class EmprestimoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDuser, IDlivro):
        l=self.sistema.getLivrobyID(IDlivro)
        u=self.sistema.getUserbyID(IDuser)
        if l.getEmprestado() is False:
            if u.empValido(l) is True:
                exemplar = l.getExemplarDisponivel()
                u.addLivro(exemplar)
                exemplar.setEmprestado(u)
                print("Empréstimo do livro " + l.getTitulo() + " para " + u.getNome()  + " feito com sucesso!")     
        else:
            print("Empréstimo negado do livro " + l.getTitulo() + " para " + u.getNome() +": Livro indisponível")

class DevolucaoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDuser, IDlivro):
        l=self.sistema.getLivrobyID(IDlivro)
        u=self.sistema.getUserbyID(IDuser)
        for i in l.getExemplares():
            if i in u.getEmprestimos_em_curso():
                u.removeLivro(i)
                return print("Livro " + l.getTitulo() + " emprestado para " + u.getNome() +" devolvido")    
        print("Livro " + l.getTitulo() + " emprestado para " + u.getNome() +" não pode ser devolvido") 

class ReservaCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDuser, IDlivro):
        l=self.sistema.getLivrobyID(IDlivro)
        u=self.sistema.getUserbyID(IDuser)
        if u.reservaValida(l) is True:
            reserva = Reserva(l, datetime.now().strftime("%Y-%m-%d"))
            u.addReserva(reserva)
            l.addReserva(u)
            if len(l.getReservas()) > 2:
                l.notificarObservadores()
            print("Reserva do livro " + l.getTitulo() + " para " + u.getNome()  + " feito com sucesso!")
        else:
            print("Reserva do livro " + l.getTitulo() + " para " + u.getNome()  + " não pode ser feita: Limite de reservas atingido")

class ObservacaoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDobs, IDlivro):
        o = self.sistema.getUserbyID(IDobs)
        l = self.sistema.getLivrobyID(IDlivro)
        l.addObservadores(o)
        print(o.getNome() +  " confirmado como observador do livro " +l.getTitulo())
        

class UsuarioCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDuser):
        u = self.sistema.getUserbyID(IDuser)
        res = u.getReservas()
        print("Empréstimos: ")
        for j in u.getLivros():
            estado = "Finalizado"
            if j.getEmprestado() is True:
                estado = "Em curso"
            if estado=="Em curso":
                dataemp = j.getData_Emprestimo()
                data_hoje = datetime.now()
                tempo_usuario = u.getTempo()  # Inteiro representando dias
                tempo_emprestado = j.getTempoEmprestado()  # Inteiro representando dias
                diferenca_dias = tempo_usuario - tempo_emprestado
                dataprev = data_hoje + timedelta(days=diferenca_dias)
                print(j.getTitulo(), estado, "data de empréstimo: ", dataemp, "data para a devolução: ", dataprev.strftime("%Y-%m-%d"))
            if estado=="Finalizado":
                datadev = j.getData_devolucao()
                dataemp = j.getData_Emprestimo()
                print(j.getTitulo(), estado, "data de empréstimo: ", dataemp, "data da devolução: ", datadev)
        print ("Reservas: ")
        for i in res:
            print(i.getTitulo(), "data da reserva: ", i.getData_Reserva())            


class LivroCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDlivro):
        l = self.sistema.getLivrobyID(IDlivro)
        res=l.getReservas()
        titulo =l.getTitulo()
        qnt_reservas = len(res)
        print(titulo, " reservas: ", qnt_reservas)
        if qnt_reservas > 0:
            print ("Usuários que reservaram o livro: ")
            for i in res:
                print(i.getNome())
        print ('Exemplares: ')
        for i in l.getExemplares():
            status = "Disponível"
            if i.getEmprestado() is True:
                dono_emprestimo = i.getUser().getNome()
                dataprev = i.getDataPrevista()
                dataemp = i.getData_Emprestimo()
                status = "Emprestado para " + str(dono_emprestimo) + " data empréstimo: " + dataemp + " data prevista para devolução: " + dataprev
                print ("Código: ", i.getIdEx() , " status: ", status)
            else:
                print ("Código: ", i.getIdEx() , " status: ", status)
 

class NotificacaoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, IDobs):
        obs = self.sistema.getUserbyID(IDobs)
        noti = obs.getNotificacoes()
        print(noti)








    







            

            