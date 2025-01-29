from exemplares import Exemplar

class Livro:
    def __init__ (self, id, t, ed, au, edicao, ap):
        self.id=id
        self.titulo=t
        self.editora=ed
        self.autores=au
        self.edicao=edicao
        self.ano_publicacao=ap
        self.tempo_emprestado=0
        self.observadores = []
        self.reservas = 0
        self.emprestado = False
        self.exemplares = [Exemplar(1)]

    def getEmprestado(self):
        for i in self.exemplares:
            if i.getEmprestado() is False:
                return False
        return True

    def setEmprestado(self, vv):
        for i in self.exemplares:
            if i.getEmprestado() is False:
                i.setEmprestado(vv)

    def getTempoEmprestado(self):
        return self.tempo_emprestado
    
    def setTempoEmprestado(self, valor):
        self.tempo_emprestado=valor

    def getID(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def removeReserva(self):
        self.reservas = self.reservas-1
    
    def addReserva(self):
        self.reservas = self.reservas+1

    def getReservas(self):
        return self.reservas

    def getReservado(self):
        return self.reservado

    def getObservadores(self):
        return self.observadores 

    def notificarObservadores(self):
        obs = self.getObservadores() 
        if obs is not None and self.getReservas()>2:
            for i in obs:
                i.addNotificacao() 