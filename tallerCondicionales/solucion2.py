# Comparar cual de los tres es más caro.

horasPrimerPrograma= int( input("Ingrese número de horas\n") )
lineasPrimerPrograma= int( input("Ingrese lineas codíficadas\n") )


horasSegundoPrograma= int( input("Ingrese número de horas\n") )
lineasSegundoPrograma= int( input("Ingrese lineas codíficadas\n") )


horasTercerPrograma= int( input("Ingrese número de horas:\n") )
lineasTercerPrograma= int( input("Ingrese lineas codíficadas\n") )

costo1= ( lineasPrimerPrograma / horasPrimerPrograma ) * 20000
precio1=  costo1 + (costo1 * 0.1 )   

costo2= (lineasSegundoPrograma / horasSegundoPrograma) * 20000
precio2= costo2 + (costo2 * 0.1)

costo3= (lineasTercerPrograma / horasTercerPrograma) * 20000
precio3= costo3 + (costo3 * 0.1)

print(f"el precio del programa 1 es: ${precio1} , el precio 2 es: ${precio2} y del 3 es: ${precio3}")
  
if precio1>precio2 and precio1>precio3:
    print("El precio1 es mayor al precio2 y precio3 ")
elif precio2>precio1 and precio2>precio3:
    print("El precio2 es mayor al precio1 y al precio3 ")
elif precio3>precio1 and precio3>precio2:
    print("El precio3 es mayor al precio1 y al pecio2")

