TemperaturaCorporal= [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
PreguntaOpcion='''
        1) para hacer conversiones de grados centigrados a kelvin o farenheit
        2) para saber que temperaturas son saludables
        3)Para saber la temperatura maxima y la minima
        4) para finalizar
'''
PreguntaConversionTemperatura='''
        Escoja la opcion que quiere convertir
            F) para pasar de grados centigrados a farenheit
            K) para pasar de grados centigrados a kelvin
            C) para mostrar lista original
'''
MensajeErrorMenu= 'lo sentimos, debes ingresar un numero valido entre 1 y 4'
MensajeErrorConversion= 'Lo sentimos, debes ingresar valida K,F,C'



#---punto1--#
import FuncionPunto1Conversor as ct
temperaturaCoprporalKelvin= ct.conversionTemperatura (TemperaturaCorporal, 'K')
print('la conversion de celsius a Kelvin es :')
print(temperaturaCoprporalKelvin)

TemperaturaCorporalFahrenheit= ct.conversionTemperatura (TemperaturaCorporal, 'F')
print('la conversion de celsius a fahrenheit es :')
print(TemperaturaCorporalFahrenheit)
#---punto2--#
ClasificacionTemperaturas= ct.ClasificarTemperaturas(TemperaturaCorporal)
print(ClasificacionTemperaturas)






Opcion= int(input(PreguntaOpcion))
while(Opcion!=4):
    if(Opcion==1):
        Conversion= input(PreguntaConversionTemperatura)
        if(Conversion=='F'):
            Fn.mostrarLista(TemperaturaCorporalFahrenheit)
        elif(Conversion=='K'):
            fn.mostrarLista(temperaturaCoprporalKelvin)
        elif(Conversion=='C'):
            fn.mostrarLista(TemperaturaCorporal)
            print('para este caso la conversion no era necesaria')
        else:
            print(MensajeErrorConversion)
    elif(Opcion==2):
        fn.mostrarLista(ClasificacionTemperaturas)
        print ('mostrando clasificacion temperaturas')
    elif(Opcion==3):
        ct.MostrarTopes(TemperaturaCorporal)
    else:
        print(MensajeErrorMenu)
    Opcion= int(input(PreguntaOpcion))

print('Adios chaval')
#---NOTA---#
'''
LOS CODIGOS ESTAN BIEN, LO UNICO POR LO QUE NO ME DA ES EL ORDEN DE LAS COSAS Y QUITARLE LOS PRINTS A 
LOS IMPORTS DE LAS FUNCIONES ES DECIR; LINEAS (25 A 30)