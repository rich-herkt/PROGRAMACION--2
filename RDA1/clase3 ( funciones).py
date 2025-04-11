
def funcion(nombre):
    print("Estamos estudiando python",nombre)
    
funcion("Edison")
print("\n")

print("Paso de argumentos a una funcion")

def datos(nombre,apellido):
    
    print("Estamos estudiando Python",nombre,apellido)
datos("Richard","Herkt")
datos(apellido="Herkt",nombre="Richard") #NOMINAL

print("\n")

print("Retorno de una funcion ")

def area_triangulo(base,altura):
    calc=base*altura/2
    print(calc)
area_triangulo(2,3) #POSICIONAL
area_triangulo(4,5)

print("\n")

print("Argumentos por defecto..")

def welcome(nombre="zorro",lenguaje ="Python"):
    print("Bienvenido a",lenguaje,nombre + "!")
    
welcome()

welcome("Richard","PHP")

print("\n")

print("PASAR UN NUMERO INDETERMINADOS DE ARGUMENTOS")

def menu(*platos):
    print("Hoy tenemos :" , end="")
    for plato in platos:
        print(plato,end=",")
        
menu("Pasta", "Pizza", "Sushi")

def contacto(**info):
    print("Informacion de contacto: ")
    
    for vlave,valor in info.items():
        print(vlave,":",valor)
contacto(nombre="Richard", email="algo@gmail.com")
print("\n")
contacto(nombre="Richard", email="algo@gmail.com", direccion="Quito-ecuador")
