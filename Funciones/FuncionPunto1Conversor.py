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
        if unidad== 'K':
            conversion= temperatura + 273,15
        elif unidad == 'F':
            conversion= temperatura *1,8 + 32
        else:
            Listaconvertida = None
        Listaconvertida.append (conversion)
        return Listaconvertida
