#--Punto1--#
import matplotlib.pyplot as plt

Meses=['Enero','Febrero','marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
Ingresos= [230.000,180.000,1.000000,80.000,340.000,100.000,450.000,203.000,700.000,630.000,632.000, 100.000]

plt.bar (Meses, Ingresos, width= 0.6, color= 'g')
#############
plt.title('Ingresos del Año')
plt.xlabel('Meses del año')
plt.ylabel('Ingresos $')

plt.show()