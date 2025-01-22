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
    def empValido(self):
        pass