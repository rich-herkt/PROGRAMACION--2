
# class Persona:
#     def __init__(self,nombre,edad,ocupacion):
#             self.nombre = nombre
#             self.edad = edad
#             self.ocupacion = ocupacion
#     def descripcion(self):
#         return f"Me llamo {self.nombre}, tengo {self.edad} años y soy :{self.ocupacion}"
    
# while True:
#     try:
#         print("""MENU DE OPCIONES
#                 1. Agregar Persona   
#                 2. Salir""")
#         opcion= int(input('Ingrese la opcion que desee: '))
#         if opcion ==1:
#             persona1=Persona(input("Ingrese su nombre.."),int(input("Ingrese su edad..")),input("Ingrese su ocupacion.."))
#             print(persona1.descripcion())
        
#         if opcion==2:
#             break
#     except ValueError:
#         print("Error, ingrese un valor numerico")
#     except KeyboardInterrupt:
#         print("\nSaliendo del programa...")
#         break
    
# class Libro:
#     def __init__(self,titulo,autor,anio):
#         self.titulo=titulo
#         self.autor=autor
#         self.anio=anio
        
    
#     def descripcion(self):
#         return f"El nombre es {self.titulo}, el tema es {self.autor} y el año es {self.anio}"
    
    
# libro1=(Libro("Pepito y sus amigos ", "Richard Herkt", 2020))
# print(libro1.descripcion())
    

        
# class estudiante:
#     def __init__(self,nombre,carrera,nota_final):
#         self.nombre=nombre
#         self.carrera=carrera
#         self.nota_final=nota_final
        
#     def presen(self):
#         return f"Hola! mi nombre es {self.nombre}, sigo la carrera de {self.carrera} y mi nota final es {self.nota_final}" 
    
#     def veri(self):
#         if self.nota_final>=7:
#             return "Estoy Aprobado "
#         else:
#             return "Reprobado "
        
# persona1=estudiante(input("Ingrese su nombre.."),input("Ingrese su carrera.."),float(input('Ingrese su nota final..')))

# print(persona1.presen())
# print(persona1.veri())        
        

    
    
        
