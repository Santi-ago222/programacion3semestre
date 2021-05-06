import matplotlib.pyplot as plt

labels= ['Bogota','Medellin','Cali','Bucaramanga','Ibague']
sizes= [10.4, 2.6, 2.4, 1.3, 0.9]
Pieexplode=[0.1,0,0,0,0]

def porcentajes (sizes,labels,indicador= '-->'):
    acumulador= 0
    for elemento in sizes:
        acumulador += elemento
    for i in range(len(labels)):
        porcentajex = round(sizes[i]/acumulador*100, 2)
        labels[i] += indicador+str(porcentajex)+ 'Millones de personas'

porcentajes(sizes, labels,'*')

plt.pie(sizes,labels=labels,explode=Pieexplode,shadow=True,startangle=45)
##########################
plt.title('Ciudades mas grandes de colombia')
plt.savefig('ciudades.png')


##########################
plt.show()
