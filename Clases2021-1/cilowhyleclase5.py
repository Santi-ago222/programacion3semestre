#---ahorrandoparaunpc---#
#---mensajes---#
SALUDAR= "bienvenido, te ayudare ahorrando : "
PREGUNTAR_VALOR_PC= 'Cuanto vale, el PC que deseas? : '
PREGUNTAR_CUANTO_TIENE= 'cuanto tienes ahorrado ? :'
MENSAJE_AHORRADO = 'LLEVAS AHORRADO : '
MENSAJE_COMPLETO= 'lo que tienes te alcanza para comprar tu pc'
MESNAJE_NOALCANZA= 'lo que tienes aun no te alcanza para comprar el pc. '
HOYTENEMOS= "si le sumamos un peso a el valor que tenias ayer, hoy tenemos: "

#---ENTRADAS---#
print (SALUDAR)
valor= int(input(PREGUNTAR_VALOR_PC))
ahorrado= int(input(PREGUNTAR_CUANTO_TIENE))
if(ahorrado>=valor):
    print(MENSAJE_COMPLETO)
#-------------#
while(valor>ahorrado):
    print(MESNAJE_NOALCANZA, "te ayudare a ahorrar, un peso por dia")
    print(HOYTENEMOS, ahorrado,"pesos", " y te hacen faltan :", valor-ahorrado,"pesos" )
    ahorrado= ahorrado +1
    print(valor==ahorrado)
print("muy bien ya alcanzamos lo que te faltaba para comprar el pc, felicitaciones")


