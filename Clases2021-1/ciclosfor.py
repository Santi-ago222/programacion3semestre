for iteracion in range (10):
    print(iteracion)
print('#'*60)
for iteracion in range (12):
    print(iteracion+1)
print('#'*60)
for iteracion in range (1,16,2):
    print(iteracion)
print('#'*60)

Residuo= 5%4
print(Residuo)
Residuo=4%4
print(Residuo)
print('#'*60)

for iteracion in range (1,11):
    if (iteracion % 2 == 0 ):
        print(iteracion)
print('#'*60)

for iteracion in range (1,11):
    if(iteracion % 2 == 0):
        print(iteracion, '---> es un numero par')
    else:
        print(iteracion,'---> es un numero impar')

rango= int (input('ingrese rango maximo :'))
opcion= int(input ('''
    1- ver solo impares
    2- ver solo pares
    3- ver las dos clasificaciones
    4- no ver nada


'''))

print('#'*30)
if(opcion==1):
    for iteracion in range(1, rango +1):
        if (iteracion % 2 != 0):
            print(iteracion,'---> numero impar')
elif(opcion==2):
    for iteracion in range(1, rango +1):
        if(iteracion % 2 == 0):
            print(iteracion,'---> numero par')
elif(opcion==3):
    for iteracion in range (1, rango + 1):
        if (iteracion % 2 == 0):
            print(iteracion,'---> es un numero par')
        else:
            print(iteracion,'---> es un numero impar')

else:
    print('mostrando nada')