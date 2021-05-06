#Grafico de trorta
import matplotlib.pyplot as plt
#Creamos los labels sizes y explode
#Labels: nombre de tortas
labels= ['Phyton','C++','Java','dart']
sizes=[20,30,40,10]
Pieexplode=[0,0,0.1,0]

plt.pie(sizes,labels=labels,explode=Pieexplode,shadow=True,startangle=45)
##########################
plt.title('Uso de lenguajes de programacion en el 2021')


##########################
plt.show()