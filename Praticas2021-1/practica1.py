#---MENSAJES---#
CULPABILIDAD="señor hemos investigado el caso del asesinato, y lo declaramos el principal responsable. :"
PREGUNTA= "Se declara usted culpable? : "
DICTAMEN= "Iras a la carcel  "
DICTAMEN2= "Iras a casa"
#---codigos---#
print (CULPABILIDAD)
pregunta1= input(PREGUNTA)
if (pregunta1== "si"):
    print(DICTAMEN)
else:
    print(DICTAMEN2)
