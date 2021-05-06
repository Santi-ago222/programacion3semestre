#--Punto1--#
import matplotlib.pyplot as plt

Meses=['Enero','Febrero','marzo','Abril','Mayo','Junio','Julio']
Ingresos= [230.000,350.000,500.000,80.000,340.000,100.000,450.000]

plt.bar (Meses, Ingresos, width= 0.5, color= 'g')
#############
plt.title('Ingresos del Año')
plt.xlabel('Meses del año')
plt.ylabel('Ingresos $')

plt.savefig('Ingresos de un trabajador.png')
plt.show()