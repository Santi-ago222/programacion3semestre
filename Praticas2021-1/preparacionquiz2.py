#--replicando un taller hecho en clase 11/03/2021--#
# ---- Preguntas
preguntaNumero  =  '''
Ingrese alguna de estas opciones
    1.Hacer conversión de pesos a dólares o euros
    2.Agrege un valor a la lista de pesos
    3.Mostrar valor más alto, más bajo y promedio
    4.Eliminar elemento de la lista
    5. Salir
'''
preguntaMoneda  =  '''
    C- Mostrar original en pesos colombiano
    D- Mostrar en Dolares
    E- Mostrar en Euros
'''
preguntarNumero  =  'Ingrese un valor en COP:'
preguntaBorrarCoordenada  =  'Ingrese la posición que desea borrar:'
# ---- Mensajes --- #
mensajePesos  =  'Mostrando lista original'
mensajeDolares  =  'Mostran Lista en dolares'
mensajeEuros  =  'Mostran Lista en euros'
mensajeMayor  =  'El mayor numero ingresado es ->'
mensajeMenor  =  'El menor numero ingresado es ->'
mensajePromedio  =  'El promedio es ->'
mensajeDespedida  = '☺Que tengas un feliz día ☺☻'
mensajeError= 'valor ingresado, no valido'

listapesos= [2000, 3000, 4000, 2500, 1000, 7600]
#--punto 1--#
#conversiones
listaeuros= []
for elemento in listapesos:
    conversor= round (elemento *0.0023, 2)
    listaeuros.append (conversor)

listadolares= []
for elemento in listapesos:
    conversor= round (elemento * 0.0028, 2)
    listadolares.append (conversor)

opcionEscogida=int(input(preguntaNumero))
while(opcionEscogida =! 5):
    #--OPCION 1--Hacer conversión de pesos a dólares o euros-- #
    if (opcionEscogida==1):
        opcionMoneda= input ()
        if (escogemoneda== 'C'):
            print(mensajePesos)
            print(listapesos)
        elif (escogemoneda == 'D'):
            print(mensajeDolares)
            print(listadolares)
        elif (escogemoneda== 'E'):
            print(mensajeEuros)
            print(listaeuros)
        else:
            print(mensajeError)
#--opcion 2--Agrege un valor a la lista de pesos--#
  elif ( opcionEscogida  ==  2 ):
        valorIngresado  =  float ( input ( preguntarNumero ))
        listaPesos . añadir ( valorIngresado )
        imprimir ( listaPesos )
#--opcion 3--Mostrar valor más alto, más bajo y promedio-- #
 elif ( opcionEscogida  ==  3 ):
        imprimir ( mensajeMayor , max ( listaPesos ))
        imprimir ( mensajeMenor , min ( listaPesos ))
        imprimir ( mensajePromedio , sum ( listaPesos ) / len ( listaPesos ))
#--opcion4--Eliminar elemento de la lista--#
elif ( opcionEscogida  ==  4 ):
        imprimir ( listaPesos )
        posicion  =  int ( input ( preguntaBorrarCoordenada )) -  1
        listaPesos . pop ( posicion )
        imprimir ( listaPesos )
#--ultima opcion-- no valida--#
else :
        imprimir ( mensajeErrorEntrada )
    opcionEscogida  =  int ( input ( preguntaNumero ))

print(mensajeDespedida)