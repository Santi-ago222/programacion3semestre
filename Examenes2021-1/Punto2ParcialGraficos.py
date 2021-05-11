
import matplotlib.pyplot as plt
ciudadesfavoritas= []
Sizes=[]
Pieexplode=[0,0,0.1,0,0]
for i in range(5):
    ciudades= input('Por favor ingrese su ciudad favorita para agregarla a una lista :')
    ciudadesfavoritas.append(ciudades)
print(ciudadesfavoritas)

for i in range(5):
    poblacion= input ('Ahora ingrese su respectiva poblacion :')
    Sizes.append(poblacion)
print(Sizes)


plt.pie(Sizes, labels=ciudadesfavoritas, explode=Pieexplode,shadow=True)
plt.title('Datos demograficos de 5 ciudades')
plt.xlabel('Ciudades favoritas')
plt.savefig('Datosdemograficos.png')
plt.show()
