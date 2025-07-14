
from funciones import agregar_libro,  mostrar_datos, mostrar_todos, agregar_prestamo

while True:
    print("\n1. Registrar un Libro")
    print("2. Registrar Un prestamo")
    print("3. Mostrar Informacion de un Libro")
    print("4. Mostrar los libros registrados")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        agregar_prestamo()
    elif opcion == "3":
        mostrar_datos()
    elif opcion =="4":
        mostrar_todos()
        
    elif opcion == "5":
        print("Gracias por usar nuestro programa ")
        break
    else:
        print("Opción no válida.")