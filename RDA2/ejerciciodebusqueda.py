
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


def encontrar_libro(nombres,objetivo):
    contador=0
    for i in range(len(nombres)):
        contador+=1
        if nombres[i] ==objetivo:
            return i,contador
    return False


productos = [
    "pan integral",
    "leche descremada",
    "café",
    "arroz blanco",
    "aceite de oliva",
    "detergente líquido",
    "jabón de baño",
    "pasta dental",
    "papel higiénico",
    "harina",
    "azúcar morena",
    "huevos",
    "chocolate en barra",
    "queso",
    "polvo de hornear"
]
print("""
      
BIENVENIDO A LA TIENDITA!!
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
""")

try:
    producto=input("Ingrese el nombre del producto el cual quiere buscar..").lower().strip()
except ValueError:
    print("Ingrese un nombre valido..")
    
busqueda=encontrar_libro(productos,producto)

if busqueda != False:
    print(f"El producto {producto} se encuentra en la posicion {busqueda[0]}\n")
    print("El bucle se ha ejecutado ",busqueda[1],"veces\n")
else:
    print("El producto no se encuenta disponible")
    
# BÚSQUEDA BINARIA
productos= sorted(productos, key=lambda x: x.lower())
inicio = 0
fin = len(productos) - 1
encontrado_binaria = False
contador1=0
while inicio <= fin:
    medio = (inicio + fin) // 2
    contador1+=1
    titulo_medio = productos[medio].lower()
    
    if titulo_medio == producto:
        
        print(f"[Búsqueda Binaria] Libro encontrado en la posición {medio}. El buscle se ha ejecutado {contador1} veces")
        encontrado_binaria = True
        break
    elif producto < titulo_medio:
        fin = medio - 1
    else:
        inicio = medio + 1

if not encontrado_binaria:
    print("[Búsqueda Binaria] Libro no encontrado.")
    






    