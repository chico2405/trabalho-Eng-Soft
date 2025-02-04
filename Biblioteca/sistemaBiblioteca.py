class sistemaBiblioteca:
    def __init__(self, lista_usuarios = None, lista_livros = None):
            self.usuarios = lista_usuarios if lista_usuarios else []
            self.livros = lista_livros if lista_livros else []


    def getUserbyID (self, ID):
        for usuario in self.usuarios:
            if usuario.getID() == ID:  
                return usuario
            
        return None
         
    
    def getLivrobyID (self, ID):
        for livro in self.livros:
            if livro.getID() == ID:
                return livro
        return None
    

 