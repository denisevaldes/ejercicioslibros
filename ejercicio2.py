#write a program to prompt the user for hours and rate per hour to
#compute gross pay

horas = int(input('por favor introduzca las horas:\n'))
tasa_hora = float(input('por favor introduzca la tasa por hora \n'))
sueldo_bruto = horas * tasa_hora
print(sueldo_bruto)