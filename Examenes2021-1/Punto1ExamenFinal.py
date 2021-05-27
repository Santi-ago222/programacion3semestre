#Solicite a un usuario que ingrese sus 8 alimentos favoritos
#luego realice un grafico de barras con la informacion ingresada.

import matplotlib.pyplot as plt
lista1= []
lista2=[]
for i in range (8):
    Alimentos= input ('Por favor ingrese el nombre de su alimento favorito : ')
    lista1.append(Alimentos)
print(lista1)
for i in range (8):
    Precios= input('Ahora por favor digite sus respectivos precios : ')
    lista2.append(Precios)
print(lista2)

plt.bar(lista1,lista2, width=0.4, color= 'r')
plt.title('Alimentos favoritos de una persona y sus respectivos costos')
plt.xlabel('Alimentos')
plt.ylabel('Precios $')
plt.savefig ('graficoAlimentos.png')
plt.show()