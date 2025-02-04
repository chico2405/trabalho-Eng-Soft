
class Livro:
    def __init__ (self, id, t, ed, au, edicao, ap):
        self.id=id
        self.titulo=t
        self.editora=ed
        self.autores=au
        self.edicao=edicao
        self.ano_publicacao=ap
        self.observadores = []
        self.usuarios_reservaram = []
        self.exemplares = []

    def getEmprestado(self):
        for i in self.exemplares:
            if i.getEmprestado() is False:
                return False
        return True

    def getExemplares(self):
        return self.exemplares
                
    def getExemplarDisponivel(self):
        for i in self.exemplares:
            if i.getEmprestado() is False:
                return i
        return None
    
    def getExemplaresDisponiveis(self):
        disponiveis = []
        for i in self.exemplares:
            if i.getEmprestado() is False:
                disponiveis.append(i)
        return disponiveis
    
    def addReserva(self, user):
        self.usuarios_reservaram.append(user)
    
    def removeReserva(self, user):
        self.reservas.remove(user)

    def getReservas(self):
        return self.usuarios_reservaram

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
        if obs is not None and len(self.usuarios_reservaram)>2:
            for i in obs:
                i.addNotificacao()
        else:
            return None 