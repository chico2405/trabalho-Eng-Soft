class Exemplar:
    def __init__ (self, id):
        self.id=id
        self.emprestado = False

    def getID(self):
        return self.id
    
    def getEmprestado(self):
        return self.emprestado

    def setEmprestado(self, vv):
        self.emprestado = vv