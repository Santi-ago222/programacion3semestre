
MENSAJEDE_BIENVENIDA='''
Hola, Bienvenido al programa que te 
enseñara lo que es una prueba diagnostica ECG
y una prueba diagnostica PPG...

Finalmente te mostrare los grfaicos de cada una.
'''
print(MENSAJEDE_BIENVENIDA)
MENSAJE_ECG= '''
Las pruebas ECG o pruebas de esfuerzo son pruebas que le permiten al medico
determinar que tan bien esta funcionando su corazon, y se realizan por medio de 
un electrocardiograma'''
print(MENSAJE_ECG)

MENSAJE_PPG='''
El test PPG es una prueba que analiza los rasgos de un individuo
tales como:
-Autoestima
-Responsabilidad
-Estabilidad emocional
-Y la sociabilidad
'''
print(MENSAJE_PPG)

import pandas as pd
import matplotlib.pyplot as plt
ecgData= pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData.keys())
muestras = list(ecgData['muestra'].values())
print(muestras)
valores=list(ecgData['valor'].values())
print(valores)
plt.plot(muestras,valores)
plt.title('Diagnostico ECG --> electrocardiograma')
plt.xlabel('Muestra')
plt.ylabel('Valores')
plt.savefig('PruebaECG.png')

plt.show()

