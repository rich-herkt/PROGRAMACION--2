
from libro import Libro
libros=[]
def agregar_libro():
    titulo=input("Ingrese el Titulo del libro..")
    autor=input("Inrese el autor del Libro..")
    ISBN=int(input('Ingrese el ISBN del libro (13 digitos)..'))
    genero=input("Ingrese el genero del Libro..")
    libro=Libro(titulo,autor,ISBN,genero)
    libros.append(libro)
    print("Libro regristrado con exito!")
    

        


def agregar_prestamo():
    ISBN=int(input('Ingrese el ISBN del libro (13 digitos)..'))
    libro=buscar_libro(ISBN)
    
    if libro :
        fecha_emision=input("Ingrese la Fecha de emision del Libro..")
        fecha_devo=input("Igrese la fecha de devolucion del libro..")
        print("Prestamo realizado con exito !!")
        libro.hacer_prestamo(fecha_emision,fecha_devo)
    else:
        print("Este libro no esta disponible..")
            
def buscar_libro(ISBN):
    for libro in libros:
        if libro.ISBN==ISBN: 
            return libro
    
    return None
        
def mostrar_datos():
    ISBN=int(input('Ingrese el ISBN del libro (13 digitos)..'))
    libro=buscar_libro(ISBN)
    
    if libro:
        libro.mostrar_datos()
        
    else:
        print("Libro no Encontrado")


def mostrar_todos():
    if not libros:
        print("No hay libross registrados.")
    else:
        for libro in libros:
            libro.mostrar_datos()