from sistemaBiblioteca import sistemaBiblioteca
from aGraduacao import alunoGrad
from aPos import alunoPos
from prof import Prof
from livro import Livro

def main():
    while True:
        u1 = alunoGrad('123', "Chico")
        u2 = alunoPos("456","Luis")
        u3 = Prof("789", "Lucas")

        l1 = Livro('100', "titulo1", "editora", "autor1", "1", "2000")
        l2 = Livro("101", "titulo2", "editora2", "autor2", "2", "2001")
        l3 = Livro("102", "titulo3", "editora3", "autor3", "3", "2002")
        
        
        s=sistemaBiblioteca([u1, u2, u3], [l1, l2, l3])
        x=input().split()
        if x[0] == "emp":
            s.emp(x[1], x[2])

if __name__ == "__main__":
    main()