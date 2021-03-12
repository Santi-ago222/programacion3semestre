nombresEstudiantes = ['santi', 'samuel', 'aleja', 'elsa']
print (nombresEstudiantes)
print (nombresEstudiantes[2])
nombresEstudiantes.append("sofia")
print (nombresEstudiantes)
print(nombresEstudiantes[4])
#---edades y estaturas---#
edades= [18,16,11,19,23]
estaturas= [1.67 , 1.74, 1.74 , 1.67]
#--para mostrar al ultimo--#
print (edades[-1])
print (estaturas[-1])
#---para mostar dos primeros---#
print(edades[0:2])
#--para mostar los doa ultimos--#
print(edades[ 3 : ])
#---para ordenar la lista en forma ascendente---#
edades.sort()
print(edades)
#---para ordenar en descendente--#
edades.sort(reverse=True)
print(edades)
#---para decir cual es el numero mas grande de la lista--#
mayor= max(edades)
print(mayor)
#---para decir cual es el numero menor--#
menor= min(edades)
print(menor)
#--para contar cuantos datos hay en la lista--#
largolistaEdades= len (edades)
print(largolistaEdades)
#--para sumar elementos--#
sumaEdades= sum (edades)
print (sumaEdades)
#---para calcular el promedio--#
promedioEdades= sumaEdades/largolistaEdades
print(promedioEdades)
#--para eliminar un elemento de la lista--#
edades.pop(3)
print(edades)
#--para mostrar elemento por elemento--#
largolistaEdades= len (edades)
for indice in range (largolistaEdades):
    print('estoy en la posicion', indice, '  valgo', edades )
print('#'*30)
#--#
largolistaNombres= len (nombresEstudiantes)
for indice in range (largolistaNombres):
    print (nombresEstudiantes [indice])
print('#'*30)
#posiciones Edades con valores pares#
posicionesEdadpares= []
largolistaEdades= len (edades)
for posicion in range (largolistaEdades):
    if (edades [posicion] % 2 == 0 ):
        posicionesEdadpares.append (posicion)
print (edades)
print(posicionesEdadpares)
print('#'*30)
