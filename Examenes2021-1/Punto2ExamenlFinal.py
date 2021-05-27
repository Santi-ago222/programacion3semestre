#Cree una clase humano con atributos 
#nombre, sexo, edad y con la accion hablar
#donde dado un mensaje se mostrara en pantalla
#luego cree una clase Doctor que herede de humano
#y tenga la accion adicional de que dado Un Peso 
#y una estatura, calcule el IMC.

class Humano ():
    def __init__(self,Nombrein,SexoIn,EdadIn):
        self.nombre=Nombrein
        self.edad=EdadIn
        self.sexo=SexoIn
    def Hablar (self):
        print(f''' Hola cordial saludo, mi nombre es {self.nombre}
        mi objetivo es presentarme, para entablar una conversacion, entonces;
        tengo tengo {self.edad} años y soy de sexo {self.sexo}.
        Ahora espero que tu te presentes para comenzar a hablar.
        ''')

class Doctor (Humano):
    def __init__(self, Nombrein, SexoIn, EdadIn, PesoIn, estaturaIn):
        self.nombre=Nombrein
        self.edad=EdadIn
        self.sexo=SexoIn
        self.peso= PesoIn
        self.estatura= estaturaIn
        print(f''' Hola soy el doctor {self.nombre} de sexo {self.sexo},
        tengo {self.edad} años, y como mi objetivo es calcularte tu IMC...
        entonces segun los datos que me arroja el sistema de tu estatura y peso
        Tu Indice de masa Corporal es de : {PesoIn / estaturaIn**2}... te encuentras dentro del rango normal
        felicitaciones!!!
        ''')



Persona= Humano('Gustavo adolfo','Masculino', 25)
Persona.Hablar()
print('#'*40)

Medico= Doctor('Gustavo adolfo', 'Masculino',25, 65, 1.75)
