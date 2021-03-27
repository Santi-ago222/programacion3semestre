def conversionTemperatura (temperaturas, unidad):
    '''
    convierte una lista de temperaturas segun 
    la unidad ingresada, puede ser:
            K: para pasar de Celsius a Kelvin
            F: para pasar de Celsius a Farenheit 
    En caso de que ingrese un valor invalido, le devolvemos nada.
    '''
    Listaconvertida = []
    for temperatura in temperaturas:
        conversion= None
        if unidad== 'F':
            conversion= temperatura * 1.8 + 32
        elif unidad == 'K':
            conversion= temperatura + 273.15
        else:
            Listaconvertida = None
        Listaconvertida.append (conversion)
    return Listaconvertida
def ClasificarTemperaturas (listaTemperaturas):
    '''
    Retorna la clasificacion de
    las temperaturas ingresadas 
    que estan en celsius
    '''
    ListaClasificacion= []
    for temperatura in listaTemperaturas:
        estado = None
        if temperatura < 36:
            estado= 'Hipotermia'
        elif temperatura >= 36 and temperatura < 37:
            estado= 'Normal'
        else:
            estado= 'Fiebre'
        ListaClasificacion.append (estado)
    return ListaClasificacion
def MostrarTopes (listaTemperaturas):
    Mayor= max(listaTemperaturas)
    menor= min(listaTemperaturas)
    PeriodoHoras= round(24/len(listaTemperaturas),2)
    print('la temperatura mayor es :', Mayor)
    print('la temperatura Menor es:', menor)
    print ('el periodo de muestras es; ', PeriodoHoras)


