#en un consultorio de neurologia 
#desea tener un archivo para el manejo de los clientes
#se pide que desarrolle un programa que en su primera ejecucion
#cree el archivo llamado pacientes.txt.
#luego en cada ejecucion se preguntara por el nombre del paciente, 
#una descripcion de la enfermedad y el precio de la consulta.

import sys
nombre= (input('Por favor ingrese su nombre : '))
Enfermedad= (input('danos una descrpcion de tu enfermedad o sintomas : '))
precio=input('El precio de la consulta te sale por : ')

nombreArchivo= 'Pacientes.txt'
try:
    archivo=open(nombreArchivo, 'a')
    print('1')
except FileNotFoundError:
    archivo=open(nombreArchivo,'w',encoding='UTF-8')
    descripcion= 'Archivo de datos de pacientes'
    print('2')
    archivo.writelines(descripcion)
    sys.exit(1)
print(archivo)
linea= "\ nombre : " + nombre +  "enfermedad : " + Enfermedad + " precio " + str(precio)
archivo.writelines(linea)
archivo.close()

with open(nombreArchivo) as reader:
    for line in reader:
        print(line)