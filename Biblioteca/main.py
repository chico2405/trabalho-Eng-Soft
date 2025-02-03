from sistemaBiblioteca import sistemaBiblioteca
from aGraduacao import alunoGrad
from aPos import alunoPos
from prof import Prof
from livro import Livro
from exemplares import Exemplar
def main():
    u1 = alunoGrad('123', "Chico")
    u2 = alunoPos("456","Luis")
    u3 = Prof("789", "Lucas")
    u4 = Prof("902", "Paulo")
    u5 = alunoGrad("805", "Pedro")

    l1 = Livro('100', "titulo1", "editora", "autor1", "1", "2000")
    l2 = Livro("101", "titulo2", "editora2", "autor2", "2", "2001")
    l3 = Livro("102", "titulo3", "editora3", "autor3", "3", "2002")
    l4 = Livro("103", "titulo4", "editora4", "autor4", "4", "2003")
    l5 = Livro("104", "titulo5", "editora5", "autor5", "5", "2002")
    
    ex1 = Exemplar("100", "01")
    ex2 = Exemplar("100", "02")
    ex3 = Exemplar("101", "03")
    ex4 = Exemplar("102", "04")  
    ex5 = Exemplar("103", "05")
    ex6 = Exemplar("104", "06")
    
    livros = [l1, l2, l3, l4, l5]
    exemplares = [ex1, ex2, ex3, ex4, ex5, ex6]
    
    for i in livros:
        for j in exemplares:
            if i.id == j.id:
                i.exemplares.append(j)
    
    fabrica = FabricaSistemaBiblioteca()

    sema = fabrica.get_sistema()ist

    s=sistemaBiblioteca([u1, u2, u3, u4, u5], [l1, l2, l3, l4, l5])
    
    while True:
        x=input().split()
        
        if x[0] == "emp":
            s.emp(x[1], x[2])
        
        if x[0] == "dev":
            s.dev(x[1], x[2])
        
        if x[0] == "res":
            s.res(x[1], x[2])
        
        if x[0] == "obs":
            s.obs(x[1], x[2])
        
        if x[0] == "usu":
            s.usu(x[1])
        
        if x[0] == "liv":
            s.liv(x[1])
        
        if x[0] == "ntf":
            s.ntf(x[1])

        if x[0] == "sai":
            break

if __name__ == "__main__":
    main()