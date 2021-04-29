import matplotlib.pyplot as plt
Paises= ['España','Inglaterra','Italia','Alemania','Brazil','Holanda','Francia']
Copas= [80,60,50,40,30,20,10]
plt.bar(Paises,Copas,width=0.5, color='r')
#########
plt.title('Numero de copas por paises')
plt.xlabel('Paises')
plt.ylabel('Copas')

###########
plt.show()