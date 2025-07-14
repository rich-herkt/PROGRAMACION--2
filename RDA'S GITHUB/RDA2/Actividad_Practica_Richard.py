
print("""Elaborado por: Richard Herkt
        Fecha: 08/5/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n                                     """)

#BUSQUEDA LINEAL 

def busqueda_de_frutas(fruta, fruta_a_buscar):
    # Recorremos toda la lista fruta elemento por elemento fruta_a_buscar
    contador=0 # Variable la cual nos ayudara a contabilizar cuantas veces se ha ejecutado el bucle
    for i in range(len(fruta)):
        # Comparamos cada elemento con la fruta buscada
        contador+=1

        if fruta[i] == fruta_a_buscar:
            return i,contador  
        # Si encontramos la fruta, devolvemos su posición en la lista
    
    return False  # Si no está en la lista, devolvemos False

# Lista de frutas disponibles
fruta = ["manzana", "fresa", "Pera", "banana", "mango", "durazno", "Sandia", "guanabana", "maracuya", "melon"]

try:
    # Solicitamos al usuario ingresar una fruta y convertimos lo convertimos a minusculas
    fruta_a_buscar = input("Ingrese la fruta que desea buscar..").lower()
except ValueError:
    # Manejo de errores en caso de que el usuario no ingrese un valor válido
    print("Error, ingrese una fruta")

# Llamamos a la función de busqueda
busqueda = busqueda_de_frutas(fruta, fruta_a_buscar)

# Comprobamos si la fruta fue encontrada en la lista
if busqueda != False:
    print(fruta_a_buscar, "se encuentra en la lista en la posición", busqueda[0])
    print("El bucle se ha ejecutado",busqueda[1],"veces")
else:
    print("La fruta que ingresaste no se encuentra en la lista de frutas")
    
    
#BUSQUEDA BINARIA 
"\n"
#Variable la cual nos permitira contabilizar cuantas veces se ha ejecutado el bucle
def busqueda_binaria(numeros, numero_a_buscar):
    # Inicializamos los límites de la búsqueda: inicio en 0 y fin la longitud de la lista -1
    inicio = 0
    fin = len(numeros) - 1
    contador=0 #Variable la cual nos permitira contabilizar cuantas veces se ha ejecutado el bucle
    
    # Mientras el inicio no supere el fin, seguimos buscando
    while inicio <= fin:
        # Calculamos el punto medio de la lista
        medio = (inicio + fin) // 2
        contador+=1 #En cada vuelta agregamos un punto a contador
        # Si el elemento en la posición 'medio' es igual al número buscado, retornamos su posición
        if numeros[medio] == numero_a_buscar:
            return medio,contador

        # Si el número en 'medio' es menor al número buscado, descartamos la mitad izquierda
        elif numeros[medio] < numero_a_buscar:
            inicio = medio + 1  # Movemos 'inicio' a la derecha, buscando en la mitad derecha

        # Si el número en 'medio' es mayor al número buscado, descartamos la mitad derecha
        else:
            fin = medio - 1  # Movemos 'fin' a la izquierda, buscando en la mitad izquierda
    
    return None  # Si no encontramos el número, retornamos 'None'

# Lista ordenada de números en la que realizaremos la búsqueda
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Solicitamos al usuario que ingrese el número que desea buscar
numero_a_buscar = int(input("Ingrese el número a buscar: "))

# Llamamos a la función de búsqueda 
busqueda = busqueda_binaria(numeros, numero_a_buscar)

# Verificamos si el número se encontró y mostramos el resultado
print(busqueda)
if busqueda != None:
    print(f"'{numero_a_buscar}' se encontró en la posición {busqueda[0]}.")
    print("El bucle se ha ejecutado",busqueda[1],"veces")
else:
    print(f"'{numero_a_buscar}' no se encuentra en la lista.")
    