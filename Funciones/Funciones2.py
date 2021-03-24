#--suma--#
def sumar (a= 0, b= 0):
    '''
        devuelve la suma de a y b
        por defecto A vale 0 al igual que B
    '''
    suma= a + b
    return suma
#--restar--#
def restar (a= 0, b =0):
    resta= a - b
    return resta
#multiplicar#
def multiplicar (a=0 , b=0):
    multiplica= a * b
    return (multiplica)
#--division--#
def division (a=1 , b=1):
    divir= a/b
    return(divir)
#--funciones dependientes de otras--#
def calcular (operacion,numeroA,numeroB):
    print(operacion(numeroA, numeroB))


print(multiplicar(367,86))
calcular(multiplicar,55,87)
calcular(sumar,1290,567)