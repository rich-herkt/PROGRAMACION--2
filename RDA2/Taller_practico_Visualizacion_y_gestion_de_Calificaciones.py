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

import time
import pandas as pd
import bisect  # Importamos el módulo 'bisect' que permite trabajar con listas ordenadas de forma eficiente
# Importamos 'matplotlib.pyplot' como 'plt' para crear gráficos y visualizar resultados
import matplotlib.pyplot as plt

# Importamos 'matplotlib.pyplot' como 'plt' para crear gráficos y visualizar resultados
import matplotlib.pyplot as plt

# Importamos 'tqdm' para mostrar barras de progreso mientras se ejecutan ciclos largos
from tqdm import tqdm

# Importamos 'clear_output' desde IPython.display para limpiar la salida en consola o en Jupyter
# Esto es útil para crear animaciones que actualizan la misma celda repetidamente
from IPython.display import clear_output

# También importamos el módulo 'time' con un alias 't' para usarlo independientemente si lo necesitamos
# (por ejemplo, usar t.sleep(0.3) en lugar de time.sleep(0.3) si queremos evitar conflictos o duplicación)
import time as t


# Importamos 'clear_output' desde IPython.display para limpiar la salida en consola o en Jupyter
# Esto es útil para crear animaciones que actualizan la misma celda repetidamente
from IPython.display import clear_output

# También importamos el módulo 'time' con un alias 't' para usarlo independientemente si lo necesitamos
# (por ejemplo, usar t.sleep(0.3) en lugar de time.sleep(0.3) si queremos evitar conflictos o duplicación)
import time as t



import random
notas = random.sample(range(0, 21), 15)  # 15 notas entre 0 y 20 sin repetidos
print(" Notas originales:", notas)


# Parámetros:
# - lista: la lista de números a ordenar
# - mostrar_pasos (bool): si es True, se guardarán los estados intermedios para animación
# - pausa (float): tiempo en segundos entre pasos, útil si se usa para animar (aunque aquí no se usa directamente)
def bubble_sort_viz(lista, mostrar_pasos=False, pausa=0.3):

    # Creamos una copia de la lista para no modificar la original
    lista = lista.copy()

    # Inicializamos contadores para registrar la cantidad de comparaciones e intercambios
    comparaciones = 0
    intercambios = 0

    # Guardamos la longitud de la lista
    n = len(lista)

    # Lista donde se almacenarán los pasos intermedios (solo si mostrar_pasos=True)
    pasos = []

    # Bucle externo que recorre toda la lista
    for i in range(n):
        # Bucle interno que compara elementos adyacentes
        for j in range(0, n - i - 1):
            # Cada vez que se comparan dos elementos, se incrementa el contador de comparaciones
            comparaciones += 1

            # Si el elemento actual es mayor que el siguiente, se deben intercambiar
            if lista[j] > lista[j + 1]:
                # Intercambio de los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                # Incrementamos el contador de intercambios
                intercambios += 1

                # Si mostrar_pasos es True, guardamos el estado actual de la lista (después del intercambio)
                pasos.append(lista.copy())

    # Al finalizar, retornamos:
    # - La lista ordenada
    # - El número total de comparaciones
    # - El número total de intercambios
    # - La lista de pasos intermedios (puede estar vacía si mostrar_pasos=False)
    return lista, comparaciones, intercambios, pasos


tamaños = [10, 50, 100, 200]  # Lista con diferentes tamaños de entrada que vamos a probar

# Lista donde almacenaremos los resultados (comparaciones, intercambios y tiempo por tamaño)
resultados = []

# Usamos tqdm para mostrar una barra de progreso mientras se ejecuta el ciclo
for tam in tqdm(tamaños):

    # Generamos una lista aleatoria de 'tam' elementos, sin repetidos, en un rango proporcional
    lista = random.sample(range(1, tam * 10), tam)

    # Medimos el tiempo justo antes de ejecutar el algoritmo
    inicio = time.time()

    # Ejecutamos bubble_sort_viz pero no nos interesa la lista final ni los pasos,
    # solo las estadísticas de comparaciones e intercambios
    _, comp, interc, _ = bubble_sort_viz(lista)

    # Medimos el tiempo al finalizar
    fin = time.time()
    
    
  
#########################################################################################

# 🎥 Función para animar Bubble Sort paso a paso
def animar_bubble_sort(pasos):
    # Recorremos cada estado intermedio guardado del algoritmo
    for estado in pasos:
        # Limpiamos la salida anterior de la celda para simular una animación continua
        clear_output(wait=True)

        # Dibujamos una gráfica de barras representando el estado actual de la lista
        plt.bar(range(len(estado)), estado, color='skyblue')

        # Agregamos título y etiquetas a la gráfica
        plt.title("Animación Bubble Sort")
        plt.xlabel("Índice")  # Eje X representa las posiciones de la lista
        plt.ylabel("Valor")   # Eje Y representa el valor de cada elemento

        # Pausamos por 0.3 segundos antes de pasar al siguiente paso para que se vea el movimiento
        plt.pause(0.3)

    # Al finalizar, mostramos la última imagen sin limpiar
    plt.show()


# 🧪 Creamos una lista pequeña de 10 elementos aleatorios entre 1 y 30 para que la animación sea clara
lista_demo = random.sample(range(1, 30), 10)

# Ejecutamos bubble_sort_viz con mostrar_pasos=True para capturar cada paso intermedio
_, _, _, pasos_animacion = bubble_sort_viz(lista_demo, mostrar_pasos=True)

# Llamamos a la función de animación con los pasos registrados
animar_bubble_sort(pasos_animacion)


################################################################################################

