from Icomando import Command
from datetime import datetime, timedelta

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
    def __init__ (self, u, res):
        self.user = u

        self.reservas = res

    def executar(self):
        print("Empréstimos: ")
        for j in self.user.getLivros():
            estado = "Finalizado"
            if j.getEmprestado() is True:
                estado = "Em curso"
            if estado=="Em curso":
                dataemp = j.getData_Emprestimo()
                data_hoje = datetime.now()
                tempo_usuario = self.user.getTempo()  # Inteiro representando dias
                tempo_emprestado = j.getTempoEmprestado()  # Inteiro representando dias
                diferenca_dias = tempo_usuario - tempo_emprestado
                dataprev = data_hoje + timedelta(days=diferenca_dias)
                print(j.getTitulo(), estado, "data de empréstimo: ", dataemp, "data para a devolução: ", dataprev.strftime("%Y-%m-%d"))
            if estado=="Finalizado":
                datadev = j.getData_devolucao()
                dataemp = j.getData_Emprestimo()
                print(j.getTitulo, estado, "data de empréstimo: ", dataemp, "data da devolução: ", datadev)

        print ("Reservas: ")
        for i in self.reservas:
            print(i.getTitulo(), "data da reserva: ", i.getData_Reserva())            


class ConsultaLivro(Command):
    def __init__ (self, livro, res):
        self.livro = livro
        self.reservaram = res

    def executar(self):
            titulo = self.livro.getTitulo()
            qnt_reservas = len(self.reservaram)
            print(titulo, " reservas: ", qnt_reservas)
            if qnt_reservas > 0:
                print ("Usuários que reservaram o livro: ")
                for i in self.reservaram:
                    print(i.getNome())
            print ('Exemplares: ')
            for i in self.livro.getExemplares():
                status = "Disponível"
                if i.getEmprestado() is True:
                    dono_emprestimo = i.getUser().getNome()
                    dataprev = i.getDataPrevista()
                    dataemp = i.getData_Emprestimo()
                    status = "Emprestado para " + str(dono_emprestimo) + " data empréstimo: " + dataemp + " data prevista para devolução: " + dataprev
                    print ("Código: ", i.getIdEx() , " status: ", status)
                else:
                    print ("Código: ", i.getIdEx() , " status: ", status)
 

                    


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
            