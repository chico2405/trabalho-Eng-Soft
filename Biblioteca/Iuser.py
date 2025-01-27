from abc import ABC, abstractmethod

class User(ABC):
    
    @abstractmethod
    def getLivros(self):
        pass
    
    def setLivros(self):
        pass
    
    @abstractmethod
    def getID (self):
        pass

    @abstractmethod
    def getNome (self):
        pass

    @abstractmethod
    def getTempo(self):
        pass

    @abstractmethod
    def addLivro(self):
        pass
    
    @abstractmethod
    def removeLivro(self):
        pass

    @abstractmethod
    def reservaValida(self):
        pass

    @abstractmethod
    def getLimiteReservas(self):
        pass

    @abstractmethod
    def getReservas(self):
        pass

    @abstractmethod
    def addReserva(self):
        pass

    @abstractmethod
    def removeReserva(self):
        pass
