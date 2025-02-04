from datetime import datetime, timedelta
from singleton import getSistemaBiblioteca

class Exemplar:
    def __init__ (self, id, id_exemplar):
        self.id=id
        self.id_exemplar = id_exemplar
        self.emprestado = False
        self.data_emprestimo = None
        self.data_devolucao = None
        self.user = None

    def getID(self):
        return self.id
    
    def getTitulo(self):
        s=getSistemaBiblioteca.get_sistema()
        livros = s.livros
        for i in livros:
            if i.id == self.id:
                return i.getTitulo()


    def getIdEx (self):
        return self.id_exemplar
    
    def getEmprestado(self):
        return self.emprestado

    def setEmprestado(self, user):
        self.emprestado = True
        self.data_emprestimo=datetime.now().strftime("%Y-%m-%d")
        self.user=user
        


    def getData_Emprestimo(self):
        return self.data_emprestimo

    def getData_devolucao(self):
        return self.data_devolucao

    def Devolvido(self, data):
        self.data_devolucao = data
        self.emprestado = False
        self.user = None
    
    def getTempoEmprestado(self):
        if self.data_emprestimo is not None:
            data_emprestimo_dt = datetime.strptime(self.data_emprestimo, "%Y-%m-%d")
            diferenca = (datetime.now() - data_emprestimo_dt).days
            return diferenca
        else:
            return 0
    

    def getUser(self):
        return self.user

    def getDataPrevista(self):
        data_hoje = datetime.now()
        tempo_usuario = self.user.getTempo()  # Inteiro representando dias
        tempo_emprestado = self.getTempoEmprestado()  # Inteiro representando dias
        diferenca_dias = tempo_usuario - tempo_emprestado
        dataprev = data_hoje + timedelta(days=diferenca_dias)
        
        return dataprev.strftime("%Y-%m-%d")