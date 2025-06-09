print("""Elaborado por: Richard Herkt
        Fecha: 09/6/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")


# Creamos una pila vacía para almacenar tareas pendientes
tareas = []
# Agregamos tres tareas a la pila
tareas.append("Estudiar pilas en Python")
tareas.append("Hacer ejercicios de estructuras de datos")
tareas.append("Leer documentación oficial de Python")
tareas_trabajada=tareas.copy()
#Aqui agregamos elementos  ala pila esto es Push

# Mostramos el estado actual de la pila
print("Tareas pendientes:", tareas)
print("\n")

print("""|-----------------Peek---------------------|""")
# Mostramos la tarea más reciente (el tope de la pila)
if tareas:
    print("Tarea más reciente:", tareas_trabajada[-1])
else:
    print("No hay tareas pendientes.")
print("""|------------------------------------------|\n""")

print("""|-----------------Pop---------------------|""")
# Quitamos la última tarea (la más reciente)
if tareas_trabajada:
    completada = tareas_trabajada.pop()
    print("Tarea completada:", completada)
else:
    print("No hay tareas para completar.")
print("""|------------------------------------------|\n""")
    
print("\n Aqui mostramos con [-1] el elemento que esta al final de la pila esto es Peek")
print("Ademas quitamos el elemento que esat al final de la pila con pop() esto es Pop\n")
    
    
print("""|-----------------isEmpty---------------------|""")
# Verificamos si aún hay tareas pendientes
if len(tareas.copy()) == 0:
    print("Todas las tareas han sido completadas.")
else:
    print("Tareas restantes:", tareas_trabajada)
print("Aqui verifiamos si la pila esta vacia, esto es isEmpty\n")
print("""|------------------------------------------|\n""")

print("Lista trabajada:",tareas_trabajada,"\n")
print("Lista Original:",tareas)
