from abc import ABC, abstractmethod

class Observador(ABC):

    @abstractmethod
    def getNotificacoes(self):
        pass

    @abstractmethod
    def getNome(self):
        pass

    @abstractmethod
    def addNotificacao(self):
        pass