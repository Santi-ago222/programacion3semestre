class Humano ():
    def __init__ (self, nombreEntrada, EdadEntrada, EstaturaEntrada):
        print('Hola, soy un humano nuevo')
        self.edad= EdadEntrada
        self.raza= 'Humano'
        self.nombre= nombreEntrada
        self.estatura= EstaturaEntrada
        self.dinero = 0
    def hablar (self, mensaje):
        print(f'hola soy {self.nombre} mido {self.estatura} y tengo un mensaje que decir...', mensaje)
    

    def MostrarAtributos (self):
        print(f'''Hola soy el humano y me presentare :
            mi nombres es {self.nombre}
            mido {self.estatura} metros
            tengo {self.edad} años
            Y tengo ahorrad0 {self.dinero}
        ''')
    
    def RecorrerDistancia (self,distancia):
        for i in range(distancia):
            print(f'''hola soy {self.nombre}
            y he recorrido {i+1} metros
            ''')
    
    def Ahorrardinero (self):
        preguntaingresarMonto= 'ingrese S--> para continuar añadiendo montos y N--> para finalizar : '
        preguntaMonto= 'Cuanto vas a ingresar? : '
        ingresarMonto= input(preguntaingresarMonto)
        while(preguntaingresarMonto != 'N'):
            monto= float(input(preguntaMonto))
            self.dinero= self.dinero +monto
            print(f'hola soy {self.nombre} y tengo {self.dinero} pesos')
        return self.dinero


class ingeniero (Humano):
    def __init__(self,nombreEntrada,EdadEntrada,EstaturaEntrada):
        self.area= areaEntrada
    def solucionarProblemas(self,problema):
        print(f'hola soy un ingeniero y me llamo {self.nombre}, y procedo a solucionar el problema {problema}')
class Programador (Humano):
    def crearAlgoritmo (self,problema):
        print(f'Hola soy {self.nombre} y procedo a resolver el algoritmo {algoritmo}')

class Biomedico(ingeniero,Programador):
    def mantenimientoEquiposMedicos(self,nombreEquipo):
        print(f'hola sou{self.nombre} y procedo a arreglar el {nombreEquipo}')

class abogado (Humano):
    def levantarAcciondeTutela(self,nombrecliente):
        print(f'hola soy {self.nombre} y estoy representando a {nombrecliente} ')


humano1 = Humano('Santiago', 18, 1.76)
humano2= Humano('Maria', 16, 1.89)

humano1.hablar('Espero que todo este muy bien ')
humano2.hablar('chao')
print(humano1.nombre)
print(humano2.nombre)
print(humano1.edad)
print(humano2.edad)
print(humano1.estatura)
print(humano2.estatura)

humano1.MostrarAtributos()
humano2.MostrarAtributos()

humano1.RecorrerDistancia(25)
humano2.RecorrerDistancia(25)

totalahorrado= humano1.Ahorrardinero()
print(totalahorrado)

biomedico1= Biomedico ('karla',20,1.63,'Biomedicina')
biomedico1.RecorrerDistancia(25)
biomedico1.MostrarAtributos()
biomedico1.mantenimientoEquiposMedicos('Electrocardiograma')

abogado1= abogado('Stiven',34,1.94)
abogado1.MostrarAtributos()
abogado1.levantarAcciondeTutela(biomedico1.nombre)
biomedico1.crearAlgoritmo('fibonacci')
biomedico1.solucionarProblemas('ocupacion alta de camas uci')
print(biomedico1.area)



