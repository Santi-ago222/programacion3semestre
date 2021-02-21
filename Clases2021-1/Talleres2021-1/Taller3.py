#---PUNTO1---#
NUMEROA= 7
NUMEROB= 17
if (NUMEROA > NUMEROB):
    print("El numero A es mayor que B")
elif (NUMEROB > NUMEROA):
    print("El numero B es mayor que A")
else:
    print ("son iguales")

#----PUNTO2----#
#---CONSTANTES---#
MENSAJE_DE_BIENVENIDA = "HOLA, CALCULARE  EN QUE ETAPA DE TU VIDA ESTAS : "
PREGUNTA_EDAD = "CUANTOS AÑOS TIENES? : "
ERES_MENOR_DE_EDAD= "ERES MENOR DE EDAD :"
ERES_JOVEN= "ERES UNA PERSONA JOVEN : "
ERES_ADULTO = "ESTAS EN TU EDAD ADULTA :"
ADULTO_MAYOR= "ERES UN ADULTO MAYOR : "


#-----CODIGOS----#
print(MENSAJE_DE_BIENVENIDA)
Edad = int(input(PREGUNTA_EDAD))
if(Edad < 18):
    print(ERES_MENOR_DE_EDAD)
elif (Edad >= 18 and Edad <= 25):
    print(ERES_JOVEN)
elif (Edad >= 26 and Edad <= 60):
    print (ERES_ADULTO)
else:
    print(ADULTO_MAYOR)

#---PUNTO3---#
DAME_ELAÑOACTUAL= "Dime en que año estamos actualmente? : "
DAME_CUALQUIER_AÑO= "Ahora dime cualquier año? : "
HAN_PASADO= "Los años que han pasado desde el son : "
AÑOS_FALTANTES= "Los años que faltan desde el son: "
#---CODIGOS---#
pregunta1= int(input(DAME_ELAÑOACTUAL))
pregunta2= int(input(DAME_CUALQUIER_AÑO))
resta= pregunta1-pregunta2
resta2= pregunta2-pregunta1
if (pregunta1>= pregunta2):
    print(f"LOS AÑOS QUE HAN PASADO DESDE EL {pregunta2} hasta el {pregunta1} son {resta}")
else:
    print(f"LOS AÑOS QUE FALTAN DESDE EL {pregunta1} HASTA EL {pregunta2} son {resta2} ")

#----CUARTOPUNTO----#
DAME_UNA_DISTANCIA= ("DAME UNA DISTANCIA EN CENTIMETROS : ")
#----CODIGOS----#
NUMERO1= 100
numero0= 0
NUMERO2= 100000
NUMERO3= 10
MENSAJE_DE_DESPEDIDA = "Hasta pronto, espero que te haya servido el programa"
centimetros= int(input(DAME_UNA_DISTANCIA))
if (centimetros<=numero0):
    print ("escriba una distancia que no sea cero")
else:
    milimetros= centimetros*NUMERO3
    print(f"la conversion de centimetros a milimetros es {milimetros} milimetros") 
    metros = centimetros / NUMERO1
    print(f"la conversion de centimetros a metros es {metros}, metros")
    kilometros = centimetros/NUMERO2
    print(f"la conversion de centimetros a kilometros es {kilometros}, kilometros ")






