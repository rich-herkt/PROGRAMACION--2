print("""Elaborado por: Richard Herkt
        Fecha: 26/5/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")


contadoro=0
contadoro1=0
def ordenamiento(lista):
    global contadoro, contadoro1
    n = len(lista)  # Guardamos la longitud de la lista

    # Recorremos toda la lista n veces
    for i in range(n):
        
        # En cada pasada, comparamos elementos adyacentes
        for j in range(0, n - i - 1):
            contadoro+=1
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                contadoro1+=1
                # Intercambio usando desempaquetado de tuplas
    return lista

numeros = []
cant=int(input("Ingrese la cantidad de precios que desea ingresar.."))
print("Ingrese sus precios")
for i in range(cant):
    precio=float(input())
    numeros.append(precio)

print("Original:", numeros)
print("Ordenado Booble Sort:", ordenamiento(numeros.copy()))
print("\n")
print("Las comparaciones realizadas en este proceso han sido:",contadoro)
print("Los intercambios realizados en este proceso han sido:",contadoro1)
print("\n")



contadori=0
contadori1=0
def insertion_sort(lista):
    global contadori, contadori1
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        contadori+=1
        actual = lista[i]  # Elemento actual a insertar
        j = i - 1          # Posición anterior

        # Mientras haya elementos mayores que el actual, los movemos una posición a la derecha
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
            

        # Insertamos el elemento en su posición correcta
        lista[j + 1] = actual
        contadori1+=1

    return lista  # Retornamos la lista ordenada
print("Original:", numeros)
print("Ordenado Insertion Sort:", insertion_sort(numeros.copy()))
print("Las comparaciones realizadas en este proceso han sido:",contadori)
print("Los intercambios realizados en este proceso han sido:",contadori1)
print("\n")


contadors=0
contadors1=0
def selection_sort(lista):
    global contadors,contadors1
    n = len(lista)

    # Recorremos todos los elementos
    for i in range(n):
        min_idx = i  # Suponemos que el mínimo está en la posición actual

        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j  # Actualizamos el índice del nuevo mínimo
            contadors+=1

        # Si encontramos un nuevo mínimo, lo intercambiamos con el actual
        if min_idx != i:
            contadors1+=1
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            
            
    return lista   
print("Original:", numeros)
print("Ordenado Selection Sort:", selection_sort(numeros.copy()))        
print("Las comparaciones realizadas en este proceso han sido:",contadors)
print("Los intercambios realizados en este proceso han sido:",contadors1)
print("\n")


#Cómo funciona cada algoritmo?
# Bubble Sort :
# Compara dos elementos que están uno junto al otro y los intercambia si están en el orden incorrecto. Repite este proceso muchas veces hasta que todos estén en orden. Es como cuando revisas una lista y vas "subiendo" los números grandes poco a poco al final, como burbujas.

#Insertion Sort :
# Toma un número de la lista y lo coloca donde debería estar, una por una.

# Selection Sort :
# Busca el número más pequeño de toda la lista y lo pone en la primera posición, luego el siguiente más pequeño en la segunda, y así hasta el final.


# Comparación de rendimientos

# En general, Insertion Sort suele ser más rápido si la lista ya está casi ordenada.

# Bubble Sort es el más lento porque hace muchas comparaciones innecesarias.

# Selection Sort es más rápido que Bubble, pero más lento que Insertion en muchos casos.

# En mi caso, Insertion Sort fue el más eficiente porque si la la lista no esta completamente desordenada, hace  menos movimientos.

#Cuando usaria cada uno ?

# Bubble Sort: solo para enseñar o practicar, ya que no es eficiente para listas largas.

# Insertion Sort: útil cuando tienes pocos datos o la lista está casi ordenada, como ordenar resultados de exámenes conforme van llegando.

# Selection Sort: sirve cuando necesitas minimizar el número de veces que cambias elementos de lugar, como en sistemas donde mover datos cuesta mucho.