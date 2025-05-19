
class Libro:
    def __init__(self,titulo, autor,ISBN,genero):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.genero=genero
        self.prestamos=[]
        
    def hacer_prestamo(self,fecha_emision,fecha_devo):
        
        prestamo=f"Fecha del prestamo: {fecha_emision}, Fecha de entrega: {fecha_devo}"
        self.prestamos.append(prestamo)
        
    
    def mostrar_datos(self):
        print(f"\nTitulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.ISBN}")
        print(f"genero: {self.genero}")
        if not self.prestamos:
            print("No hay prestamos registrados")
            
        else:
            contador=1
            print("PRESTAMOS")
            print("Prestamo numero",contador)
            contador+=1
            print(f"\n Fecha de emision: {self.fecha_emision}")
            print(f"\n Fecha de emision: {self.fecha_devo}")
            

    