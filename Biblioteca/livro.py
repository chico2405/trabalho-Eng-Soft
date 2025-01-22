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
        self.reservado=False

    def getTempoEmprestado(self):
        return self.tempo_emprestado
    
    def setTempoEmprestado(self, valor):
        self.tempo_emprestado=valor

    def getTitulo(self):
        return self.titulo

    def setReservado(self, vv):
        self.reservado = vv

    def setEmprestado(self, vv):
        self.reservado = vv

    def getReservado(self):
        return self.reservado

    def getEmprestado(self):
        return self.emprestado
    