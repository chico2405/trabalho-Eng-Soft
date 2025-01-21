from Iuser import User

class sistemaBiblioteca:
    _instancia = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(sistemaBiblioteca, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "usuarios") or not hasattr(self, "livros"):  
            self.usuarios = []  
            self.livros = []

    def getUserbyID (self, ID):
        for usuario in self.usuarios:
            if usuario.id == ID:  
                return usuario
        return None  
    
    def getLivrobyID (self, ID):
          for livro in self.livros:
            if livro.id == ID:  # Verifica se o ID do livro corresponde
                return livro
          return None 

    def emp(self, IDuser, IDlivro):
        l=self.getLivrobyID(IDlivro)
        u=self.getUserbyID(IDuser)
        
        
