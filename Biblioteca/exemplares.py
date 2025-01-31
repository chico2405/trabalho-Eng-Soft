from datetime import datetime

class Exemplar:
    def __init__ (self, id, id_exemplar):
        self.id=id
        self.id_exemplar = id_exemplar
        self.emprestado = False
        self.data_emprestimo = None
        self.data_devolucao = None

    def getID(self):
        return self.id
    
    def getEmprestado(self):
        return self.emprestado

    def setEmprestado(self, data_emprestimo):
        self.emprestado = True
        self.data_emprestimo=data_emprestimo


    def getData_Emprestimo(self):
        return self.data_emprestimo

    def getData_devolucao(self):
        return self.data_devolucao

    def Devolvido(self, data):
        self.data_devolucao = data
        self.emprestado = False

    def getTempoEmprestado(self):
        if self.data_emprestimo is not None:
            data_emprestimo_dt = datetime.strptime(self.data_emprestimo, "%Y-%m-%d")
            diferenca = (datetime.now() - data_emprestimo_dt).days
            return diferenca
        else:
            return 0
    

    