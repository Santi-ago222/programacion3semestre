# PUNTO 1 #
def lineas ():
    print('#'* 30)

def sumar (numeroA= 0, numeroB= 0,numeroC=0):
    return (numeroA+numeroB+numeroC)


def restar (numeroA=0, numeroB=0, numeroC=0):
    return (numeroA-numeroB-numeroC)

def multiplicar (numeroA=0, numeroB=1,numeroC=1):
    return  (numeroA*numeroB*numeroC)

def dividir ( numeroA=1, numeroB=1, numeroC=1):
    return (numeroA/numeroB/numeroC)

def potenciacion (numeroA=1, numeroB=1,numeroC=1):
    return ((numeroA**numeroB)**numeroC)

def calculadora (operacion, numeroA,numeroB,numeroC):
    print(operacion(numeroA,numeroB,numeroC))
calculadora(sumar,34,76,90)
lineas()
calculadora(restar,12,80,34)
lineas()
calculadora(multiplicar,77,12,45)
lineas()
calculadora(dividir,2,4,9)
lineas()
calculadora(potenciacion,5,9,8)
lineas()

#PUNTO 2# 
def mostrarlista (lista1, lista2,lista3):
    for i in range(len(lista1)):
        print(lista1[i],lista2[i],lista3[i])

edades= [1,2,3,4,5]
años= [2010,2011,2012,2013,2014]
numeros= [6,7,8,9,10]

mostrarlista(edades,años,numeros)
lineas()
#PUNTO 3#

def calcular (base=0, altura=0):
    return (base*altura/2)
print (calcular(98,52))
lineas()

#PUNTO 4#
def topes (Lista):
    Mayor= max(Lista)
    Menor= min(Lista)
    sumador= 0
    for elemento in Lista:
        sumador+=elemento
    Numerodeelementos= len (Lista)
    promedio=sumador/Numerodeelementos
    print('el numero mayor es:', Mayor)
    print('el numero menor es :', Menor)
    print('el promedio es: ', promedio)
Edades= [90,115,203,12,56,78]
topes(Edades)
lineas()

#PUNTO 5#
print('profe la verdad este si esta muy dificil jajaja')


