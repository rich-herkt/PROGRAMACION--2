
#con un bucle for se puede eliminar todos los elementos repetidos si los elementos se repiten mas de 2 veces
lista2 = [1, 2, 2, 2, 2, 4, 5]
for i in lista2:
    lista2.remove(2)
print(lista2)

#esta parte va comentada porque sino no funca
# lista3 = [1, 2, 2, 4, 5]
# for i in lista3:
#     lista2.remove(2)
# print(lista3)

#mismo ejercicio con try y except
lista3 = [1, 2, 2, 4, 5]
for i in lista3:
    try:
        lista3.remove(2)
    except ValueError:
        pass
print(lista3)

try:
    num1=int(input("Ingrese un numero.."))
    print(num1)
except ValueError:
    print("No es un numero valido..")
    
    
#BUSQUEDA LINEAL
def busqueda_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i]==objetivo:
            return i
    return -1

datos=[1,2,3,4,5]
print(busqueda_lineal(datos,3))


lista=[5,3,8,6,2,7,4,1]

for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):
        
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1]=lista[j+1],lista[j]
            
        print(lista[j], lista[j+1], end= "")
        
print(lista)

lista=[5,3,8,6,2,7,4,1]
lista.sort()
print(lista)
