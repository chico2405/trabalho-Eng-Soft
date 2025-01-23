from abc import ABC, abstractmethod

class Oberservador(ABC):

    @abstractmethod
    def getNotificacoes(self):
        pass

    @abstractmethod
    def addNotificacao(self):
        pass