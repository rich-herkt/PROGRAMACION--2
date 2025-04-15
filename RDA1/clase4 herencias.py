

# class Animal:
#     def hablar(self):
#         print("El animal hace un ruido")
#     def sonido(self):
#         print("El animal hace un sonido")
        
# class Perro(Animal):
#     def sonido(self):
#         print("El perro dice !GUAU!")
        
# class Persona(Animal):
#     def hablar(self):
#         print("La persona dice hola")
        
# perro=Perro()
# perro.sonido()
# persona=Persona()
# persona.hablar()
###################################################################################
# class Vehiculo:
#     def moverse(self):
#         print("El vehiculo se mueve")
        
# class Auto(Vehiculo):
#     def moverse(self):
#         print("El auto se mueve ")
        
# vehiculo=Vehiculo()

# vehiculo.moverse()
# auto=Auto()
# auto.moverse()

#################################################################################

class Pajaro:
    def sonido(self):
        print("El pajaro hace un sonido")
        
class Gato:
    def sonido(self):
        print("El gato hace un sonido")
        
def hacer_sonido(animal):
    animal.sonido()
    
gato=Gato()
pajaro=Pajaro()
hacer_sonido(pajaro)

hacer_sonido(gato)
    