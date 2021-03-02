#---entradas---#
MENSAJEBIENVENIDA= "Muy buenos dias, despierte que esta en clase de 6 "
PREGUNTAMENU= '''ingrese
        1- para mostrar los numeros del 1 al 5
        2- para preguntar tu nombre
        3- para mostrarte el año en que estamos
        4- para salir
'''
MENSAJE_ERROR= "Por favor ingresa una opcion valida"
PREGUNTANOMBRE= "Como te llamas? : "
#---CODIGOS---#
print(MENSAJEBIENVENIDA)
entrada= 1
while(entrada>=1 and entrada<=3):
        entrada= int(input(PREGUNTAMENU))
        if(entrada==1):
                print("1,2,3,4,5")
        elif (entrada==2):
                print(PREGUNTANOMBRE)
        elif(entrada==3):
                print("el año en que estamos es el 2021")
        elif(entrada==4):
                print('muchas gracias por usar este programa, feliz dia dormilon')
        else:
                entrada=1
                print(MENSAJE_ERROR)


