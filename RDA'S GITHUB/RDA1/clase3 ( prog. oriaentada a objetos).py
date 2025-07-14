
#funciones recursivas
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Adios master!")
    print("Fin de la función",numero)
cuenta_regresiva(5)

# def factorial(numero):

def suma(x,y):
    sum=x+y
    return sum
print(suma(1,2))

class Persona:
    def __init__(self, nombre, edad,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    def descripcion(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y soy {self.ocupacion}"
    
persona1= Persona("Juan", 30, "Ïngeniero")
persona2=Persona("Maria",25,"Doctora")

print(persona1.descripcion())
print(persona2.descripcion())
    
    
class Persona:
    def __init__(self, nombre, edad,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    def descripcion(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y soy {self.ocupacion}"
nombre=input("Ingrese su nombre..")
edad=int(input("Ingrese su edad.."))
ocupacion=input("Ingrese su ocupacion..")

#creamos un objeto de tipo Persona con la informacion porporcionada por el usuario
nueva_persona = Persona(nombre,edad,ocupacion)

#Mostramos la descripcion de la persona creada
print("\n Informacion de la persona creada")
print(nueva_persona.descripcion())

class Persona:
    def __init__(self,nombre,edad,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        
    def descripcion(self):
        return f"Me llamo {self.nombre}, tengo {self.edad} años y soy :{self.ocupacion}"
def mostrarmenu():
    print("1. Agregar Persona")   
    print("2. Mostrar Todas las personas")
    print("3. Buscar persona por nombre")
    print("4.Salir")
        
personas=[]
    
while True:
    mostrarmenu()
    opcion = input("Ingrese la opcion que desee: ")
        
    if opcion=="1":
        nombre=input("Ingrese el nombre de la persona: ")
        edad=int(input("Ingrese la edad de la persona: "))
        ocupacion=input("Ingrese la ocupacion de la persona: ")
        nueva_persona=Persona(nombre,edad,ocupacion)
        personas.append(nueva_persona)
        print(f"la persona {nombre} ha sido agregada")
            
    elif opcion=="2":
        if len(personas) > 0:
            print("\n---- Lista de personas---")
                
            for persona in personas:
                    print(persona.descripcion())
        else:
            print("No hay personas registradas")
                
    elif opcion =="3":
        if len(personas) > 0:
            nombre_buscar=input("Ingrese el nombre de la persona a buscar: ")
            encontrada=False
            for persona in personas:
                if persona.nombre.lower()==nombre_buscar.lower():
                    print(persona.descripcion())
                    print("Persona encontrada")
                    encontrada=True
                    break
            if not encontrada:
                print(f"No se encontro a  {nombre_buscar} en la lista")
        else:
                print("No hay personas registradas")
    elif opcion=="4" :
        print("Gracias por utilizar el programa")
        break
    else:
        print("Opcion no valida. Por favor Seleccione una opcion valida")
    
    