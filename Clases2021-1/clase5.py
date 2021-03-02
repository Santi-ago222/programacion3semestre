#---Entradas---#
MENSAJE_SALUDO= "BIENVENIDO A ESTE JUEGO, EN DONDE DEBERAS ACERTAR EL NUMERO CORRECTO, TE DAMOS 3 INTENTOS :"
PREGUNTA_NUMERO= "Di un numero del 1 al 10 :"
ACERTASTE= "felicidades, acertaste el numero que era"
FALLASTE= "lo siento ese, no es el numero, escoge otro"
QUEDAN= "te quedan"
PERDEDOR= 'Lo sentimos acabas de perder tus oportunidades,'
#----codigos---#
print(MENSAJE_SALUDO)
numeroescogido= int(input(PREGUNTA_NUMERO))
numerooculto= 3
vidas=5
if(numeroescogido != numerooculto):
    print(FALLASTE)
    vidas-=1
    print(f" te quedan {vidas} vidas")

while(numeroescogido != numerooculto and vidas > 0):
    numeroescogido=int(input(PREGUNTA_NUMERO))
    vidas-=1
    print(f"te quedan {vidas} vidas, ")

if (vidas>=0 and numeroescogido==numerooculto):
    print(ACERTASTE)
    print(f"al final te quedaron {vidas} vidas")

else:
    print(PERDEDOR,'el numero correcto era el ', numerooculto)

print("GRACIAS POR JUGAR!!!")

