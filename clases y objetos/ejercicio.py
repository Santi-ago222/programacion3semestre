#----ANIMAL FAVORITO---#
class Animal ():
    def __init__(self,caracteristica1,tamaño,caracteristica2):
        self.raza = 'pastor aleman'
        self.caracteristica= caracteristica1
        self.estaturaa= tamaño
        self.otracaracteristica= caracteristica2




    def atributos (self):
        print(f'''hola mi nombre es santiago y te hablare de algunos atributos sobre
        mi raza de perro favorita el {self.raza}, 
        1) primero {self.caracteristica}
        2) la estatura promedio es {self.estaturaa} centimetros
        3) {self.otracaracteristica}
        ''')

    def Correr (self, distancia, tiempo):
        for i in range (distancia):
            print(f''' mi raza de perro favorita es capaz de correr largas distancias
            en estos momentos se encuentra corriendo y lleva recorrido {i+1} metros 
            en {i+1} segundos
            ''')


pastorAleman= Animal ('son muy obedientes y nobles ', 62 ,'y por ultimo es muy usado en la labor de inteligencia policial')

print(pastorAleman.caracteristica)
print(pastorAleman.estaturaa)
print(pastorAleman.otracaracteristica)

pastorAleman.atributos()
pastorAleman.Correr(20,10)
