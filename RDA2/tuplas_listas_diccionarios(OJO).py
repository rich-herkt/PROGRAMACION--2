print("""Elaborado por: Richard Herkt
        Fecha: 30/5/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")


clientes = [
    ("Carlos", 20.5),
    ("Maria", 35.0),
    ("Juan", 150.0),
    ("Esteban", 850.0),
    ("Alejandro", 10.0),
    ("Jorge", 200.0),
    ("Gabriel", 45.0),
    ("Xavier", 120.0),
    ("Alex", 45.0),
    ("Matias", 120.0)
]

def insertion_sort_por_nombre(lista):
    # Ordenamos los productos según su nombre (posición 0 de la tupla)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0].lower() > actual[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def selection_sort_por_precio(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j][1] < lista[min_idx][1]:  # Comparamos por precio (índice 1)
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def busqueda_binaria_nombre(lista_ordenada, objetivo):
    inicio = 0
    fin = len(lista_ordenada) - 1
    comparaciones = 0

    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        nombre = lista_ordenada[medio][0].lower()

        if nombre == objetivo.lower():
            return medio, comparaciones
        elif objetivo.lower() < nombre:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1, comparaciones  # No encontrado


inventario_ordenado_por_nombre=insertion_sort_por_nombre(clientes.copy())
print("Inventario Ordenado por nombre:")
for i in inventario_ordenado_por_nombre: 
    print(i)
print("\n")

inventario_ordenado_por_precio=selection_sort_por_precio(clientes.copy())

print("Inventario ordenado por precio:")
for productos in inventario_ordenado_por_precio: 
    print(productos)
print("\n")

print("Ingrese el nombre del cliente que desea buscar..")
try:
    nombre=input("")
except Exception:
    print("Ingrese el nombre del cliente que desea buscar..")
    nombre=input("")
    
busqueda=busqueda_binaria_nombre(inventario_ordenado_por_nombre,nombre)

if busqueda[0] != -1:
    print(f"\ncliente encontrado: {nombre} en posición {busqueda[0]}")
else:
    print("\ncliente no encontrado.")

print(f"Comparaciones realizadas: {busqueda[1]}")

try:
    opcion=input("Desea Ingresar Un nuevo Cliente  SI(S) NO(N)?").upper()
except Exception:
    print("Ingrese (S) o (N)")
    opcion=input("Desea Ingresar Un nuevo Cliente  SI(S) NO(N)?").upper()

while opcion != "S" and opcion!= "N":
    print("Ingrese (S) o (N)")
    opcion=input("Desea Ingresar Un nuevo Cliente  SI(S) NO(N)?").upper()

if opcion=="S":
    cliente=input("Ingrese el nombre del cliente..")
    saldo=float(input("Ingrese el saldo del cliente.."))
    clientes.append((cliente,saldo))
    print("\n")
    print("Cliente agregado con exito..")
    for j in clientes: 
        print(j)
elif opcion=="N":
    print("OK, hasta luego")
    

####################################################################################################

# ¿Por qué es necesario ordenar antes de realizar la búsqueda binaria?

# Es debido a la manera en la que trabaja la búsqueda binaria, realiza comparaciones según el valor de lo que se está buscando.

# ¿Qué pasaría si usamos la búsqueda binaria sin ordenar primero?

# Si la lista está desordenada, el algoritmo podría descartar la mitad equivocada y nunca encontrar el número correcto.
# También puede dar una posición incorrecta, porque los valores no siguen un orden lógico.

# ¿Qué ventajas viste entre la búsqueda binaria y la búsqueda lineal?

# Ambos son algoritmos de búsqueda muy buenos, nos permiten recorrer la lista y encontrar a nuestro objetivo.
# La búsqueda binaria funciona únicamente con listas ordenadas, lo que nos permite un funcionamiento eficiente
# y ahorrar tiempo.
# La búsqueda lineal, en cambio, es muy buena en listas desordenadas debido a que busca y compara los elementos uno a uno.

# ¿Cuál de los dos ordenamientos te pareció más intuitivo de implementar y por qué?

# Considero que el Selection Sort, debido a que su manera de funcionamiento es bastante simple e intuitiva de comprender.
# Además, considero que el hecho de que su ordenamiento sea primero encontrando el valor más pequeño lo hace bastante entendible.