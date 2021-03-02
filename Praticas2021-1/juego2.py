import random
#---entradas---#
MENSAJE_SALUDAR= '''
    Bienvenido
        a este programa,
    !!! Vamos a jugar!!!'''
PREGUNTA_NUMERO='''
    En este juego deberas acertar 
    un numero entero del 1 al 10,
    la idea es que lo hagas
    antes de que se acaben tus vidas...
    no existe vida 0...
    exitos!!!!
'''
PREGUNTA_DIFICULTAD='''
        ESCOGE LA DIFICULTAD
    1) FACIL
    2) MODERADO
    3) DIFICIL
'''
MENSAJE_FALLIDO= "Agh, fallaste, ingresa otro numero: "
MENSAJE_GANASTE='felicidades ganaste, por que le acertaste papa'
MENSAJE_PERDISTE='lo siento, perdiste'
#---codigos---#
print(MENSAJE_SALUDAR)
nuemerooculto= random.randint(1,10)
vidas= None
escogerdificultad= int(input(PREGUNTA_DIFICULTAD))
while(escogerdificultad != 1 and escogerdificultad != 2 and escogerdificultad != 3):
    print ('ingrese una opcion valida por favor')
    escogerdificultad=int(input(PREGUNTA_DIFICULTAD))

if(escogerdificultad==1):
    print ('modo facil activado')
    vidas= 5
elif(escogerdificultad==2):
    print('modo moderado activado')
    vidas= 3
else:
    print('modo dificil activado')
    vidas=1

numeroingresado= int(input(PREGUNTA_NUMERO))
while(numeroingresado!= nuemerooculto and vidas>1):
    print(MENSAJE_FALLIDO)
    numeroingresado=int(input(PREGUNTA_NUMERO))

if(numeroingresado==nuemerooculto and vidas>= 0):
    print(MENSAJE_GANASTE)
else:
    print(MENSAJE_PERDISTE)
    print("ESPERO QUE TE HAYA GUSTADO EL JUEGO, ADIOS")
