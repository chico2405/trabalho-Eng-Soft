from sistemaBiblioteca import sistemaBiblioteca

class getSistemaBiblioteca:
    _instancia = None

    @staticmethod
    def get_sistema(usuarios=None, livros=None):
        if getSistemaBiblioteca._instancia is None:
            getSistemaBiblioteca._instancia = sistemaBiblioteca(usuarios or [], livros or [])
        return getSistemaBiblioteca._instancia