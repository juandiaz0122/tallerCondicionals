# Realice una encuesta a un estudiante, las posibles respuestas son Si, No.
"""
a) Estudió para el exámen?
i. Respuesta SI: Continuar con siguiente pregunta
ii. Respuesta NO: Finalizar

b) Aprobó el examen?
i. Respuesta SI: Continuar con siguiente pregunta
ii. Respuesta NO: Mostrar mensaje, “Estudiar más...”

c) Su calificación (entre 0 a 5) fue mayor o igual a 3.5?
i. Respuesta SI: Continuar con siguiente pregunta
ii. Respuesta NO:
- Fue mayor a 2? Mostrar mensaje, “Casi lo logras...”
- Fue menor o igual a 2? Mostrar mensaje, “Debes
esforzarte mucho más...” 

d) Ya terminó el trimestre?
i. Respuesta SI: Mostrar mensaje, “Felicitaciones!!!”
ii. Respuesta NO: Mostrar mensaje “Continúa así..”
"""
pregunta1= input( "¿Estudió para el exámen?:\n" ) 

if pregunta1.lower() == "si":
    pregunta2 = input( "¿aprobó el exámen?:\n" )
    if pregunta2.lower() == "si":
        pregunta3= float(input( "¿cual es su calificación?:\n" ))
        if pregunta3 >= 3.5:
            pregunta4 = input( "¿ya terminó el semestre?:\n" )
            if pregunta4.lower() == "si":
                print("Felicitaciones")
            else:
                print( "continua así..." )
        else:
            if pregunta3 > 2:
                print( "!casi lo logras¡" )
            else:
                print( "debes esforzarte mucho más..." )
            
    else:
        print( "Estudiar más" )
        