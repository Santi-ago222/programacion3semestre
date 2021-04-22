class Person ():
    def __init__(self,IDin,Nombrein):
        self.identificandolo= IDin
        self.nombreee= Nombrein
    def hablar (self, mensaje):
        print(f'mi nombre es {self.nombreee} me identifico con el numero {self.identificandolo} y tengo algo que decirte....', mensaje)
    def caminar (self, pasos):
        for i in range (pasos):
            print(f'Segun los pasos que ingresaste he recorrido {i+1} metros')


#--PUNTO2--#
class Doctor (Person):
    def __init__(self,IDin,Nombrein,AtribuIn):
        Person.__init__(self,IDin,Nombrein)
        self.atributo= AtribuIn
    def diagnosticar (self, enfermedad):
        print (f'''Hola soy el {self.atributo}, {self.nombreee} y 
        revisando su historia clinica pude
        notar que usted tiene una {enfermedad} leve, feliz dia!
        ''')

#--PUNTO3--#
class Nutrcionistaa (Person):
    def __init__(self,IDin,Nombrein,UniIn):
        Person.__init__(self,IDin,Nombrein,)
        self.egresado= UniIn
    def calcularIMC (self,pesoIn,altutraIn):
        IMC= pesoIn/altutraIn
        print(f'Hola soy la nutricionista {self.nombreee} y el resultado de tu imc es {IMC}')


#-PUNTO4--#
class abogado (Person):
    def __init__(self,Nombrein,IDin, AsesoradoIn,ProcesoIn):
        Person.__init__(self,IDin,Nombrein)
        self.Asesorado= AsesoradoIn
        self.Proceso = ProcesoIn
    def Accion (self):
        print(f'Hola soy el abogado {self.nombreee}, me identifico con el numero {self.identificandolo} estoy respaldando a el señor {self.Asesorado}, en el proceso de {self.proceso}')


persona1= Person(28393479,'Steffen')
persona1.hablar('Eres una persona muy especial para mi')
persona1.caminar(8)
print('#'*50)

medico= Doctor(778899,'Leonel', 'Pediatra')
medico.diagnosticar('Neumonia')
print('#'*50)

Nutricion= Nutrcionistaa(142245,'Vanesa','Universidad nacional de colombia')
calcularIMC= Nutricion.calcularIMC(80,1.76)

print('#'*50)
Donluis= abogado('Libardo',726383,'Falcao','demanda por alimentos')
Donluis.Accion ()
