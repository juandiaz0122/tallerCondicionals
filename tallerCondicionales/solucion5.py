"""
#5. Averiguar si una hora en formato HH:MM es mayor que otra. También
indicar si las horas son iguales.
"""
hora1 = int( input("ingrese hora:\n") )
minuto1 = int( input("ingrese minuto:\n") )

hora2 = int( input("ingrese hora:\n") )
minuto2 = int( input("ingrese minuto:\n") )

if hora1 ==  hora2:
    if minuto1 == minuto2:
        print( "las horas son iguales" )
    elif minuto1 > minuto2:
        print(f"la hora1 {hora1} mayor a la hora2 {hora2} ")
    else:
        print( "la hora1 es menor a la hora2" )
elif hora1 > hora2:
    print( f"la hora1 {hora1} es mayor a la hora2 {hora2}" )
else:
    print( f"la hora1 {hora1} es menor a la hora2 {hora2}" )
    