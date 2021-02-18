#---constantes---#
BIENVENIDOALCODIGO= "hola bienvenido"
MENSAJE_MAYOREDAD= "Eres mayor de edad, puedes seguir"
MENSAJE_MENOREDAD = "Eres menor de edad, no puedes seguir"
PREGUNTA_EDAD= " Que edad tienes ? : "

#---entrada al codigo---#
print (BIENVENIDOALCODIGO)
Edad= int (input(PREGUNTA_EDAD))
ismayoredad = Edad >= 18
resultado = ""
if (ismayoredad) :
    resultado= MENSAJE_MAYOREDAD
else :
    resultado = MENSAJE_MENOREDAD

print (resultado)

