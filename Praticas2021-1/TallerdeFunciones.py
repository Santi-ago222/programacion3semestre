
#1) Dada una lista muestrela en pantalla elemento a elemento #
def mostrandolista (lista):
    for elemento in lista:
        print(elemento)


Nombres = ['pablo', 'vanesa', 'maria', 'camilo']
mostrandolista (Nombres)

# 2) Dada una lista de numeros enteros, muestre el mas grande,pequeño y el promedio
ListadeEnteros = [23,45,78,99,10,18,19,7,17]
suma= sum(ListadeEnteros)
print(suma)
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
Edades= [55,78,99,12,56,78]
topes(Edades)

# 3) SALUDE N VECES
def saludo (cantidad):
    print('Hola capo  '   * cantidad)
saludo(17)

# 4)Que devuelva todos los números pares de una lista de números enteros
def numerospares (lista):
    pares= []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append (elemento)
    return pares
Edades= [55,78,99,12,56,78]
devuelvapares= numerospares(Edades)
print (devuelvapares)

# 5) QUE DEVUELVA UNICAMENTE MAYORES A 24 
def mayorlista (lista):
    Mayores= []
    for elemento in lista:
        if elemento > 24 :
            Mayores.append (elemento)
    return Mayores
Edades= [55,78,99,12,56,78]
mayoresde= mayorlista(Edades)
print(mayoresde)

# 6) CREE UNA FUNCION PARA EL IMC
def calcularimc (peso, altura):
    return peso /(altura**2)
Imc= calcularimc(35,78.3)
print('su indice de masa corporal es: ', Imc)

# 7) FUNCION PARA DESPEDIRSE