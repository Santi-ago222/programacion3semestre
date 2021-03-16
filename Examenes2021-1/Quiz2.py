#--DatoInicial--#
ListaDeTemperaturas= [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
#--preguntas--#
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
PreguntaDoctor= 'doctor por favor ingrese el dato de la temperatura en que se encuentra el paciente :'
#---Mensajes--#
MensajeErrorMenu= 'lo sentimos, debes ingresar un numero valido entre 1 y 4'
MensajeErrorConversion= 'Lo sentimos, debes ingresar valida K,F,C'


#--PreguntaMenu--#
Opcion= int(input(PreguntaOpcion))

#--ListasParacalculos--#
ListaFarenheit=[]
ListaKelvin=[]

#--conversiones--#
#--de Celsius a Farenheit--#
for elemento in ListaDeTemperaturas:
    farenheit= (elemento * 1,8 + 32)
    ListaFarenheit.append(farenheit)
#--pasando a Kelvin--#
for elemento in ListaDeTemperaturas:
    Kelvin= (elemento+ 273)
    ListaKelvin.append(Kelvin)
ListaDiagnostico=[]
#--Temperaturas saludables--#
for elemento in ListaDeTemperaturas:
    Clasificando=''
    if (elemento < 36):
        Clasificando='usted esta en un rango de hipotermia, mucho cuidado'
    elif(elemento> 37.6):
        Clasificando= 'Usted esta en un rango de fiebre, prestele atencion'
    elif(elemento>= 36 and elemento <= 37.6):
        Clasificando='usted esta en un rango de temperatura normal'
    else:
        Clasificacion= 'su caso ya es preocupante'
    ListaDiagnostico.append(Clasificando)
#--calculando la T maxima y minima--#
Maximo= max (ListaDeTemperaturas)
Minimo= min (ListaDeTemperaturas)

#--Menu--#
while(Opcion!=4):
    #--1-#
    if(Opcion==1):
        Conversion= input(PreguntaConversionTemperatura)
        if(Conversion=='F'):
            print(ListaFarenheit)
        elif(Conversion=='K'):
            print(ListaKelvin)
        elif(Conversion=='C'):
            print(ListaDeTemperaturas)
            print('para este caso la conversion no era necesaria')
        else:
            print(MensajeErrorConversion)
    elif(Opcion==2):
        for i in range(len(ListaDeTemperaturas)):
            print(ListaDeTemperaturas[i])
            print(ListaDiagnostico[i])
    elif(Opcion==3):
        print('la temperatura maxima fue', Maximo)
        print('la temperatura minima fue', Minimo)
    else:
        print(MensajeErrorMenu)

    Opcion=int(input(PreguntaOpcion))

print('gracias por usar este programa, feliz dia')
