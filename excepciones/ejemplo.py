#ahora para decir que por favor ingrese un dato valido
iscorrectInfo= False
while(iscorrectInfo==False):
#Para corregir datos mal ingresados
    try:
        edad= int(input('ingrese su edad :'))
        iscorrectInfo= True
    except ValueError:
        print('ingresaste un dato no valido')

nombreArchivo= input('Ingrese el nombre del archivo que desea encontrar : ')
try:
    archivo= open(nombreArchivo)
except FileNotFoundError:
    print(f' el archivo {nombreArchivo}, no se ha encontrado')

base=4
divisor=0
try:
    dividir= base/divisor
except ZeroDivisionError:
    print('no se puede dividir por 0')


nombre='Daniel'
print(nombre.isalpha()) ## alfa son letras
assert (nombre.isalpha()) # el assert sirve para que en algun momento del codigo, dos cosas sean iguales o que tiene que ser asi
iscorrectInfo= False
while(iscorrectInfo==False):
    try:
        nombre= input('ingrese su nombre :')
        assert (nombre.isalpha())
        iscorrectInfo= True
    except AssertionError:
        print('ingresaste un dato no valido')


#Para validar si alguien es mayor de edad
iscorrectInfo= False
while(iscorrectInfo==False):
    try:
        edad= int(input('ingrese su edad :'))
        assert (edad >= 18)
        iscorrectInfo= True
    except AssertionError:
        print('los menores de edad no pueden acceder')
    except ValueError:
        print('las edades son numeros enteros')

listas= [2,34,32,34]
try:
    listas [5]
except:
    print('El indice es mayor al tamaño de la lista')

