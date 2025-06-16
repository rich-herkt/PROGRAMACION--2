print("""Elaborado por: Richard Herkt
        Fecha: 13/6/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")

class ColaPrioridadHospital:
        
        def __init__(self):
                self.items=[]
                

        def encolar(self,nombre,prioridad):
                
                self.items.append((nombre,prioridad))
                print("Ingreso al paciente",nombre,"con prioridad",prioridad)

                
        
        def desencolar(self):
                if not self.esta_vacia():
                        self.items.sort(key=lambda x: x[1])
                        print("Atendiendo a- ",self.items[0])
                        atendido=self.items.pop(0)
                        print("Se antendio a- ",atendido[0],"Prioridad- ",atendido[1])
                        print("\n")
                        restantes=len(self.items)
                        print("--------------------------------------------")
                        print("Pacientes en espera- ",restantes)
                        print("--------------------------------------------")
                        print("\n")
                else:
                # Si la cola está vacía, informamos
                        print("No hay clientes para atender.")
                        return None
                        
                return atendido
        
        def restantes(self):
                print(f"Pacientes por atender")
                print(self.items)
                print("\n")
                
        def esta_vacia(self):
        # Retorna True si la lista no tiene elementos
                return len(self.items) == 0
        

cola_atencion = ColaPrioridadHospital()

cola_atencion.encolar("Marcelo", 1)
cola_atencion.encolar("Juana", 3)
cola_atencion.encolar("Esteban", 2)
cola_atencion.encolar("Alejandro", 4)
cola_atencion.encolar("Dylon", 8)
cola_atencion.encolar("Gabriel", 6)
cola_atencion.encolar("Jorge", 5)
cola_atencion.encolar("Victor ", 7)

cola_atencion.restantes()

while not cola_atencion.esta_vacia():
    cola_atencion.desencolar()
    print("\n")
                
