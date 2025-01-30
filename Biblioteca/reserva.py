class Reserva:
    def __init__ (self, livro, data):
        self.livro = livro
        self.data_reserva = data
    
    def getLivro(self):
        return self.livro
    
    def getTitulo(self):
        return self.livro.getTitulo()
    
    def getData_Reserva(self):
        return self.data_reserva
    
