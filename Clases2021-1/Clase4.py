#constantes
MENSAJE_DEBIENVENIDA= "hola espero que estes bien"
MENSAJEMAYOR = "el numero A es mayor que B"
MENSAJEMENOR= "El numero A es menor que B : "
MENSAJEIGUAL = "A y B son iguales : "
PREGUNTA_A= "ingrese numero A : "
PREGUNTA_B= "ingrese numero B : "

#--entrada al codigo--#
print(MENSAJE_DEBIENVENIDA)
NumeroA= int (input(PREGUNTA_A))
NumeroB= int (input(PREGUNTA_B))
Ismayor = NumeroA > NumeroB
Ismenor = NumeroA < NumeroB
Resultado = ""


if(Ismayor):
    print(MENSAJEMAYOR)
    Resultado = MENSAJEMAYOR
elif (Ismenor):
    print (MENSAJEMENOR)
    Resultado = MENSAJEMENOR
else :
    print (MENSAJEIGUAL)
    Resultado= MENSAJEIGUAL
print (Resultado)



