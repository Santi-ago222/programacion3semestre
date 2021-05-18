texto='hola espero que todo ande bien'
lista=[1,434,53,2,2]
lista.sort()
print(lista)
lista.pop(2)
for elemento in lista:
    print(elemento)
for i in range(len(lista)):
    print(lista[i])

for letra in texto:
    print(letra)

print(texto[1])
palabras= texto.split(' ')
print(palabras)
print(type(palabras))
eliminarE= texto.split('e') ##para separar
print(eliminarE)
datos='nombre;apellido;edad'
print(datos.split(';'))

###para volver a unir###
uniendo='i'.join(eliminarE)
print(uniendo)
info= ' '.join(datos.split(';'))
print(info)

###comparar
listaNombres=['Laura','Juan','Mario','Elsa','Katherin','daniel','Raul']
print(max(listaNombres))

print(max(listaNombres, key=len)) ###este es la mejor forma por que no tma en cuenta el ansi

respuesta=input('Ingrese si o no : ')
print(respuesta.upper())
if respuesta.upper=='si': ##uper para validar que el usuario pueda escribir si o no en mayuscula o minuscula
    print('hola bienvenido al programa')
else:
    print('Chao')

nombre= input('Ingrese su nombre: ') ###para poner la primera en mayuscula
print(nombre.capitalize())

## para volver todo minuscula

correo= 'ESPERO QUE ESTE BIEN'
print(correo.casefold())
print(correo.casefold().capitalize())

#que quede en el centro
saludo='Hola como estas?'
nombre='maria alejandra'
nombres=nombre.split(' ')
nombre= ''
for elemento in nombres:
    nombre += elemento.capitalize() + ' ' ##para convertir el las dos iniciales del nombre en mayuscula
print(nombre)

print(saludo.center(50))
print(nombre.center(50))

enunciado='Hola, hola ya me canse de decir tantos hola pero como vamos hola'
print(enunciado.count('hola')) #para contar los hola
print(enunciado.upper().count('HOLA'))

print(enunciado.find('decir'))
print(enunciado[25:30]) ##posicion

##para cambiar palabras
txt='me gusta programar en java'
print(txt.replace('java', 'phyton'))

##para saber si lo que ingreso el ususario si esta bien
#como saber si el usuario si ingreso algo numerico

##como se yo que el string si es numerico
numerodeID= '123556'
print(numerodeID.isnumeric())

##para verificar que un parrafo si termina en punto
parrafo= 'lsld jwnjnde skjdie skdejifn skeod liberosn dj.'
print(parrafo.endswith('.'))