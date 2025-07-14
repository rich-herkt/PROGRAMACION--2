
print("""Elaborado por: Richard Herkt
        Fecha: 08/5/2024
        Carrera: Ing. Sistemas de la Información  
        Ing.Edison Emeneses\n""")
print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\n""")


# Que es la busqueda lineal, como funciona ?

# La búsqueda lineal es un método de búsqueda algorítmica que nos permite encontrar elementos 
# recorriendo la lista uno por uno hasta encontrar el deseado.
# La búsqueda lineal recorre cada elemento de la lista hasta encontrar su objetivo.
# Este método de búsqueda es usualmente utilizado en listas de elementos cortas.

#----------------------------------------------------------------------------------------------------
#Que es la busqueda binaria, como funciona?

# La búsqueda binaria es un método de búsqueda algorítmica, más complejo que la búsqueda lineal.
# Nos permite encontrar un objetivo dentro de una lista necesariamente ordenada, optimizando el tiempo de búsqueda y los recursos.
# La búsqueda binaria divide la lista en mitades y realiza comparaciones entre las posiciones de los elementos,
# reduciendo progresivamente el espacio de búsqueda hasta encontrar el objetivo.

#----------------------------------------------------------------------------------------------------
# ¿En qué caso nos conviene usar cada una?
#
# Al momento de querer realizar búsquedas, ambos métodos son efectivos, sin embargo,
# hay que tener en cuenta que la búsqueda lineal recorre toda la lista de inicio a fin.
# Es eficiente cuando se trata de listas no ordenadas y cortas, pero si tenemos listas largas,
# este proceso será más lento y consumirá más memoria.
#
# Por otra parte, la búsqueda binaria es más versátil en listas cortas o largas, 
# pero requiere que la lista esté ordenada para operar. Al realizar la búsqueda,
# detecta si el elemento se encuentra en una posición más alta o más baja dentro de la lista,
# lo que optimiza el proceso.


def encontrar_producto(nombres, objetivo):  
    contador = 0  # Contador para medir cuántas iteraciones hace el bucle  
    for i in range(len(nombres)):  
        contador += 1  
        if nombres[i] == objetivo:  # Si el producto es encontrado, se retorna su índice y número de iteraciones  
            return i, contador  
    return False  # Si el producto no es encontrado, se devuelve False  

productos = [  
    "pan integral", "leche descremada", "café", "arroz ", "aceite de oliva",  
    "detergente líquido", "jabón de baño", "pasta dental", "papel higiénico",  
    "harina", "azúcar morena", "huevos", "chocolate", "queso",  
    "polvo para hornear", "mantequilla", "sal", "yogur ", "galletas ", "botella de agua"  
]  

productos_buscados = []  # Lista para almacenar los productos que han sido buscados  

print("""  
BIENVENIDO A LA TIENDITA!!  
──────▄▀▄─────▄▀▄  
─────▄█░░▀▀▀▀▀░░█▄  
─▄▄──█░░░░░░░░░░░█──▄▄  
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█  
""")  

while True:  
    producto = input("Ingrese el nombre del producto el cual quiere buscar o escriba (salir) para salir..").lower().strip()  

    while producto == "":  # Aseguramos que el usuario no ingrese un campo vacío  
        producto = input("Ingrese el nombre del producto el cual quiere buscar o escriba (salir) para salir ..").lower().strip()  

    busqueda = encontrar_producto(productos, producto)  

    if producto == "salir":  # Condición para salir del programa  
        print("Gracias por visitar la Tiendita..")  
        if not productos_buscados:  
            print("No se realizaron búsquedas hoy..")  
        else:  
            print("Los productos buscados del día han sido:", productos_buscados)  
        break  
    else:  
        productos_buscados.append(producto)  # Agregar producto a la lista de búsquedas  
        if busqueda != False:  
            print(f"[Búsqueda Lineal] El producto {producto} se encuentra en la posición {busqueda[0]}\n")  
            print("El bucle se ha ejecutado ", busqueda[1], "veces\n")  
        else:  
            print("[Búsqueda Lineal] El producto no se encuentra disponible\n")  

        # BÚSQUEDA BINARIA  
        productos = sorted(productos, key=lambda x: x.lower())  # Ordenamos la lista  
        inicio = 0  
        fin = len(productos) - 1  
        encontrado_binaria = False  
        contador1 = 0  

        while inicio <= fin:  # Implementación de búsqueda binaria  
            contador1 += 1  
            medio = (inicio + fin) // 2  
            titulo_medio = productos[medio].lower()  

            if titulo_medio == producto:  # Si encontramos el producto  
                print(f"[Búsqueda Binaria] Producto encontrado en la posición {medio} (en la lista ordenada).")  
                print(f"El bucle se ha ejecutado {contador1} veces\n")  
                encontrado_binaria = True  
                break  
            elif producto < titulo_medio:  # Ajustamos los límites de la búsqueda  
                fin = medio - 1  
            else:  
                inicio = medio + 1  

        if not encontrado_binaria:  # Si el producto no fue encontrado  
            print("[Búsqueda Binaria] Producto no encontrado.\n")  

