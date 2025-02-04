from singleton import getSistemaBiblioteca
from comandos import *
class Console:
    def __init__ (self, sistema):
        self.sistema = sistema
        self.commands = {
            "emp": EmprestimoCommand(sistema),
            "dev": DevolucaoCommand(sistema),
            "res": ReservaCommand(sistema),
            "obs": ObservacaoCommand(sistema),
            "usu": UsuarioCommand(sistema),
            "liv": LivroCommand(sistema),
            "ntf": NotificacaoCommand(sistema)
        }

    def run (self): 
        while True:
            print("Digite um comando")
            x=input().split()
            if x[0] == "sai":
                print ("encerrado")      
                break
            comando = x[0]
            argumentos = x[1:]  # argumentos extras, se houver
            if comando in self.commands:
                self.commands[comando].execute(*argumentos)
            else:
                print("Comando inválido.")
            

