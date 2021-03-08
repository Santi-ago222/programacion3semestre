#---punto1---#
sumatoria = 0
for iteracion in range (101):
    sumatoria+=iteracion
    print('--> la sumatroria de los numeros es', iteracion)
#---punto2---#
Mensajenumero='por favor ingrese un numero entero positivo, para mostrar su factorial : '
numero=int(input(Mensajenumero))
factorial=1
for iteracion in range(numero):
    factorial= factorial* (iteracion+1)
print('el numero que usted ingreso en factorial es', factorial)
#---tercer punto---#
positivossuma=0
promediopositivos=0
sumanegativos=0
for iteracion in range (6):
    numeros= int(input('ingrese 6 numeros enteros ya sean positivos o negativos, diferentes de cero :'))
    if numeros> 0:
        positivossuma= positivossuma+numeros
        promediopositivos= promediopositivos+1
    else:
        sumanegativos= sumanegativos + numeros
print('la suma de los numero negativos fue:', sumanegativos)
if promediopositivos != 0:
    promediopositivos= positivossuma/promediopositivos
    print('el promedio de los positivos fue:', promediopositivos)
else:
    print('usted no ingreso numeros positivos,por ende no le puedo dar el promedio de los postivos, adios')
#---cuartopunto--#
