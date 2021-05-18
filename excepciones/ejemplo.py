#ahora para decir que por favor ingrese un dato valido
iscorrectInfo= False
while(iscorrectInfo==False):
#Para corregir datos mal ingresados
    try:
        edad= int(input('ingrese su edad :'))
        iscorrectInfo= True
    except ValueError:
        print('ingresaste un dato no valido')

archivo= open('hola.txt')
