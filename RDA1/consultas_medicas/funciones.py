
from paciente import Paciente

pacientes = []

def agregar_paciente():
    nombre = input("Ingrese su nombre: ").lower()
    cedula = input("Ingrese su C.I.: ")
    edad = int(input("Ingrese su edad: "))
    tipo_sangre = input("Ingrese su tipo de sangre: ")
    paciente =Paciente(nombre, cedula, edad, tipo_sangre)
    pacientes.append(paciente)
    print("Paciente registrado con éxito.")

def datos_consulta():    
    cedula = input("Ingrese la cedula del paciente a buscar: ").lower()
    paciente = buscar_paciente(cedula)  

    if paciente:
        fecha = input("Ingrese la fecha de consulta: ")
        diagnostico = input("Ingrese el diagnóstico: ")
        tratamiento = input("Ingrese el tratamiento: ")
        
        paciente.agregar_consulta(fecha, diagnostico, tratamiento)
        print("Consulta agregada exitosamente.")
    else:
        print("Paciente no encontrado.")

def buscar_paciente(cedula):
    for paciente in pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None

def mostrar_paciente():
    cedula = input("Ingrese la cedula del paciente a buscar: ").lower()
    paciente = buscar_paciente(cedula)
    if paciente:
        paciente.mostrar_datos()
    else:
        print("Paciente no encontrado.")

def mostrar_todos():
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            paciente.mostrar_datos()
            