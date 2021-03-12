Escojaunaopcion='''
            escoja:
            1) para hacer conversiones desde un lista de dolares
            2) para saber en que rango de ingresos esta usted
            3) para mostrar el ingreso mas bajo, alto y el promedio de ingresos
            4) para salir
'''
ParaConvertir= '''
    C- para convertir dolares a pesos colombianos
    D- para mostrar la listaa original en dolaretes
    E- para convertir los dolares en euros
'''
MensajePesoscop= 'la conversion de dolares a pesos colombianos es la siguiente : '
MensajeListaoriginal= 'mostrando lista original, scs no es necesaria la conversion pero igual te la muestro :'
MensajeEuros= 'la conversion de dolares a euros es la siguiente : '
MensajeError= 'lo sentimos , ese valor no es valido'
Mensajeopcion= 'la opcion que usted escogio fue :'


ListaClasificacion= []
Listadepesoscop= []
ListaenEuros= []
ListaDolares= [20000, 30000, 4000, 2500, 1000, 7600]
#--conversion--#
Listadepesoscop= []
for elemento in ListaDolares:
    conversor= round (elemento * 3700, 2)
    Listadepesoscop.append (conversor)

ListaenEuros= []
for elemento in ListaDolares:
    conversor= round (elemento * 0.84, 2)
    ListaenEuros.append (conversor)

#--Clasificacion--#
for elemento in ListaDolares:
    Clasificacion= ''
    if (elemento < 1000):
        Clasificacion= 'Usted tiene ingresos mensuales bajos'
    elif(elemento>= 1000 and elemento <7000):
        Clasificacion= 'usted tiene ingresos mensuales medios'
    elif(elemento ==7000 and elemento < 20000):
        Clasificacion= 'usted tiene ingresos mensuales altos'
    else:
        Clasificacion= 'usted tiene ingresos mesuales elevados'
        ListaClasificacion.append(Clasificacion)


#--Punto1-- para hacer conversiones desde un lista de dolares--#
loquescogio= int(input(Escojaunaopcion))
while(loquescogio != 4):
    if(loquescogio == 1):
        opcionMoneda = input (ParaConvertir)
        if(opcionMoneda == 'C'):
            print(MensajePesoscop)
            print(Listadepesoscop)
        elif(opcionMoneda== 'D'):
            print(MensajeListaoriginal)
            print(ListaDolares)
        elif(opcionMoneda=='E'):
            print(MensajeEuros)
            print(ListaenEuros)
        else:
            print(MensajeError)
#--PUNTO2--para saber en que rango de ingresos esta usted--#
    elif (loquescogio==2):
        print(Mensajeopcion.format(2))
        print(ListaClasificacion)



