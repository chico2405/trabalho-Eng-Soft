class Livro:
    def __init__ (self, id, t, ed, au, edicao, ap):
        self.id=id
        self.titulo=t
        self.editora=ed
        self.autores=au
        self.edicao=edicao
        self.ano_publicacao=ap
        self.tempo_emprestado=0
        self.emprestado=False
        self.observadores = []
        self.reservas = 0
        
    def getTempoEmprestado(self):
        return self.tempo_emprestado
    
    def setTempoEmprestado(self, valor):
        self.tempo_emprestado=valor

    def getTitulo(self):
        return self.titulo

    def removeReserva(self):
        self.reservas = self.reservas-1

    def getReservas(self):
        return self.reservas

    def setEmprestado(self, vv):
        self.reservado = vv

    def getReservado(self):
        return self.reservado

    def getEmprestado(self):
        return self.emprestado

    def getObservadores(self):
        return self.observadores  