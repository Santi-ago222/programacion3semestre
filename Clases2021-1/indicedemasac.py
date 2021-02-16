#-----constantes-----#
PREGUNTA_PESO = "cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en metros ? : "
MENSAJE_BIENVENIDA = "Hola como estas? voy a calcular tu imc. : "
MENSAJE_DESPEDIDA = "Tu imc es : "
#-----entrada codigo-----#
print(MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
IMC = peso/ estatura**2
print(MENSAJE_DESPEDIDA, IMC)
estoyobeso= IMC >= 30
print ("el resultado de el examen de obesidad es...", estoyobeso)

