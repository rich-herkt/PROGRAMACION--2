
class Auto:
    def __init__(self,marca,modelo):
        self.marca =marca
        self.modelo=modelo
        self.arrancado=False
        

    def mostrar(self):
        return f"La marca de este auto es {self.marca}y el modelo es{self.modelo}"
    def arrancar(self):
        self.arrancado=True
        return f"El carro esta arrancado"
        
carro1=Auto(input("Ingrese la marca"), input("Ingrese el modelo"))

    
        
print(carro1.mostrar())
print(carro1.arrancar())

class Estudiante :
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    def datos(self):
        print("El estudiante",self.nombre,"tiene",self.edad,"Y esta en ",self.grado)
        
    def estudiar(self):
        
        print('El estudiante esta estudiando')
        
        
estudiante=Estudiante(input("Ingrese su nombre.."),input("Ingrese su edad.."),input("En que grado se encuentra.."))

estudiante.datos()

estudiar=input()
if estudiar.lower() == "estudiar":
    estudiante.estudiar()


class Zorrro:
    
    modelo=12
    marca="apple"
    
telefono1=Zorrro()

print(telefono1.modelo)
print(telefono1.marca)

    