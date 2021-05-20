import sys  #permite que un codigo  se deje de eejecutar
nombre= (input('Por favor ingrese su nombre : '))
edad= int(input('Por favor ingrese su edad : '))
estatura= float(input('Ingrese su estatura : '))

nomreArchivo= 'estudiantes.txt'
try:
    archivo=open(nomreArchivo,'a')  
    print('1')
except FileNotFoundError:
    archivo = open(nomreArchivo, 'w',encoding='UTF-8')
    descripcion= 'Archivo de datos de estudiantes '
    print('2')
    archivo.writelines(descripcion)
    sys.exit(1)
print(archivo)
linea = "\nnombre :" + nombre +  "edad  :" +  str(edad)  +  "estatura : "+  str(estatura)
archivo.writelines(linea)
archivo.close()
#\n --> es para dar enter

#LEER
with open(nomreArchivo) as reader:
    for line in reader:
        print(line)