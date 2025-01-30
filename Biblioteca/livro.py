from exemplares import Exemplar

class Livro:
    def __init__ (self, id, t, ed, au, edicao, ap):
        self.id=id
        self.titulo=t
        self.editora=ed
        self.autores=au
        self.edicao=edicao
        self.ano_publicacao=ap
        self.observadores = []
        self.reservas = []
        self.exemplares = []

    def getEmprestado(self):
        for i in self.exemplares:
            if i.getEmprestado() is False:
                return False
        return True

    def getExemplares(self):
        return self.exemplares
                
    def getExemplarDisponivel(self, data_emprestimo):
        for i in self.exemplares:
            if i.getEmprestado() is False:
                i.setEmprestado(data_emprestimo)
                return i
        return None
    
    def addReserva(self, user):
        self.reservas.append(user)
    
    def removeReserva(self, user):
        self.reservas.remove(user)

    def getReservas(self):
        return self.reservas

    def getID(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def getObservadores(self):
        return self.observadores 

    def addObservadores(self, obs):
        self.observadores.append(obs)

    def notificarObservadores(self):
        obs = self.getObservadores() 
        if obs is not None and self.getReservas()>2:
            for i in obs:
                i.addNotificacao()
        else:
            return None 