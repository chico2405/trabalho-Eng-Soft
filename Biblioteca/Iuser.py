from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def getID (self):
        pass

    @abstractmethod
    def getTempo(self):
        pass

    @abstractmethod
    def empValido(self):
        pass