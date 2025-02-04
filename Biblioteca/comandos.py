from Icomando import Command

class EmprestimoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, usuario_id, livro_id):
        self.sistema.emp(usuario_id, livro_id)

class DevolucaoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, usuario_id, livro_id):
        self.sistema.dev(usuario_id, livro_id)

class ReservaCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, usuario_id, livro_id):
        self.sistema.res(usuario_id, livro_id)

class ObservacaoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, usuario_id, livro_id):
        self.sistema.obs(usuario_id, livro_id)

class UsuarioCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, usuario_id):
        self.sistema.usu(usuario_id)

class LivroCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, livro_id):
        self.sistema.liv(livro_id)

class NotificacaoCommand(Command):
    def __init__(self, sistema):
        self.sistema = sistema

    def execute(self, obs_id):
        self.sistema.ntf(obs_id)








    







            

            