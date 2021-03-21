#--funcion que no tiene return--#
guardar= print ('hola')
print (guardar)
#--funcion que si tiene return--#
guardar= round (34.5655,2)
print(guardar)
#---estructura de las funciones--#
def linedesing (cantidad,simbolo):
    print (simbolo*cantidad)
    return None
linedesing(40, '#')
linedesing (30, '*')

#---muestre la lista--#
def mostrarLista (listaEntrada):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista= [23,78,90,56,534]
mostrarLista(lista)
linedesing(30,'?')
lista2= [77777777,7777777]
mostrarLista(lista2)

#--ahora para sumar 2 numeros en funcion--#
def sumar (a= 0, b= 0):
    suma= a + b
    return suma
resultado =sumar()
print(resultado)
print(sumar(7,35))
#--restar--3
def restar (a= 0, b =0):
    resta= a - b
    return resta
resultado= restar()
print (resultado)
print (restar(12,77))
#multiplicar#
def multiplicar (a=0 , b=0):
    multiplica= a * b
    return (multiplica)
resultado= multiplicar()
print(resultado)
print(multiplicar(4728,5679))
#--division--#
def division (a=1 , b=1):
    divir= a/b
    return(divir)
resultado= multiplicar()
print(resultado)
print(division(18/17))
