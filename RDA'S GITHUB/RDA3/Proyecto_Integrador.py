print("""Elaborado por: Richard Herkt
        Fecha: 7/7/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")


while True:

    print("""                           ----BIENVENIDO----
                |                                    |
                |    1)Gestion de Reportes Medicos   |
                |    2)Simulacion de Evacuacion      |
                |    3)Registro de Visitas Médicas   |
                |    4)Bitacora de Incidentes        |
                |    5)Salir del Programa            |\n""")
    option=input("Que programa desea Utilizar?..")
    print("\n")
    if option=="1":
        class ReporteMedico:
            def __init__(self, tipo, observacion):
                self.tipo = tipo
                self.observacion = observacion  

        # Clase PilaReportes
        class PilaReportes:
            def __init__(self):
                self.pacientes=[]

            def agregar_reporte(self, tipo, observacion):
                pacientes=ReporteMedico(tipo,observacion)
                self.pacientes.append(pacientes)
                

            def eliminar_reporte(self):
                if self.pacientes !=[]:
                    atendido=self.pacientes.pop()
                    print("----REPORTE ELIMINADO----")
                    print("-"+" Paciente atendido con :",atendido.tipo)
                    print("-----------------")
                else:
                    print("Error! No hay reportes guardados")
            def mostrar_reportes(self):
                if self.pacientes !=[]:
                    print("----REPORTES RESTANTES----")
                    for i in self.pacientes:
                        print("-"+"Tipo:",i.tipo)
                        print("-"+"Observacion:",i.observacion )
                    print("-----------------")
                else:
                    print("No existen reportes guardados")
        pila=PilaReportes()


        while True:
            
            print("""                 ----GESTION DE REPORTES MEDICOS----
                |                                   |
                |   1)Agregar reporte               |
                |   2)Eliminar Reporte              |
                |   3)Mostrar Reportes Existentes   |
                |   4)Salir                         |\n""")                     
            opcion=input("Ingrese la opcion deseada..")
            
            if opcion =="1":
                tipo=input("Ingrese el tipo de enfermedad..")
                observacion=input("Ingrese la observacion..")
                pila.agregar_reporte(tipo,observacion)
                print("Reporte Agregado con exito!")
                print("\n")
                
            elif opcion=="2":
                pila.eliminar_reporte()
            elif opcion=="3":
                
                pila.mostrar_reportes()

            elif opcion=="4":
                print("Gracias por la visita!")
                break
            else:
                print("Ingrese una opcion valida..")




    #######################################################################################################################
    elif option=="2":
        # Clase EstudianteEvacuacion
        class EstudianteEvacuacion:
            def __init__(self, nombre, aula):
                self.nombre = nombre
                self.aula = aula
                self.siguiente= None

        # Clase ColaEvacuacion
        class ColaEvacuacion:
            def __init__(self):
                self.cabeza=None# Completa la implementación
                self.cola=None

            def agregar_estudiante(self, nombre, aula):
                nuevo=EstudianteEvacuacion(nombre,aula)
                if not self.cabeza:
                    self.cabeza=nuevo
                    self.cola=nuevo
                else:
                    self.cola.siguiente=nuevo
                    self.cola=nuevo
                    
            def atender_estudiante(self):
                if self.cabeza is not None:
                    atendido=self.cabeza
                    print("Estudiante Evacuado:",atendido.nombre,"|","Aula:",atendido.aula)
                    self.cabeza=self.cabeza.siguiente
                else:
                    print("No hay mas estdiantes que evacuar")
            def mostrar_en_espera(self):
                actual=self.cabeza
                print("PACIENTES EN COLA:")
                while actual is not None:
                    print(actual.nombre,end="->")
                    actual=actual.siguiente
                print("FIN")
        evacuados=ColaEvacuacion()


        while True:
            
            print("""                 ----GESTION DE EVACUACION ESCOLAR----
                |                                   |
                |   1)Agregar Estudiante            |
                |   2)Evacuar Estudiante            |
                |   3)Mostrar Estudiantes en cola   |
                |   4)Salir                         |\n""")                     
            
            opcion=input("Ingrese la opcion deseada..")
            
            if opcion=="1":
                nombre=input("Ingrese el nombre del estudiante..")
                aula=int(input("Ingrese el numero del aula.."))
                print("Estudiante agregado con exito!")
                evacuados.agregar_estudiante(nombre,aula)
                
            elif opcion=="2":    
                    evacuados.atender_estudiante()
                    
            elif opcion=="3":
                print("------COLA DE EVACUACION------")
                print("\n")

                print("\n")
                evacuados.mostrar_en_espera()
                print("------------------------------")
            
            
            elif opcion=="4":
                print("SIMULACION FINALIZADA")
                break
            else:
                print("Opcion no valida")




    ##########################################################################################################################
    elif option=="3":
        class VisitaMedica:
            def __init__(self, estudiante, motivo, fecha):
                self.estudiante = estudiante
                self.motivo = motivo
                self.fecha = fecha

        # Nodo doble
        class NodoDoble:
            def __init__(self, visita):
                self.visita = visita
                self.anterior = None
                self.siguiente = None

        # Clase ListaVisitas
        class ListaVisitas:
            def __init__(self):
                self.actual = None

            def agregar_visita(self, visita):
                visitas=NodoDoble(visita)
                
                if not self.actual:
                    self.actual=visitas
                else:
                    
                    self.actual.siguiente=visitas
                    visitas.anterior=self.actual
                    self.actual=visitas

            def retroceder(self):
                if self.actual is None:
                    print("No hay visitas aun..")
                elif self.actual.anterior is not None:
                    self.actual=self.actual.anterior
                    print("Ficha del Paciente:",self.actual.visita.estudiante)
                else:
                    print("No existen mas reportes")

            def avanzar(self):
                if self.actual is None:
                    print("No hay visitas aun..")
                elif self.actual.siguiente is not None:
                    self.actual=self.actual.siguiente
                    print("Visitante:",self.actual.visita.estudiante)
                else:
                    print("No existen mas reportes")

            def mostrar_actual(self):
                print("------FICHA MEDICA------")
                print(self.actual.visita.estudiante)
                print(self.actual.visita.motivo)
                print(self.actual.visita.fecha)
                print("------------------------")

        paciente=ListaVisitas()
        while True:
            
            print("""                 ----REGISTRO DE VISITAS MEDICAS----
                |                                   |
                |   1)Agregar Visita                |
                |   2)Avanzar a la siguiente visita |
                |   3)Retroceder visita             |
                |   4)Mostrar Visita actual         |
                |   5)Salir                         |\n""")                     
            
            opcion=input("Ingrese la opcion deseada..")
            
            if opcion=="1":
                nombre=input("Ingrese el nombre del visitante..")
                motivo=input("Ingrese el motivo de la visita..")
                fecha=input("Ingrese la fecha de la visita..")
                print("Visita Agregada con exito!")
                print("\n")
                paciente.agregar_visita(VisitaMedica(nombre,motivo,fecha))
                
            elif opcion=="2":
                print("\n")
                paciente.avanzar()
                
            elif opcion=="3":
                paciente.retroceder()
            elif opcion=="4":
                print("\n")
                paciente.mostrar_actual()
                
            elif opcion=="5":
                print("Gracias por su visita..")
                break
            else:
                print("Ingrese una opcion valida..")


    ##########################################################################################################################
    elif option=="4":
        
        # Clase Incidente
        class Incidente:
            def __init__(self, anio, tipo):
                self.anio = anio
                self.tipo = tipo

        # Nodo simple
        class NodoIncidente:
            def __init__(self, incidente):
                self.incidente = incidente
                self.siguiente = None

        # Clase ListaBitacora
        class ListaBitacora:
            def __init__(self):
                self.inicio = None

            def agregar_incidente(self,incidente):
                incidente=NodoIncidente(incidente)
                
                if not self.inicio:
                    self.inicio=incidente 
                else:
                    actual=self.inicio
                    while actual.siguiente:
                        actual = actual.siguiente
                    actual.siguiente = incidente
        

            def eliminar_incidente(self, anio):
                
                
                if self.inicio and self.inicio.incidente.anio == anio:
                    self.inicio = self.inicio.siguiente
                    return

                actual = self.inicio
                while actual and actual.siguiente:
                    if actual.siguiente.incidente.anio == anio:
                        actual.siguiente = actual.siguiente.siguiente
                        return
                    actual = actual.siguiente



            def buscar_incidente(self, anio):
                actual = self.inicio
                while actual:
                    if actual.incidente.anio == anio:
                        print(" Incidente encontrado:")
                        print(f"Motivo: {actual.incidente.tipo}")
                        print(f"Año: {actual.incidente.anio}")
                        return
                    actual = actual.siguiente
                print(" No se encontró ningún incidente para ese año.")


            def mostrar_incidentes(self):
                actual = self.inicio
                if not actual:
                    print("La bitácora está vacía.")
                    return

                print(" Incidentes registrados:")
                while actual:
                    print(f"Año: {actual.incidente.anio}, Tipo: {actual.incidente.tipo}")
                    actual = actual.siguiente

        bitacora=ListaBitacora()
        while True:
            
            print("""                --BITACORA DE INCIDENTES ESCOLARES--
                |                                   |
                |   1)Agregar Incidente             |
                |   2)Eliminar Incidente            |
                |   3)Buscar Incidente              |
                |   4)Mostrar Incidentes            |
                |   5)Salir                         |\n""")                     
            
            opcion=input("Ingrese la opcion deseada..")
            
            if opcion=="1":
                anio=int(input("Ingrese el año del suceso.."))
                tipo=input("Ingrese el tipo de incidente..")
                print("Agregado con exito!")
                print("\n")
                bitacora.agregar_incidente(Incidente(anio, tipo))
            elif opcion=="2":
                anio=int(input("Ingrese el año del suceso a eliminar.."))
                bitacora.eliminar_incidente(anio)
                
            elif opcion=="3":
                anio=int(input("Ingrese el año del suceso a buscar.."))
                bitacora.buscar_incidente(anio)
            elif opcion=="4":
                
                bitacora.mostrar_incidentes()
                
            elif opcion=="5":
                print("Gracias por la visita..")
                break
            else:
                print("Ingrese una opcion valida..")
            
    elif option=="5":
        print("Gracias por la visita.. :)")
        break
        
    else:
        print("Ingrese ua opcion valida..")