from typing import List
import matplotlib.pyplot as plt

tiempo=[0,1,2,3,4,5]
sensor=[4,5,6,8,9,10]
##################################
plt.title('grafico de sensor contra el tiempo')
plt.xlabel('tiempo (seg)')
plt.ylabel('Voltaje (Mv)')

#################################
plt.plot(tiempo,sensor,'g')
plt.show()


diccionario= {}
diccionario['NombresEstudiantes'] = ['jacobo','dani','maria','elena']
diccionario['edadestudiantes'] = [18,17,24,32]
diccionario['Peso'] = [84,56,64,57]
print(diccionario)
print(diccionario['edadestudiantes'][-1],diccionario['NombresEstudiantes'][-1],diccionario['Peso'][-1])




import pandas as pd
import matplotlib.pyplot as plt
ecgData = pd.read_csv('señales.csv',encoding='UTF-8',header=0,delim_whitespace=';').to_dict()
print(ecgData.keys())
tiempos = list(ecgData['Tiempo'].values())
print(tiempos)
voltajes= list(ecgData['Voltaje'].values())
print(voltajes)
plt.plot(tiempos, voltajes)
plt.show()