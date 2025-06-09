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

historial = ["google.com","python.org","stackoverflow.com"]
while True:
	print("""
	1)Ingresar a nuevas paginas web
	2)Mostrar el historial Actual
	3)Consultar pagina Actual
	4)Regresar
	5)Verificar si el historial esta vacio \n""")
	opcion=int(input("Ingrese la opcion deseada.."))

	if opcion==1:
		# Mostrar el historial 
		print("Historial:", historial,"\n")
		# Agrega las páginas visitadas aquí
		print("Ingrese sus paginas o Ingrese (S) para Salir ")
		while True:
			
			nuevas=input("\n").upper()
			if nuevas=="S":
				break
			else:
				historial.append(nuevas)


	elif opcion ==2:
		# Muestra el historial actual
		print("Historial:", historial,"\n")
	
	elif opcion==3:
		# Verifica si hay páginas y muestra la más reciente
		if historial:
			print("Página actual:", historial[-1])
		else:
			print("No hay páginas en el historial")	

	elif opcion==4:
		# Elimina la última página visitada y muestra el historial restante
		if historial:
			try:
				eliminada = historial.pop()
				print("Volviste desde:", eliminada)
				print("Página actual:",historial[-1],"\n")
			except IndexError:
				print("Ya no puedes regresar Estas en la pagina inicial")
				
		else:
			print("No puedes volver, historial vacío.")


	elif opcion==5:
		# Verifica si el historial está vacío
		if len(historial)==0:
			print("El historial está vacío.")
		else:
			print("El historial no esta vacio:", historial)
		
	else:
		print("Gracias por usar el programa..")
		break


