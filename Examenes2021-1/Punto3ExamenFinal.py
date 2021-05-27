#Se sabe que un dolar son 0,82 euros
#indique a un usuario que ingrese su dinero en dolares y su nombre
#luego muestre en pantalla el nombre del usuario y cuanto dinero tiene en euros.

PreguntaNombre= input ('Ingrese su nombre por favor : ')
preguntaDinero= float(input('Ingrese su dinero en dolares para convertirselos a euros : '))
Euros=(preguntaDinero* 0.82)
print(f''' el usuario que queria hacer la conversion se llama {PreguntaNombre}, el cual nos dijo que 
tenia {preguntaDinero} dolares, por lo que al hacer la conversion le dijimos que cuenta con
{Euros} euros en su bolsillo.
''')
