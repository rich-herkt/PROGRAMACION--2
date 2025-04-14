
class Persona:
    def __init__(self,nombre,edad,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        
    def descripcion(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y soy :{self.ocupacion}"
    
persona1= Persona(input("Ingrese su nombre.."),int(input("Ingrese su edad..")),input("Ingrese su ocupacion.."))
persona2=Persona(input("Ingrese su nombre.."),int(input("Ingrese su edad..")),input("Ingrese su ocupacion.."))
print(persona1.descripcion())
print(persona2.descripcion())