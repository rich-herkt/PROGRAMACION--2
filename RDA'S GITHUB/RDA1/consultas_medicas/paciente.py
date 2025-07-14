
class Paciente:
    def __init__(self, nombre, cedula, edad, tipo_sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.consultas = []  # Lista de diccionarios

    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        consulta = {
            "fecha": fecha,
            "diagnostico": diagnostico,
            "tratamiento": tratamiento
        }
        self.consultas.append(consulta)

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de Sangre: {self.tipo_sangre}")
        print("Consultas:")
        if not self.consultas:
            print("  No hay consultas registradas.")
        else:
            contador = 1
            for consulta in self.consultas:
                print(f"  Consulta {contador}:")
                print(f"    Fecha: {consulta['fecha']}")
                print(f"    Diagnóstico: {consulta['diagnostico']}")
                print(f"    Tratamiento: {consulta['tratamiento']}")
                contador += 1
        
        
        
        

    
        