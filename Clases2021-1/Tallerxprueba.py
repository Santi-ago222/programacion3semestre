#PRIMER PUNTO- NUMEROS
Numero1= 89
Numero2= 77
MENSAJEMAYOR= "El numero mayor es"
#IGUALES
isiguala= Numero1==Numero2
print(isiguala)
#CUAL ES MAYOR
ismayor= Numero1 > Numero2
print(ismayor)

print(MENSAJEMAYOR,Numero1)


#---PUNTO2---#
#----CONSTANTES---#
MENSAJE_DE_BIENVENIDA= "Hola, bienvenido a tu calculadora"
PREGUNTA_EDAD = "Cual es tu edad? : "
MENSAJE_MENOREDAD= "Eres menor de edad : "
MENSAJE_JOVEN = "estas joven : "
MENSAJE_ADULTO= "Eres adulto: "
MENSAJE_ADULTO_MAYOR = "Eres adulto mayor : "
MENSAJE_DE_DESPEDIDA= "Espero que te haya servido,adios : "


#---CODIGOS---#
Edad= int (input(PREGUNTA_EDAD))
Ismenor= Edad < 18
isjoven = Edad >=18 and Edad == 25
isadulto = Edad >= 26 and Edad == 60
isadultomayor = Edad > 60 
if (Ismenor):
    print= (MENSAJE_MENOREDAD)
elif (isjoven):
    print= (MENSAJE_JOVEN)
elif (isadulto):
    print= (MENSAJE_ADULTO)
else:
    print= (MENSAJE_ADULTO_MAYOR)















