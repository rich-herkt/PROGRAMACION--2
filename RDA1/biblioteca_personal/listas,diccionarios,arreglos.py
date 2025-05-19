
#remove solo elimina un UNICO elemento repetido
lista = [1,5,5,2]
lista.remove(5)
print(lista)

#con un bucle for se puede eliminar todos los elementos repetidos
lista2 = [1,5,5,5,2]
for i in lista2:
    lista2.remove(5)
print(lista2)


import array
a=array.array('i',[1,2,3,4])# i indica tipo entero

print(a[0])

#SUMA ACOMULADA

numeros=[1,2,3,4,5]
suma=0
for num in numeros:
    suma+=num
    print("SUMA TOTAL:",suma)
    
#ENCONTRAR NUMERO MAYOR

numeros=[12,45,3,22,89,5]
mayor=numeros[0]

for num in numeros:
    if num> mayor:
        mayor =num
print("El numero mayor es :", mayor)

cuadrados=[]

for i in range(1,6):
    cuadrados.append(i**2)
    
print(cuadrados)

