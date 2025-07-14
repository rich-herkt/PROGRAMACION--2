print("""Elaborado por: Richard Herkt
        Fecha: 27/6/2025
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")


# Clase NodoDoble
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

# Clase HistorialNavegador
class HistorialNavegador:
    def __init__(self):
        self.actual = None  # Nodo donde se encuentra el usuario

    def visitar_pagina(self, url):
        nueva=NodoDoble(url)
        if not self.actual:
            self.actual=nueva
        else:
            
            self.actual.siguiente=nueva
            nueva.anterior = self.actual
            self.actual = nueva  # Avanzamos al nuevo nodo
            

    def atras(self):
        if self.actual.anterior:
            self.actual = self.actual.anterior
        print("Página anterior:", self.actual.dato)


    def adelante(self):
        if self.actual.siguiente:
            self.actual = self.actual.siguiente
        print("Página siguiente:", self.actual.dato)


    def mostrar_historial(self):
        pagina_actual=self.actual
        
        while pagina_actual.anterior:
            pagina_actual=pagina_actual.anterior
        while pagina_actual:
            print(pagina_actual.dato,end="<->")
            pagina_actual=pagina_actual.siguiente
        print("NULL")

    def pagina_actual(self):
        return self.actual.dato
    
    
navegador=HistorialNavegador()
navegador.visitar_pagina("Inicio")
navegador.visitar_pagina("Página 1")
navegador.visitar_pagina("Página 2")

print("Pagina Actual:",navegador.pagina_actual())  # Página 2
navegador.atras()

navegador.adelante() 
print("Pagina Actual:",navegador.pagina_actual())
navegador.mostrar_historial()