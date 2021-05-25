#Punto1. Calcular el IMC de un usuario, 
# pero valide que los datos de entrada sean los correctos 
# en caso de que alguna entrada sea errónea 
# vuelva a solicitar el ingreso del dato hasta que sea correcto 
# (adicionalmente pida el nombre y valide que sea un nombre válido).

def validateFloat(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print('datos incorrectos ingrese nuevamente')
    return valor 

def validateString(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print('datos incorrectos ingrese nuevamente')
    return valor 
validateString ('nombre :')
validateFloat('ingrese Peso :')

#Calcular imc => Estatura , peso =>peso/estatura^2
def pedirDatosEPN():
    '''
    Se le pide al usuario el peso la estatura 
    y el nombre
    validando que la data este buena
    '''
    preguntaPeso = 'Ingrese su peso en kg :'
    preguntaEstatura = 'Ingrese su estatura en metros : '
    preguntaNombre = 'Ingrese su Nombre :'
    peso = validateFloat(preguntaPeso)
    estatura = validateFloat(preguntaEstatura)
    nombre = validateString (preguntaNombre)
    return peso,estatura, nombre

def calcularIMC ():
    pesoIn, estaturaIn, nombreIn = pedirDatosEPN()
    imc = pesoIn/ (estaturaIn**2)
    return imc, nombreIn
calcularIMC()
imc, nombre = calcularIMC()
print(imc, nombre)
print(f'El imc de {nombre} es de {imc} %')