#🎞️ Función que anima y compara visualmente el proceso de ordenamiento de:
# - Bubble Sort (real, paso a paso)
# - sorted() (simulado, para efectos didácticos)
def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.2):

    # Creamos una copia de la lista original para Bubble Sort
    lista_bubble = lista_original.copy()

    # Calculamos el resultado final de sorted() (lista ordenada) para simularlo paso a paso
    lista_sorted_final = sorted(lista_original)

    # Inicializamos la lista de pasos del algoritmo Bubble Sort (comenzamos con el estado original)
    pasos_bubble = [lista_bubble.copy()]

    # Lista de pasos para simular el comportamiento de sorted()
    pasos_sorted = []

    # 🔄 Generamos los pasos reales de Bubble Sort
    n = len(lista_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                # Intercambiamos los elementos si están fuera de orden
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                # Guardamos el estado actual después del intercambio
                pasos_bubble.append(lista_bubble.copy())

    # 🧪 Simulamos cómo se vería el progreso de sorted() paso a paso
    # Aunque sorted() es inmediato, aquí lo representamos como una transformación progresiva
    lista_simulada = lista_original.copy()
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            # Sustituimos el valor por el que estaría en la lista ordenada
            lista_simulada[i] = lista_sorted_final[i]
        # Guardamos el paso simulado
        pasos_sorted.append(lista_simulada.copy())

    # Definimos el número total de pasos que tendrá la animación (el mayor entre ambos procesos)
    total_pasos = max(len(pasos_bubble), len(pasos_sorted))

    # 🖼️ Animación paso a paso
    for k in range(total_pasos):
        clear_output(wait=True)  # Limpiamos la salida anterior para crear efecto de movimiento

        # Creamos una figura con dos gráficos uno al lado del otro
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        # 🎬 Animación de Bubble Sort (proceso real)
        if k < len(pasos_bubble):
            axs[0].bar(range(len(pasos_bubble[k])), pasos_bubble[k], color='skyblue')
            axs[0].set_title(f"Bubble Sort - Paso {k+1}")
            axs[0].set_ylim(0, max(lista_original) + 5)
        else:
            # Si se terminaron los pasos, mantenemos la vista final
            axs[0].bar(range(len(pasos_bubble[-1])), pasos_bubble[-1], color='skyblue')
            axs[0].set_title("Bubble Sort - Final")

        # 🎬 Simulación animada de sorted() (transformación progresiva)
        if k < len(pasos_sorted):
            axs[1].bar(range(len(pasos_sorted[k])), pasos_sorted[k], color='lightgreen')
            axs[1].set_title(f"sorted() - Paso {k+1}")
            axs[1].set_ylim(0, max(lista_original) + 5)
        else:
            axs[1].bar(range(len(lista_sorted_final)), lista_sorted_final, color='lightgreen')
            axs[1].set_title("sorted() - Final")

        # Acomoda ambos subgráficos para que no se encimen
        plt.tight_layout()

        # Pausa entre cada frame para que la animación sea visible
        plt.pause(pausa)

    # Muestra la última imagen estática al terminar
    plt.show()


# 🎲 Generamos una lista aleatoria con 20 números únicos entre 1 y 50
# Usamos una lista más grande que en los ejemplos anteriores para que la animación
# del ordenamiento sea más notoria, visualmente atractiva y educativa.
lista_demo = random.sample(range(1, 50), 20)

# 🎞️ Ejecutamos la función de animación comparativa simulada
# Esta función mostrará lado a lado:
# - A la izquierda: el proceso real paso a paso del algoritmo Bubble Sort.
# - A la derecha: una simulación paso a paso de cómo `sorted()` iría construyendo la lista ordenada.
animar_comparacion_sorted_bubble_simulada(lista_demo)

########################################################################################################

opcion=input("Desea Ingresar una nueva nota ?? SI(S) o NO(N)..").upper()

while opcion != "S" and opcion != "NO":
    print("Ingrese SI(S) o NO(N)..")
    opcion=input("Desea Ingresar una nueva nota ?? SI(S) o NO(N)..").upper()
if opcion =="S":
    nueva_nota = int(input("Ingrese la nota.."))  # puedes cambiar o pedir por input
    bisect.insort(notas, nueva_nota)
    print("✅ Lista después de insertar la nueva nota:", notas)

else:
    print("OK")
    
    
opcion1=input("Desea buscar una nota? SI(?) o NO(N)").upper()
while opcion != "S" and opcion != "NO":
    print("Ingrese SI(S) o NO(N)..")
    opcion=input("Desea Ingresar una nueva nota ?? SI(S) o NO(N)..").upper()
    
if opcion =="S":
    nota_buscar = int(input("Ingrese la nota que desea buscar..")) # puedes cambiar o pedir por input
    posicion = bisect.bisect_left(notas, nota_buscar)
    if posicion < len(notas) and notas[posicion] == nota_buscar:
        print(f"🔍 La nota {nota_buscar} se encuentra en la posición {posicion}")
    else:
        print(f"❌ La nota {nota_buscar} no está en la lista.")
        
else:
    print("Gracias por usar el programa..")
    
    
    
# Escribe aquí tu reflexión final:
# ¿Qué método te pareció más eficiente o claro para ordenar?

# Sorted siempre será el mejor método para ordenar debido a que es un proceso autoático que funciona de manera rápida y eficiente
#Booble sort por su parte es un método mecánico el cual en listas grandes llega a ser muy ineficiente y lento

# ¿Crees que es útil visualizar el proceso de ordenamiento?

# No, debido a que nos sirve únicamente para monitorear el funcionamieneto de nuestro ordenamiento
# No implementa ninguna funcionalidad a nuestro proceso principal