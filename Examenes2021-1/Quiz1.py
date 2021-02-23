#----constantes----#
MENSAJE_DE_BIENVENIDAA= "Bienvenido a tu programa de control  "
INGRESA_ELDATO= "Ingresa el valor de los trigliceridos : "
INGRESA_ELDATO2= "Ingresa el valor de la homocisteina : "
OPTIMOTRI= "Usted se encuentra dentro de los valores optimos para los trigliceridos "
OPTIMOHOMO= "Usted se encuentra dentro de los valores optimos para la homocisteina "
SOBRE_LIMITETRI= "Usted se encuentra sobre el limite de valores optimos para los trigliceridos "
SOBRE_LIMITEHOMO= "Usted se encuentra sobre el limite de valores optimos para los homocisteina "
ALTOTRI= "Usted esta dentro de los valores altos para los trigliceridos "
ALTOHOMO= "Usted esta dentro de los valores altos para la homocisteina "
MUYALTOTRI= "Usted se encuentra con los valores muy altos en los trigliceridos, tenga mucho cuidado"
MUYALTOHOMO= "Usted se encuentra con los valores muy altos en la homocisteina, tenga mucho cuidado"
#---CODIGOS---#
print(MENSAJE_DE_BIENVENIDAA)
Dato1= int(input(INGRESA_ELDATO))
Dato2= int(input(INGRESA_ELDATO2))
Isoptimotri= Dato1 < 150
IsoptimoHO= Dato2 >= 2 and Dato2 < 15
IssobrelimiteTRI= Dato1 >= 150 and Dato1 < 199
IssobrelimiteHO= Dato2 >= 15 and Dato2 < 30
IsaltoTRI= Dato1 >= 200 and Dato2 < 499
IsaltoHO= Dato2 >= 30 and Dato2 < 100
IsmuyaltoTRI= Dato1 > 500 
IsmuyaltoHO= Dato2 > 100

if(Isoptimotri):
    print(OPTIMOTRI)
elif(IssobrelimiteTRI):
    print(SOBRE_LIMITETRI)
elif(IsaltoTRI):
    print(ALTOTRI)
else:
    print(MUYALTOTRI)
#---homocisteina---#
if(IsoptimoHO):
    print(OPTIMOHOMO)
elif(IssobrelimiteHO):
    print(SOBRE_LIMITEHOMO)
elif(IsaltoHO):
    print(ALTOHOMO)
else:
    print(MUYALTOHOMO)


