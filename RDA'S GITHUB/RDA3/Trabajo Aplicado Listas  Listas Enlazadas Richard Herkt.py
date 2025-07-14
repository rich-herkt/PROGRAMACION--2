print("""Elaborado por: Richard Herkt
        Fecha: 4/6/2025
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")

class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

class ListaAtencion:
    def __init__(self):
        self.inicio = None

    def agregar_paciente(self, nombre):
        nuevo = Nodo(nombre)
        if not self.inicio:
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_paciente(self, nombre):
        actual = self.inicio
        anterior = None

        while actual:
            if actual.paciente == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar_lista(self):
        actual = self.inicio
        if not actual:
            print("Lista vacia")
            return
        print("Cola de Atención:")
        while actual:
            print( actual.paciente)
            actual = actual.siguiente
        


lista = ListaAtencion()
lista.agregar_paciente("Javier")
lista.agregar_paciente("Jose")
lista.agregar_paciente("Elisa")
lista.agregar_paciente("Matias")
lista.agregar_paciente("Erick") 

lista.mostrar_lista()
print("\nAtendiendo a Javier...")
lista.eliminar_paciente("Javier")
lista.mostrar_lista()

