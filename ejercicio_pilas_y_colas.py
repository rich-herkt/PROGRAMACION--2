print("""Elaborado por: Richard Herkt
        Fecha: 16/6/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")

class PilasTareas:
    
    def __init__(self):
        self.items=[]

    def agergar_tarea(self,nombre):
        
        print("-----TAREAS DEL DIA -----")
        self.items.append(nombre)
        print("Se ha agregado la terea:",nombre)
        
    def terminar_tarea(self):
        
        terminada=self.items.pop()
        print("Se ha finalizado la actividad:",terminada)
        
    def mostrar_actual(self):
        actual=self.items[-1]
        print("Se encuentra realizando la actividad:",actual)
        
    def longitud(self):
        restantes=len(self.items)
        print("Tareas restantes:",restantes)
    
    def pendientes(self):
        return self.items
    
    def estavacio(self):
        
        return len(self.items)==0


mesero=PilasTareas()


print("-------------------------------------------------------------------------------------\n")


while True:
    print("""
	1)Cargar Tareas del dia
	2)Mostrar Tarea Actual
	3)Terminar tarea
	4)Consultar tareas pendientes
	5)Verificar si la lista esta vacia
 	6)Salir\n""")
    
    
    opcion=int(input("Ingrese la opcion deseada.."))
    if opcion==1:
        if mesero.estavacio():
            mesero.agergar_tarea("- Al final del turno, dejar todo listo para el siguiente día")
            mesero.agergar_tarea("- Llevar la comida y las bebidas a la mesa sin accidentes.")
            mesero.agergar_tarea("Sonreír y hacer que los clientes se sientan bienvenidos.")
            mesero.agergar_tarea("Revisar que los platos estén correctos antes de servirlos.")
            mesero.agergar_tarea("Cobrar sin equivocarse y dar el cambio correcto.")
            mesero.agergar_tarea("Sugerir platillos si alguien no sabe qué pedir.")
            mesero.agergar_tarea("Limpiar las mesas para que estén listas para los siguientes clientes.")
            mesero.agergar_tarea("Escuchar y ayudar si hay quejas o pedidos especiales.")
            mesero.agergar_tarea("Trabajar en equipo para que el servicio sea rápido y organizado.")
            mesero.agergar_tarea("Tomar pedidos y asegurarse de que todo esté claro.")
        else:
            print("Ya has cargado las Tareas del dia..")
    elif opcion==2:
        if  not mesero.estavacio():
            mesero.mostrar_actual()
        else:
            print("Aun no hay elementos en la lista :)")
    elif opcion==3:
        if  not mesero.estavacio():
            mesero.terminar_tarea()
        else:
            print("No hay elementos en la lista :)") 
        
    elif opcion==4:
        if  not mesero.estavacio():
            print("----- TAREAS PENDIENTES-----\n")
            print(mesero.pendientes(),"\n")
            print("----------------------------\n")
            mesero.longitud()
        else:
            print("Aun no hay elementos en la lista :)")
    elif opcion==5:
        if  not mesero.estavacio():
            print("La lista no esta vacia..")
            mesero.longitud()
        else:
            print("Aun no hay elementos en la lista :)")
    elif opcion ==6:
        if not mesero.estavacio():
            print("Aun no puedes salir TIENES QUE TERMINAR TU TRABAJO!!")
        else :
            print(" Puedes irte..Te veo veo el dia siguiente")
            break    
	
	


class ColaPrioridadClientes:
    def __init__(self):
        self.items = []
        
    def agregar_cliente(self, nombre, prioridad):
        self.items.sort(key=lambda x: x[1])
        self.items.append((nombre,prioridad))
        print("Ingreso al paciente",nombre,"con prioridad",prioridad)
        
        
    def atender_cliente(self):
        
        print("Se esta atendiendo a ",self.items[0][0],"Con prioridad",self.items[0][1])
        atendido=self.items.pop(0)
        print("Se ha atendido a ",atendido[0],"Con prioridad",atendido[1],"\n")

        
        
    def mostrar_pendientes(self):
        print("Clientes pendientes..")
        print(self.items)
    def tamaño(self):
        print("Clientes Pendientes")
        print(len(self.items))
    
    def vacia(self):
        return len(self.items)==0
    
    
cola_atencion = ColaPrioridadClientes()

cola_atencion.agregar_cliente("Marcelo", 1)
cola_atencion.agregar_cliente("Juana", 3)
cola_atencion.agregar_cliente("Esteban", 2)
cola_atencion.agregar_cliente("Alejandro", 4)
cola_atencion.agregar_cliente("Dylon", 8)
cola_atencion.agregar_cliente("Gabriel", 6)
cola_atencion.agregar_cliente("Jorge", 5)
cola_atencion.agregar_cliente("Victor ", 7)

print("\n")

cola_atencion.mostrar_pendientes()
cola_atencion.tamaño()
print("\n")
while not cola_atencion.vacia():
    cola_atencion.atender_cliente()
    print("\n")
    cola_atencion.mostrar_pendientes()
    cola_atencion.tamaño()
        
        

# Reflexión final

# Explica en tus propias palabras: ¿Qué diferencias observas entre el funcionamiento de una PILA y una COLA CON PRIORIDAD?

#La Pila Nos permite Resolver Tareas de la mas reciente a la mas antigua, sin importar la prioridad ni el orden en el que llego, debido a q usa el principio LIFO
# En cambio la cola nos permite distinguir entre las prioridades y resolver las Tareas segun su importancia debido a q usa el principio FIFO