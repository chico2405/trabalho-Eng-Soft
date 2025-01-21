class Livro:
    def __init__ (self, id, t, ed, au, edicao, ap):
        self.id=id
        self.titulo=t
        self.editora=ed
        self.autores=au
        self.edicao=edicao
        self.ano_publicacao=ap
        self.tempo_emprestado=0
        self.reservado=False

    def getTempoEmprestado(self):
        return self.tempo_emprestado
    
    def set