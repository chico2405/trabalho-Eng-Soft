from sistemaBiblioteca import sistemaBiblioteca

class GetSistemaBiblioteca:
    _instancia = None

    @staticmethod 
    def get_sistema():
        if GetSistemaBiblioteca._instancia is None: 
            GetSistemaBiblioteca._instancia = sistemaBiblioteca()
        return GetSistemaBiblioteca._instancia