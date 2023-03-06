# Construya un algoritmo para cada uno de los enunciados siguientes:
"""1. Un programador necesita saber cuánto cobrar por tres programas que le
pidieron desarrollar. Para calcularlo usar las siguientes fórmulas:

Costo = (LineasCodificadas / Tiempo) * $20.000
Precio= Costo + 10% del Costo

Primer Programa: Se demoró en realizarlo 45 horas y la cantidad de líneas
codificadas fueron 183. 

Segundo Programa: Escribió 629 líneas de código y se demoró en
realizarlo 200 horas. 

Tercer Programa: Escribió N líneas de código y se demoró en realizarlo
X horas
"""

horasPrimerPrograma= int( input("Ingrese número de horas\n") )
lineasPrimerPrograma= int( input("Ingrese lineas codíficadas\n") )


horasSegundoPrograma= int( input("Ingrese número de horas\n") )
lineasSegundoPrograma= int( input("Ingrese lineas codíficadas\n") )


horasTercerPrograma= int( input("Ingrese número de horas\n") )
lineasTercerPrograma= int( input("Ingrese lineas codíficadas\n") )

costo1= ( lineasPrimerPrograma / horasPrimerPrograma ) * 20000
precio1=  costo1 + (costo1 * 0.1 )   

costo2= (lineasSegundoPrograma / horasSegundoPrograma) * 20000
precio2= costo2 + (costo2 * 0.1)

costo3= (lineasTercerPrograma / horasTercerPrograma) * 20000
precio3= costo3 + (costo3 * 0.1)

print(f"el precio del programa 1 es: ${precio1} , el precio 2 es: ${precio2} y del 3 es: ${precio3}")
