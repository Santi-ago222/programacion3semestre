#---FUNCIONES SIN ENTRADA---#
def linedesing ():
    print('#'*45)
linedesing ()
print('Hola hola')

#--FUNCIONES CON UNA ENTRADA--#

#mostrando cierta cantidad de numerales (#)--#
def linedesingCantidad (cantidad):
    print ('#'*cantidad)
linedesingCantidad (32)
# O tambien se puede de esta forma--#
def linedesingCantidad (cantidad= 32):
    print('#'*cantidad)
linedesingCantidad ()

#FUNCIONES CON VARIAS ENTRADAS#

#funcion suma#
def sumar (valor1=0 , valor2=0):
    return (valor1+ valor2)
print(sumar(34,56))
linedesing()
print(sumar())
linedesing()
#-- funcion restar--#
def restar (valor1=0 , valor2=0):
    return (valor1- valor2)
print(restar(47,65))
linedesing()

#--funcion multiplicar--#
def multiplicar (valor1=1 , valor2=0):
    return (valor1* valor2)
print(multiplicar(45,190))
linedesing()

#--funcion dividir--#
def dividir (valor1=1 , valor2=1):
    return (valor1/ valor2)
print(dividir(45,72))
linedesing()
print(dividir())
linedesing()

#--funcion potenciacion--#
def potenciacion (valor1=1 , valor2=1):
    return (valor1** valor2)
print(potenciacion(90,56))
linedesing()

#FUNCIONES DENTRO DE FUNCIONES#
def calculadora (accion, valor1, valor2):
    print(accion(valor1,valor2))
calculadora(sumar,56,89)
calculadora(restar,4,6)
calculadora(multiplicar,56,123)