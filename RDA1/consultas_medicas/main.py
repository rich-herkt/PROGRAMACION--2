
from funciones import agregar_paciente, mostrar_todos, mostrar_paciente, datos_consulta

while True:
    print("\n1. Agregar paciente")
    print("2. Mostrar paciente")
    print("3. Mostrar todos los pacientes")
    print("4. Agregra Consulta")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        mostrar_paciente()
    elif opcion == "3":
        mostrar_todos()
    elif opcion =="4":
        datos_consulta()
        
    elif opcion == "5":
        print("Gracias por usar nuestro programa ")
        break
    else:
        print("Opción no válida.")