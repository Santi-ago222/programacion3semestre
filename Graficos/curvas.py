import matplotlib.pyplot as plt

tiempo=[0,1,2,3,4,5]
sensor=[4,5,6,8,9,10]

plt.title('grafico de sensor contra el tiempo')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (Mv)')

plt.plot(tiempo,sensor,'g')
plt.show()