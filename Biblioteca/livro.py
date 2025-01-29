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
        self.emprestado = False
        self.reservas = 0
        #self.exemplares = [Exemplar(1)]

    def getEmprestado(self):
        #for i in self.exemplares:
            #if i.getEmprestado() is False:
                #return False
        return self.emprestado

    def setEmprestado(self, vv):
        #for i in self.exemplares:
            #if i.getEmprestado() is False:
               # i.setEmprestado(vv)
        self.emprestado = vv

    def getTempoEmprestado(self):
        return self.tempo_emprestado
    
    def setTempoEmprestado(self, valor):
        self.tempo_emprestado=valor

    def addReserva(self):
        self.reservas = self.reservas+1
    
    def removeReserva(self):
        self.reservas = self.reservas-1

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
        if obs is not None and len(self.getReservas())>2:
            for i in obs:
                i.addNotificacao()
        else:
            return None 