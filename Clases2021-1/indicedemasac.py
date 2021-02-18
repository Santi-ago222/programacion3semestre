#-----constantes-----#
PREGUNTA_PESO = "cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en metros ? : "
MENSAJE_BIENVENIDA = "Hola como estas? voy a calcular tu imc. : "
MENSAJE_DESPEDIDA = "Tu imc es : "
MENSAJE_BAJO_PESO = "Estas en los huesos, necesitas bienestarina"
MENSAJE_PESONORMAL= "Estas melo caramelo"
MENSAJE_SOBREPESO= "Ya te andas pasando bro"
MENSAJE_OBESO = "Ya andas al borde del infarto "
#-----entrada codigo-----#
print(MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
IMC = peso/ (estatura**2)
isbajopeso= IMC  <  18,5
isnormal = IMC >=  18.5  and IMC <  25 
issobrepeso = IMC >=  25  and IMC  <  30
Resultado =""
if (isbajopeso) :
    Resultado=MENSAJE_BAJO_PESO
elif (isnormal):
    Resultado=MENSAJE_PESONORMAL

else:
    Resultado= MENSAJE_SOBREPESO
print (MENSAJE_DESPEDIDA, IMC)
print(Resultado)




