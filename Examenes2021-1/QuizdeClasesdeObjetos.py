#GRUPO 11 -- SANTIAGO AMAYA-- SANTIAGO BERMUDEZ#

#PUNTO1#
class ElementosDigitales ():
    def __init__(self, Nombrein, CreadorIn,FechaIn):
        self.nombre= Nombrein
        self.creador= CreadorIn
        self.Fecha= FechaIn
    def mostrarAtributtos(self):
        print(f''' este es el elemento  {self.nombre}, creado por  la empresa {self.creador} y la fecha 
        de creacion fue {self.Fecha}
        ''')
class Usuario ():
    def __init__(self,Nombree,edadIn,sexoIn,nacionalidadIn,CancionIn):
        self.nombre = Nombree
        self.edad= edadIn
        self.sexo= sexoIn
        self.nacionalidad = nacionalidadIn
        self.cancion = CancionIn
    def MostrandoAtributos (self):
        print(f'''Hola soy {self.nombre}, tengo {self.edad} años soy de sexo {self.sexo}...
        tengo nacionalida {self.nacionalidad} y estoy escuchando la cancion {self.cancion} de eminen
        ''')
class Pagina ():
    def __init__(self,TipodeConIn, FormatoIn,FechaDepIn):
        self.tipodecontenido= TipodeConIn
        self.formato= FormatoIn
        self.fecha=FechaDepIn
    def DefiniendoAtributos (self):
        print(f'''esta es una pagina que publica {self.tipodecontenido} en el año {self.fecha}
        en el formato {self.formato}
        ''')
class Cancion (ElementosDigitales):
    def __init__(self, Nombrein, CreadorIn, FechaIn,GeneroIn,DuracionIN,Nombrenueva,Fechanueva):
        ElementosDigitales.__init__(self, Nombrein, CreadorIn, FechaIn)
        self.genero = GeneroIn
        self.fecha= FechaIn
        self.cancionnueva= Nombrenueva
        self.fechanueva = Fechanueva
        self.duracion =DuracionIN
    def NuevaCancion(self):
        print(f'''
        este es el elemento  {self.nombre}, creado por  la empresa {self.creador} y la fecha 
        de creacion fue {self.Fecha}
        ademas presentamos 
        Esta nueva cancion llamada {self.cancionnueva}
        que tiene una duracion de {self.duracion} segundos y es 
        del genero musical {self.genero}, 
        publicada en el año {self.fechanueva}
        ''')
    def repticion (self, repetir):
        for i in range (repetir):
            print(f'sonando la cancion {self.cancionnueva} {i+1} veces')
class Artista (Usuario):
    def __init__(self,Nombree,edadIn,sexoIn,nacionalidadIn,CancionIn,GeneroM,NmeroCanciones,NmeroAlmb,CiudadIn):
        self.nombre = Nombree
        self.edad= edadIn
        self.sexo= sexoIn
        self.nacionalidad = nacionalidadIn
        self.cancion = CancionIn
        self.numerocanciones= NmeroCanciones
        self.numeroAlmbunes= NmeroAlmb
        self.generomusical=GeneroM
        self.ciudad= CiudadIn
        print(f'''Hola soy el artista {self.nombre}, tengo {self.edad} años soy de sexo {self.sexo}...
        tengo nacionalidad {self.nacionalidad}.
        y voy a inagurar mi almbum numero {self.numeroAlmbunes} del genero musical {self.generomusical}
        y tengo programado hacerlo en la ciudad de {self.ciudad} donde voy cantar {self.numerocanciones} canciones
        entre las mas pedidas esta la cancion : {self.cancion}
        
        ''')
class Favoritos (Pagina):
    def __init__(self,TipodeConIn, FormatoIn,FechaDepIn,Listafav,fechaultima):
        self.listaFavoritos= Listafav
        self.fechaUl= fechaultima
    def Atributos (self,Listafav,fechaultima):
        print(f'''la lista de canciones favoritas por la comunidad es {self.listaFavoritos}
        y se actualizo el {self.fechaUl}
        ''')





elemento= ElementosDigitales('PS5','Sony',1970)
elemento.mostrarAtributtos()
print('#'*40)

Persona= Usuario('Santiago',19,'masculino','colombiano','Explicito')
Persona.MostrandoAtributos()
print('#'*40)

Cantante= Pagina('Ensayos','Phyton',2000)
Cantante.DefiniendoAtributos()
print('#'*40)

CancionNueva= Cancion('PS5','Sony',1970,'baladas', 342, 'Donde estan las gatas',1970)
CancionNueva.NuevaCancion()
print('#'*40)

CancionNueva.repticion(5)
print('#'*40)

Pablo= Artista('santiago',19,'masculino','colombiana','explicito','trap','3','5','Medellin')
print('#'*40)

comunidad=Favoritos('ensayo','pdf',1839,'bailando,tropical,tocando',2010)
comunidad.Atributos('bailando,tropical,tocando', 2010)