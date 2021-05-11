#####PUNTO1########
import matplotlib.pyplot as plt
lista1= []
lista2=[]
for i in range (5):
    snacks= input('Por favor ingrese el nombre de su snack favorito para agregarlo a una lista : ')
    lista1.append(snacks)
print(lista1)
for i in range(5):
    precios= input('por favor ahora ingrese el precio de cada uno :')
    lista2.append(precios)
print(lista2)

plt.bar(lista1, lista2, width=0.5, color= 'b')
plt.title('Snacks favoritos de un Usuario')
plt.xlabel('Snacks')
plt.ylabel('Precios $')
plt.savefig('Graficodesnacks.png')
plt.show()


