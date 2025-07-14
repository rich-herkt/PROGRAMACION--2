a=5
b=2.5
c="hola"
d='mundo'
e=True

# print(a,'es de tipo',type(a))
# print(b,'es de tipo',type(b))
# print(c,'es de tipo',type(c))
# print(d,'es de tipo',type(d))
# print(e,'es de tipo',type(e))
#------------------------------------------------------
# nombre=input("Ingrese su nombre..")
# edad=int(input("Ingrese su edad.."))
# altura=float(input("Ingrese su altura.."))

# print("Hola",nombre,"tienes",edad,)

# print("Mides",altura,"metros")
#------------------------------------------------------

# num1=int(input("Introduce el primer numer.."))
# num2=int(input("Introduce el segundo numero.."))

# suma=num1+num2
# resta=num1-num2
# multiplicacion=num1*num2
# division=num1/num2
# potencia=num1**num2
# division_entera=num1//num2
# modulo=num1%num2

# print("La suma es:", suma)
# print("La resta es:",resta)
# print("La mutiplicacion es: ",multiplicacion )
# print("La division es: ",division )
# print("La potencia es: ",potencia )
# print("La division entera es: ",division_entera )
# print("El modulo es: ",modulo )
#------------------------------------------------------

a=10
b=5
c=3

# if a >b:
#     print("a es mayor que b")
    
# if a >b:
#     print(a,"a es mayor que b",b)
# else:
#     print(a,"a es menor que b",b)

# if a>b:
#     print(a,"a es mayor que b",b)
# elif a==b:
#     print(a,"a es igual a b",b)
# else:
#     print(a,"a es menor que b",b)
    
# if a>b:
#     print(a,"a es mayor que b",b)
#     if a>c:
#         print(a,"a es mayor que c",c)
#     else:
#         print(a,"a es menor que c",c)
# else:
#     print(a,"a es menor que b",b)
#     if a>c:
#         print(a,"a es mayor que c",c)
#     else:
#         print(a,"a es menor que c",c)
#------------------------------------------------------

# if b==0:
#     print("No se puede dividir entre cero")
# else:
#     print(a/b)
    
# if b!=0:
#     print(a/b)
# else:
#     print("No se puede dividir entre cero")
    
# if b==0: print("No se puede dividir entre cero")
# else:    print(a/b)
    
#------------------------------------------------------

print("MENU DE OPCIONES\n")

opcion =int(input(""" QUE DESEA HACER?
                  
    1.SUMAR
    2.RESTAR
    3.MULTIPLICAR
    4.DIVIDIR
   
        \n"""))

if opcion <1 or opcion >4 :
    print("OPCION NO VALIDA\n")
    
else:
    num1=float(input("Ingrese el primer numero.."))
    num2=float(input("Ingrese el segundo numero.."))
    if num2==0:
        print("Ingrese un valor diferente de  0\n")
    else:
        if opcion == 1:
            sure=input("Ha seleccionado la Opcion 1.SUMA, es correcto? S/N..").upper()
            if sure=="S":
                print(num1+num2)
            else:
                print("No se realizo ninguna operacion")
        elif opcion == 2:
            sure=input("Ha seleccionado la Opcion 2.RESTA, es correcto? S/N..").upper()
            if sure=="S":
                print(num1-num2) 
            else:
                print("No se realizo ninguna operacion")
            
        elif opcion == 3:
            sure=input("Ha seleccionado la Opcion 3.MULTIPLICACION, es correcto? S/N..").upper()
            if sure=="S":
                print(num1*num2)
            else:
                print("No se realizo ninguna operacion")
            
            
        elif opcion == 4:
            sure=input("Ha seleccionado la Opcion 4.DIVISION, es correcto? S/N..").upper()
            if sure=="S":
                print(num1/num2)
            else:
                print("No se realizo ninguna operacion")
            
