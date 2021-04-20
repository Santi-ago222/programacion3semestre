#PUNTO 1#
class Torta ():
    def __init__(self,EntradaSabor,EntradaAltura,entradaForma,EntradaPrecio):
        print('Hola te vengo a describir una rica torta')
        self.sabor= EntradaSabor
        self.altura=EntradaAltura
        self.forma=entradaForma
        self.precio=EntradaPrecio
    def Atributos (self):
        print(f'''La torta es de un sabor {self.sabor}
        muy deliciosa!!, el tamaño es de {self.altura} centimetros
        tiene forma {self.forma} y su precio tan solo es de
        {self.precio} pesos
            ''')


Pastel= Torta('Tres leches', 20,'Rectangular',9.000)
Pastel.Atributos()
print('#'*30)

#PUNTO2#
class Estudiante ():
    def __init__(self,entradanombre,entradaEdad,Identificacion,entradaCarrera,EntradaSemestre,materia,HorasdeEstudio):
        self.nombre= entradanombre
        self.edad=entradaEdad
        self.id=Identificacion
        self.carrera=entradaCarrera
        self.semestre=EntradaSemestre
        self.Asignatura=materia
        self.Horas=HorasdeEstudio
        self.Asignatura=materia
        self.Horas=HorasdeEstudio
    def muestraAtributos (self):
        print(f'''Hola mi nombres es {self.nombre},
        tengo {self.edad} años , estoy estudiando 
        {self.carrera}, en el carnet estudiantil me dieron el numero :
        {self.id}... y estoy en {self.semestre}
        
        
        Ademas voy a ver la materia de {self.Asignatura} en {self.Horas} horas.
        Gracias por su atencion!!!
        ''')


Alumno= Estudiante('Santiago Bermudez', 18, 92883892,'Ingenieria Biomedica','Tercer semestre','Morfofisiologia', 23893)
Alumno.muestraAtributos()
print('#'*30)

#PUNTO3#
class Nutricionista ():
    def __init__(self,años,sellama,Uni):
        self.edad=años
        self.nombre=sellama
        self.Universidad=Uni
    def LosAtributos(self):
        print(f'''Hola mi nombres es {self.nombre}
        tengo {self.edad} y soy egresado de la universidad {self.Universidad}
        ''')

Profesional= Nutricionista(19,'Sebastian','La sabana')
Profesional.LosAtributos()
print('#'*30)
#PUNTO4#
class Canguro ():
    def __init__(self,EntrandoEdad,NmroID,Mellamo):
        self.eedad=EntrandoEdad
        self.ID=NmroID
        self.noombre=Mellamo
    def especificandoCanguro(self):
        print(f'''Hola soy un canguro australiano, mi nombres es
        {self.noombre}, soy un joven de {self.eedad} años
        y en la reserva me identifican como {self.ID}
        ''')
    def Saltando (self, saltar):
        for i in range (saltar):
            print(f''' Hola soy {self.noombre} el canguro
            y he dado {i+1} saltos
            ''')

Animal=Canguro(6, 172839, 'messi')
Animal.Saltando(12)
print('#'*30)

#PUNTO 5#
class Instrumento ():
    def __init__(self,nombre,Tamaño,tipo,costo,Musica):
        self.talla= Tamaño
        self.clase= tipo
        self.Nnombre= nombre
        self.Precio= costo
        self.Cancion=Musica

    def Definiendolo (self):
        print(f'''
        Holaa, mi instrumento favorito es el {self.Nnombre}
        es un instrumento de tipo {self.clase}, tiene un tamaño de {self.talla} centimetros
        y tiene un precio de {self.Precio} dolares

        Ahora voy a interpretar la cancion que me dijeron
        osea {self.cancion} de carlos vives
        ''')

Musica=Instrumento('Piano', 100,'armonico', 230,'Bailar contigo')
Musica.Definiendolo()